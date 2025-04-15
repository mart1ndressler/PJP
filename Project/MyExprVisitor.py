from ExprVisitor import ExprVisitor
from ExprParser import ExprParser
from enum import Enum

class VarType(Enum):
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    STRING = "string"

class MyExprVisitor(ExprVisitor):
    def __init__(self):
        self.symbols, self.errors = {}, []

    def str_to_type(self, type_str):
        if type_str == "int": 
            return VarType.INT
        elif type_str == "float": 
            return VarType.FLOAT
        elif type_str == "bool": 
            return VarType.BOOL
        elif type_str == "string": 
            return VarType.STRING
        else: return None

    def visitDeclarationStatement(self, ctx):
        type_ctx = ctx.declStmt().getTypedRuleContext(ExprParser.TypeContext, 0)
        type_str = type_ctx.getText()
        var_type = self.str_to_type(type_str)
        for id_tok in ctx.declStmt().idList().Identifier():
            var_name = id_tok.getText()
            if var_name in self.symbols:
                self.errors.append(f"Error: Variable '{var_name}' is already declared.")
            else:
                self.symbols[var_name] = var_type
        return None

    def visitReadStatement(self, ctx):
        text = ctx.getText()
        if text.startswith("read"): text = text[len("read"):]
        if text.endswith(";"): text = text[:-1]
        text = text.strip()
        if text:
            identifiers = [s.strip() for s in text.split(',')]
            for var_name in identifiers:
                if var_name not in self.symbols:
                    self.errors.append(f"Error: Variable '{var_name}' is not declared (read).")
        else:
            self.errors.append("Error: No identifier list found in read statement.")
        return None

    def visitWriteStatement(self, ctx):
        expr_list_ctx = ctx.writeStmt().exprList()
        if expr_list_ctx is None:
            self.errors.append("Error: No expression list found in write statement.")
            return None
        
        expr_nodes = expr_list_ctx.expr()
        if not expr_nodes:
            self.errors.append("Error: No expressions found in write statement.")
            return None

        for expr in expr_nodes:
            self.visit(expr)
        return None

    def visitExpressionStatement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitAssignExpr(self, ctx):
        var_name = ctx.Identifier().getText()
        if var_name not in self.symbols:
            self.errors.append(f"Error: Variable '{var_name}' is not declared (assignment).")
            left_type = None
        else:
            left_type = self.symbols[var_name]
        right_type = self.visit(ctx.expr())
        if left_type is None:
            return None
        if not self.is_compatible(left_type, right_type):
            self.errors.append(f"Error: Cannot assign value of type '{right_type.value if right_type else 'None'}' to variable of type '{left_type.value}'.")
        return left_type

    def visitLogicalOrExpr(self, ctx):
        left_type = self.visit(ctx.logicalAndExpr(0))
        for i in range(1, len(ctx.logicalAndExpr())):
            op = ctx.getChild(2*i - 1).getText()
            right_type = self.visit(ctx.logicalAndExpr(i))

            if left_type != VarType.BOOL or right_type != VarType.BOOL:
                self.errors.append(f"Error: Operator '{op}' requires bool operands, got '{left_type.value if left_type else 'None'}' and '{right_type.value if right_type else 'None'}'.")
            left_type = VarType.BOOL
        return left_type

    def visitLogicalAndExpr(self, ctx):
        left_type = self.visit(ctx.equalityExpr(0))
        for i in range(1, len(ctx.equalityExpr())):
            op = ctx.getChild(2*i - 1).getText()
            right_type = self.visit(ctx.equalityExpr(i))

            if left_type != VarType.BOOL or right_type != VarType.BOOL:
                self.errors.append(f"Error: Operator '{op}' requires bool operands, got '{left_type.value if left_type else 'None'}' and '{right_type.value if right_type else 'None'}'.")
            left_type = VarType.BOOL
        return left_type
    
    def visitEqualityExpr(self, ctx):
        left_type = self.visit(ctx.relationalExpr(0))
        for i in range(1, len(ctx.relationalExpr())):
            op = ctx.getChild(2*i - 1).getText()
            right_type = self.visit(ctx.relationalExpr(i))
            allowed_for_eq = (VarType.INT, VarType.FLOAT, VarType.STRING)

            if left_type not in allowed_for_eq or right_type not in allowed_for_eq:
                self.errors.append(f"Error: Operator '{op}' only supports int, float, or string, got '{left_type.value}' and '{right_type.value}'.")
            elif left_type != right_type:
                self.errors.append(f"Error: Cannot compare '{left_type.value}' and '{right_type.value}' with '{op}'.")
            left_type = VarType.BOOL
        return left_type

    def visitAdditiveExpr(self, ctx):
        result_type = self.visit(ctx.multiplicativeExpr(0))
        for i in range(1, len(ctx.multiplicativeExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right_type = self.visit(ctx.multiplicativeExpr(i))
            if op in ['+', '-']:
                if self.is_numeric(result_type) and self.is_numeric(right_type):
                    result_type = VarType.FLOAT if(result_type == VarType.FLOAT or right_type == VarType.FLOAT) else VarType.INT
                else:
                    self.errors.append(f"Error: Operator '{op}' requires numeric types, got '{result_type.value}' and '{right_type.value}'.")
            elif op == '.':
                if result_type != VarType.STRING or right_type != VarType.STRING:
                    self.errors.append(f"Error: Operator '.' requires string types, got '{result_type.value}' and '{right_type.value}'.")
                    result_type = None
                else:
                    result_type = VarType.STRING
        return result_type

    def visitMultiplicativeExpr(self, ctx):
        result_type = self.visit(ctx.unaryExpr(0))
        for i in range(1, len(ctx.unaryExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right_type = self.visit(ctx.unaryExpr(i))
            if op in ['*', '/']:
                if self.is_numeric(result_type) and self.is_numeric(right_type):
                    result_type = VarType.FLOAT if (result_type == VarType.FLOAT or right_type == VarType.FLOAT) else VarType.INT
                else:
                    self.errors.append(f"Error: Operator '{op}' requires numeric types, got '{result_type.value}' and '{right_type.value}'.")
            elif op == '%':
                if result_type == VarType.INT and right_type == VarType.INT:
                    result_type = VarType.INT
                else:
                    self.errors.append(f"Error: Operator '%' requires int types, got '{result_type.value}' and '{right_type.value}'.")
        return result_type

    def visitUnaryExpr(self, ctx):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            operand_type = self.visit(ctx.unaryExpr())
            if op == '-':
                if not self.is_numeric(operand_type):
                    self.errors.append(f"Error: Unary minus requires numeric type, got '{operand_type.value if operand_type else 'None'}'.")
                return operand_type
            elif op == '!':
                if operand_type != VarType.BOOL:
                    self.errors.append(f"Error: '!' operator requires bool, got '{operand_type.value if operand_type else 'None'}'.")
                return VarType.BOOL
        else:
            return self.visit(ctx.primaryExpr())

    def visitPrimaryExpr(self, ctx):
        if ctx.getChildCount() == 3: 
            return self.visit(ctx.expr())
        elif ctx.literal() is not None: 
            return self.visit(ctx.literal())
        elif ctx.Identifier() is not None:
            var_name = ctx.Identifier().getText()
            if var_name not in self.symbols:
                self.errors.append(f"Error: Variable '{var_name}' is not declared (usage).")
                return None
            return self.symbols[var_name]
        else: return None

    def visitLiteral(self, ctx):
        if ctx.IntegerLiteral() is not None: 
            return VarType.INT
        elif ctx.FloatLiteral() is not None: 
            return VarType.FLOAT
        elif ctx.BooleanLiteral() is not None: 
            return VarType.BOOL
        elif ctx.StringLiteral() is not None: 
            return VarType.STRING
        else: return None

    def is_numeric(self, typ): 
        return typ in (VarType.INT, VarType.FLOAT)

    def is_compatible(self, declared, actual):
        if declared == actual: 
            return True
        if declared == VarType.FLOAT and actual == VarType.INT: 
            return True
        return False
    
    def visitIfStmt(self, ctx):
        condition_type = self.visit(ctx.expr())
        if condition_type != VarType.BOOL:
            self.errors.append(f"Error: Condition in 'if' must be bool, got '{condition_type.value if condition_type else 'None'}'.")

        self.visit(ctx.statement(0))
        if ctx.statement(1) is not None:
            self.visit(ctx.statement(1))
        return None

    def visitWhileStmt(self, ctx):
        condition_type = self.visit(ctx.expr())
        if condition_type != VarType.BOOL:
            self.errors.append(f"Error: Condition in 'while' must be bool, got '{condition_type.value if condition_type else 'None'}'.")

        self.visit(ctx.statement())
        return None
    
    def visitRelationalExpr(self, ctx):
        left_type = self.visit(ctx.additiveExpr(0))
        for i in range(1, len(ctx.additiveExpr())):
            op = ctx.getChild(2*i - 1).getText()
            right_type = self.visit(ctx.additiveExpr(i))

            if not self.is_numeric(left_type) or not self.is_numeric(right_type):
                self.errors.append(f"Error: Operator '{op}' requires numeric operands, got '{left_type.value if left_type else 'None'}' and '{right_type.value if right_type else 'None'}'.")
            left_type = VarType.BOOL
        return left_type