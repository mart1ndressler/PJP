from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):
    def __init__(self): self.symtab = {}
    def lab7_visitMulDiv(self, left, right, op, ctx):
        if op == '*': return left * right
        else:
            if right == 0: raise ZeroDivisionError("Division by zero")
            return left // right

    def lab7_visitAddSub(self, left, right, op):
        if op == '+': return left + right
        else: return left - right

    def visitParens(self, ctx): return self.visit(ctx.expr())
    def visitNumber(self, ctx):
        txt = ctx.getText()
        if txt.startswith("0x") or txt.startswith("0X"): return int(txt, 16)
        elif txt.startswith("0") and len(txt) > 1: return int(txt, 8)
        return int(txt)

    def visitDecl(self, ctx):
        vartype = ctx.type_().getText()
        for idCtx in ctx.idList().ID():
            name = idCtx.getText()
            self.symtab[name] = {'type': vartype, 'value': None}
        return None

    def visitAssignment(self, ctx):
        if ctx.getChildCount() == 3:
            left_node = ctx.addExpr()
            if left_node.getChildCount() == 1 and left_node.getText().isalpha(): varName = left_node.getText()
            else: raise Exception(f"{ctx.start.line}:{ctx.start.column} - Left-hand side of assignment must be a variable.")
            if varName not in self.symtab: raise Exception(f"{ctx.start.line}:{ctx.start.column} - Variable '{varName}' is not declared.")
            rightVal = self.visit(ctx.assignExpr())
            varType = self.symtab[varName]['type']
            if varType == 'int' and isinstance(rightVal, float): raise Exception(f"{ctx.start.line}:{ctx.start.column} - Variable '{varName}' is of type int, but the assigned value is float.")
            if varType == 'float' and isinstance(rightVal, int): rightVal = float(rightVal)
            self.symtab[varName]['value'] = rightVal
            return rightVal
        else: return self.visit(ctx.addExpr())

    def visitAddSub(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.addExpr())
            right = self.visit(ctx.multExpr())
            op = ctx.op.text
            return self.lab7_visitAddSub(left, right, op)
        else: return self.visit(ctx.multExpr())

    def visitMulDivMod(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.multExpr())
            right = self.visit(ctx.atom())
            op = ctx.op.text
            if op == '%':
                if not (isinstance(left, int) and isinstance(right, int)): raise Exception(f"{ctx.start.line}:{ctx.start.column} - The modulo operator can only be used with integer values.")
                return left % right
            else:
                if op == '/':
                    if right == 0 or right == 0.0: raise ZeroDivisionError("Division by zero")
                    if isinstance(left, float) or isinstance(right, float): return left / right
                    else: return left // right
                else: return left * right
        else: return self.visit(ctx.atom())

    def visitVariable(self, ctx):
        varName = ctx.getText()
        if varName not in self.symtab: raise Exception(f"{ctx.start.line}:{ctx.start.column} - Variable '{varName}' is not declared.")
        value = self.symtab[varName]['value']
        if value is None: raise Exception(f"{ctx.start.line}:{ctx.start.column} - Variable '{varName}' does not have an assigned value.")
        return value

    def visitFloat(self, ctx): return float(ctx.getText())
    def visitProg(self, ctx):
        for stat in ctx.stat():
            try:
                if stat.decl(): self.visit(stat.decl())
                else:
                    result = self.visit(stat.expr())
                    print(result)
            except Exception as e: print(e)
        return None

