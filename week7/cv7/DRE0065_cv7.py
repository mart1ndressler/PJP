from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):
    def visitMulDiv(self, ctx):
        left, right = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if ctx.op.text == '*': return left * right
        else:
            if right == 0: raise ZeroDivisionError("Division by zero")
            return left // right

    def visitAddSub(self, ctx):
        left, right = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        if ctx.op.text == '+': return left + right
        else: return left - right

    def visitParens(self, ctx): return self.visit(ctx.expr())
    def visitNumber(self, ctx):
        txt = ctx.getText()
        if txt.startswith("0x") or txt.startswith("0X"): return int(txt, 16)
        elif txt.startswith("0") and len(txt) > 1: return int(txt, 8)
        return int(txt)

def main():
    lines = []
    while True:
        line = input()
        if line.strip() == "": break
        lines.append(line)
    
    data = "\n".join(lines).strip()
    if not data: return

    lexer = ExprLexer(InputStream(data))
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)

    try: tree = parser.prog()
    except Exception: return

    visitor = EvalVisitor()
    for stat in tree.stat():
        try:
            val = visitor.visit(stat.expr())
            print(val)
        except Exception: return

if __name__ == '__main__': main()