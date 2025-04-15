# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#DeclarationStatement.
    def visitDeclarationStatement(self, ctx:ExprParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ReadStatement.
    def visitReadStatement(self, ctx:ExprParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#WriteStatement.
    def visitWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#IfStatement.
    def visitIfStatement(self, ctx:ExprParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#WhileStatement.
    def visitWhileStatement(self, ctx:ExprParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#BlockStatement.
    def visitBlockStatement(self, ctx:ExprParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ExpressionStatement.
    def visitExpressionStatement(self, ctx:ExprParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#EmptyStatement.
    def visitEmptyStatement(self, ctx:ExprParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type.
    def visitType(self, ctx:ExprParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declStmt.
    def visitDeclStmt(self, ctx:ExprParser.DeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#idList.
    def visitIdList(self, ctx:ExprParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#readStmt.
    def visitReadStmt(self, ctx:ExprParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#writeStmt.
    def visitWriteStmt(self, ctx:ExprParser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#exprStmt.
    def visitExprStmt(self, ctx:ExprParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#exprList.
    def visitExprList(self, ctx:ExprParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifStmt.
    def visitIfStmt(self, ctx:ExprParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#whileStmt.
    def visitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#blockStmt.
    def visitBlockStmt(self, ctx:ExprParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#AssignExpr.
    def visitAssignExpr(self, ctx:ExprParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#OrExpr.
    def visitOrExpr(self, ctx:ExprParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalOrExpr.
    def visitLogicalOrExpr(self, ctx:ExprParser.LogicalOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalAndExpr.
    def visitLogicalAndExpr(self, ctx:ExprParser.LogicalAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#equalityExpr.
    def visitEqualityExpr(self, ctx:ExprParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#relationalExpr.
    def visitRelationalExpr(self, ctx:ExprParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:ExprParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:ExprParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unaryExpr.
    def visitUnaryExpr(self, ctx:ExprParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:ExprParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#literal.
    def visitLiteral(self, ctx:ExprParser.LiteralContext):
        return self.visitChildren(ctx)



del ExprParser