class CodeGenVisitor(ExprVisitor):
    def __init__(self): self.symtab = {}
    def visitDecl(self, ctx):
        vartype = ctx.type_().getText()
        ctype = "I" if vartype == "int" else "F"
        code = []
        for idCtx in ctx.idList().ID():
            varName = idCtx.getText()
            self.symtab[varName] = {'type': vartype, 'codeType': ctype}
            code.append(f"PUSH {ctype} 0")
            code.append(f"SAVE {ctype} {varName}")
        return (code, None)
    
    def visitNumber(self, ctx):
        txt = ctx.getText()
        if txt.startswith("0x") or txt.startswith("0X"): value = int(txt, 16)
        elif txt.startswith("0") and len(txt) > 1: value = int(txt, 8)
        else: value = int(txt)
        return ([f"PUSH I {value}"], "I")
    
    def visitFloat(self, ctx): return ([f"PUSH F {ctx.getText()}"], "F")
    def visitParens(self, ctx): return self.visit(ctx.expr())
    def visitVariable(self, ctx):
        varName = ctx.getText()
        if varName not in self.symtab: raise Exception(f"{ctx.start.line}:{ctx.start.column} - Variable '{varName}' is not declared.")
        ctype = self.symtab[varName]['codeType']
        return ([f"LOAD {varName}"], ctype)
    
    def visitAssignment(self, ctx):
        if ctx.getChildCount() == 3:
            left_node = ctx.addExpr()
            if left_node.getChildCount() == 1 and left_node.getText().isalpha(): varName = left_node.getText()
            else: raise Exception(f"{ctx.start.line}:{ctx.start.column} - Left-hand side of assignment must be a variable.")
            if varName not in self.symtab: raise Exception(f"{ctx.start.line}:{ctx.start.column} - Variable '{varName}' is not declared.")
            code_right, rtype = self.visit(ctx.assignExpr())
            varType = self.symtab[varName]['type']
            var_ctype = self.symtab[varName]['codeType']
            if varType == "int" and rtype == "F": raise Exception(f"{ctx.start.line}:{ctx.start.column} - Variable '{varName}' is of type int, but the assigned value is float.")
            code = code_right + [f"SAVE {var_ctype} {varName}", f"LOAD {varName}"]
            return (code, var_ctype)
        else: return self.visit(ctx.addExpr())
    
    def visitAddSub(self, ctx):
        left_code, left_type = self.visit(ctx.addExpr())
        right_code, right_type = self.visit(ctx.multExpr())
        res_type = "I" if (left_type == "I" and right_type == "I") else "F"
        instr = "ADD" if ctx.op.text == "+" else "SUB"
        code = left_code + right_code + [instr]
        return (code, res_type)
    
    def visitMulDivMod(self, ctx):
        left_code, left_type = self.visit(ctx.multExpr())
        right_code, right_type = self.visit(ctx.atom())
        op = ctx.op.text
        if op == '%':
            if not (left_type == "I" and right_type == "I"): raise Exception(f"{ctx.start.line}:{ctx.start.column} - The modulo operator can only be used with integer values.")
            instr = "MOD"
            res_type = "I"
        elif op == '/':
            instr = "DIV"
            res_type = "F" if (left_type == "F" or right_type == "F") else "I"
        else:
            instr = "MUL"
            res_type = "F" if (left_type == "F" or right_type == "F") else "I"
        code = left_code + right_code + [instr]
        return (code, res_type)
    
    def visitToMult(self, ctx): return self.visit(ctx.multExpr())
    def visitToAtom(self, ctx): return self.visit(ctx.atom())
    def visitProg(self, ctx):
        program = []
        for stat in ctx.stat():
            if stat.decl():
                code_decl, _ = self.visit(stat.decl())
                program.extend(code_decl)
            else:
                code_expr, etype = self.visit(stat.expr())
                program.extend(code_expr)
                program.append(f"PRINT {etype}")
        return program

def main():
    lines = []
    while True:
        try: line = input()
        except EOFError: break
        if line.strip() == "": break
        lines.append(line) 
    data = "\n".join(lines).strip()
    if not data: return
    
    lexer = ExprLexer(InputStream(data))
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    
    try: tree = parser.prog()
    except Exception as e:
        print(e)
        return

    print("=== Evaluation Output ===")
    evalVisitor = EvalVisitor()
    evalVisitor.visit(tree)
    
    print("\n=== Generated Code ===")
    codeGenVisitor = CodeGenVisitor()
    try:
        program = codeGenVisitor.visit(tree)
        for instr in program: print(instr)
    except Exception as e: print(e)

if __name__ == '__main__': main()