# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#stat.
    def enterStat(self, ctx:ExprParser.StatContext):
        pass

    # Exit a parse tree produced by ExprParser#stat.
    def exitStat(self, ctx:ExprParser.StatContext):
        pass


    # Enter a parse tree produced by ExprParser#decl.
    def enterDecl(self, ctx:ExprParser.DeclContext):
        pass

    # Exit a parse tree produced by ExprParser#decl.
    def exitDecl(self, ctx:ExprParser.DeclContext):
        pass


    # Enter a parse tree produced by ExprParser#type.
    def enterType(self, ctx:ExprParser.TypeContext):
        pass

    # Exit a parse tree produced by ExprParser#type.
    def exitType(self, ctx:ExprParser.TypeContext):
        pass


    # Enter a parse tree produced by ExprParser#idList.
    def enterIdList(self, ctx:ExprParser.IdListContext):
        pass

    # Exit a parse tree produced by ExprParser#idList.
    def exitIdList(self, ctx:ExprParser.IdListContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#Assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#Assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#ToMult.
    def enterToMult(self, ctx:ExprParser.ToMultContext):
        pass

    # Exit a parse tree produced by ExprParser#ToMult.
    def exitToMult(self, ctx:ExprParser.ToMultContext):
        pass


    # Enter a parse tree produced by ExprParser#AddSub.
    def enterAddSub(self, ctx:ExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExprParser#AddSub.
    def exitAddSub(self, ctx:ExprParser.AddSubContext):
        pass


    # Enter a parse tree produced by ExprParser#MulDivMod.
    def enterMulDivMod(self, ctx:ExprParser.MulDivModContext):
        pass

    # Exit a parse tree produced by ExprParser#MulDivMod.
    def exitMulDivMod(self, ctx:ExprParser.MulDivModContext):
        pass


    # Enter a parse tree produced by ExprParser#ToAtom.
    def enterToAtom(self, ctx:ExprParser.ToAtomContext):
        pass

    # Exit a parse tree produced by ExprParser#ToAtom.
    def exitToAtom(self, ctx:ExprParser.ToAtomContext):
        pass


    # Enter a parse tree produced by ExprParser#Parens.
    def enterParens(self, ctx:ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#Parens.
    def exitParens(self, ctx:ExprParser.ParensContext):
        pass


    # Enter a parse tree produced by ExprParser#Variable.
    def enterVariable(self, ctx:ExprParser.VariableContext):
        pass

    # Exit a parse tree produced by ExprParser#Variable.
    def exitVariable(self, ctx:ExprParser.VariableContext):
        pass


    # Enter a parse tree produced by ExprParser#Float.
    def enterFloat(self, ctx:ExprParser.FloatContext):
        pass

    # Exit a parse tree produced by ExprParser#Float.
    def exitFloat(self, ctx:ExprParser.FloatContext):
        pass


    # Enter a parse tree produced by ExprParser#Number.
    def enterNumber(self, ctx:ExprParser.NumberContext):
        pass

    # Exit a parse tree produced by ExprParser#Number.
    def exitNumber(self, ctx:ExprParser.NumberContext):
        pass



del ExprParser