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


    # Enter a parse tree produced by ExprParser#DeclarationStatement.
    def enterDeclarationStatement(self, ctx:ExprParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#DeclarationStatement.
    def exitDeclarationStatement(self, ctx:ExprParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#ReadStatement.
    def enterReadStatement(self, ctx:ExprParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#ReadStatement.
    def exitReadStatement(self, ctx:ExprParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#WriteStatement.
    def enterWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#WriteStatement.
    def exitWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#IfStatement.
    def enterIfStatement(self, ctx:ExprParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#IfStatement.
    def exitIfStatement(self, ctx:ExprParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#WhileStatement.
    def enterWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#WhileStatement.
    def exitWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#BlockStatement.
    def enterBlockStatement(self, ctx:ExprParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#BlockStatement.
    def exitBlockStatement(self, ctx:ExprParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#ExpressionStatement.
    def enterExpressionStatement(self, ctx:ExprParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#ExpressionStatement.
    def exitExpressionStatement(self, ctx:ExprParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#EmptyStatement.
    def enterEmptyStatement(self, ctx:ExprParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#EmptyStatement.
    def exitEmptyStatement(self, ctx:ExprParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#type.
    def enterType(self, ctx:ExprParser.TypeContext):
        pass

    # Exit a parse tree produced by ExprParser#type.
    def exitType(self, ctx:ExprParser.TypeContext):
        pass


    # Enter a parse tree produced by ExprParser#declStmt.
    def enterDeclStmt(self, ctx:ExprParser.DeclStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#declStmt.
    def exitDeclStmt(self, ctx:ExprParser.DeclStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#idList.
    def enterIdList(self, ctx:ExprParser.IdListContext):
        pass

    # Exit a parse tree produced by ExprParser#idList.
    def exitIdList(self, ctx:ExprParser.IdListContext):
        pass


    # Enter a parse tree produced by ExprParser#readStmt.
    def enterReadStmt(self, ctx:ExprParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#readStmt.
    def exitReadStmt(self, ctx:ExprParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#writeStmt.
    def enterWriteStmt(self, ctx:ExprParser.WriteStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#writeStmt.
    def exitWriteStmt(self, ctx:ExprParser.WriteStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#exprStmt.
    def enterExprStmt(self, ctx:ExprParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#exprStmt.
    def exitExprStmt(self, ctx:ExprParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#exprList.
    def enterExprList(self, ctx:ExprParser.ExprListContext):
        pass

    # Exit a parse tree produced by ExprParser#exprList.
    def exitExprList(self, ctx:ExprParser.ExprListContext):
        pass


    # Enter a parse tree produced by ExprParser#ifStmt.
    def enterIfStmt(self, ctx:ExprParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#ifStmt.
    def exitIfStmt(self, ctx:ExprParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#whileStmt.
    def enterWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#whileStmt.
    def exitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#blockStmt.
    def enterBlockStmt(self, ctx:ExprParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#blockStmt.
    def exitBlockStmt(self, ctx:ExprParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#AssignExpr.
    def enterAssignExpr(self, ctx:ExprParser.AssignExprContext):
        pass

    # Exit a parse tree produced by ExprParser#AssignExpr.
    def exitAssignExpr(self, ctx:ExprParser.AssignExprContext):
        pass


    # Enter a parse tree produced by ExprParser#OrExpr.
    def enterOrExpr(self, ctx:ExprParser.OrExprContext):
        pass

    # Exit a parse tree produced by ExprParser#OrExpr.
    def exitOrExpr(self, ctx:ExprParser.OrExprContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalOrExpr.
    def enterLogicalOrExpr(self, ctx:ExprParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalOrExpr.
    def exitLogicalOrExpr(self, ctx:ExprParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalAndExpr.
    def enterLogicalAndExpr(self, ctx:ExprParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalAndExpr.
    def exitLogicalAndExpr(self, ctx:ExprParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by ExprParser#equalityExpr.
    def enterEqualityExpr(self, ctx:ExprParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by ExprParser#equalityExpr.
    def exitEqualityExpr(self, ctx:ExprParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by ExprParser#relationalExpr.
    def enterRelationalExpr(self, ctx:ExprParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by ExprParser#relationalExpr.
    def exitRelationalExpr(self, ctx:ExprParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by ExprParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:ExprParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by ExprParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:ExprParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by ExprParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:ExprParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by ExprParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:ExprParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by ExprParser#unaryExpr.
    def enterUnaryExpr(self, ctx:ExprParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by ExprParser#unaryExpr.
    def exitUnaryExpr(self, ctx:ExprParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by ExprParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:ExprParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by ExprParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:ExprParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by ExprParser#literal.
    def enterLiteral(self, ctx:ExprParser.LiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#literal.
    def exitLiteral(self, ctx:ExprParser.LiteralContext):
        pass



del ExprParser