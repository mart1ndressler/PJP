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
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__': main()