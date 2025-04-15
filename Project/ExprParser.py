# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,191,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,61,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,5,4,72,8,4,10,4,12,4,75,9,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,8,1,8,1,8,5,8,91,8,8,10,8,12,8,94,9,8,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,103,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,
        11,5,11,113,8,11,10,11,12,11,116,9,11,1,11,1,11,1,12,1,12,1,12,1,
        12,3,12,124,8,12,1,13,1,13,1,13,5,13,129,8,13,10,13,12,13,132,9,
        13,1,14,1,14,1,14,5,14,137,8,14,10,14,12,14,140,9,14,1,15,1,15,1,
        15,5,15,145,8,15,10,15,12,15,148,9,15,1,16,1,16,1,16,5,16,153,8,
        16,10,16,12,16,156,9,16,1,17,1,17,1,17,5,17,161,8,17,10,17,12,17,
        164,9,17,1,18,1,18,1,18,5,18,169,8,18,10,18,12,18,172,9,18,1,19,
        1,19,1,19,1,19,1,19,3,19,179,8,19,1,20,1,20,1,20,1,20,1,20,1,20,
        3,20,187,8,20,1,21,1,21,1,21,0,0,22,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,0,6,1,0,2,5,1,0,19,20,1,0,21,22,
        1,0,23,25,1,0,26,28,1,0,30,33,191,0,47,1,0,0,0,2,60,1,0,0,0,4,62,
        1,0,0,0,6,64,1,0,0,0,8,68,1,0,0,0,10,76,1,0,0,0,12,80,1,0,0,0,14,
        84,1,0,0,0,16,87,1,0,0,0,18,95,1,0,0,0,20,104,1,0,0,0,22,110,1,0,
        0,0,24,123,1,0,0,0,26,125,1,0,0,0,28,133,1,0,0,0,30,141,1,0,0,0,
        32,149,1,0,0,0,34,157,1,0,0,0,36,165,1,0,0,0,38,178,1,0,0,0,40,186,
        1,0,0,0,42,188,1,0,0,0,44,46,3,2,1,0,45,44,1,0,0,0,46,49,1,0,0,0,
        47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,51,5,
        0,0,1,51,1,1,0,0,0,52,61,3,6,3,0,53,61,3,10,5,0,54,61,3,12,6,0,55,
        61,3,18,9,0,56,61,3,20,10,0,57,61,3,22,11,0,58,61,3,14,7,0,59,61,
        5,1,0,0,60,52,1,0,0,0,60,53,1,0,0,0,60,54,1,0,0,0,60,55,1,0,0,0,
        60,56,1,0,0,0,60,57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,0,0,61,3,1,0,
        0,0,62,63,7,0,0,0,63,5,1,0,0,0,64,65,3,4,2,0,65,66,3,8,4,0,66,67,
        5,1,0,0,67,7,1,0,0,0,68,73,5,34,0,0,69,70,5,6,0,0,70,72,5,34,0,0,
        71,69,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,9,1,0,
        0,0,75,73,1,0,0,0,76,77,5,7,0,0,77,78,3,8,4,0,78,79,5,1,0,0,79,11,
        1,0,0,0,80,81,5,8,0,0,81,82,3,16,8,0,82,83,5,1,0,0,83,13,1,0,0,0,
        84,85,3,24,12,0,85,86,5,1,0,0,86,15,1,0,0,0,87,92,3,24,12,0,88,89,
        5,6,0,0,89,91,3,24,12,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,
        0,92,93,1,0,0,0,93,17,1,0,0,0,94,92,1,0,0,0,95,96,5,9,0,0,96,97,
        5,10,0,0,97,98,3,24,12,0,98,99,5,11,0,0,99,102,3,2,1,0,100,101,5,
        12,0,0,101,103,3,2,1,0,102,100,1,0,0,0,102,103,1,0,0,0,103,19,1,
        0,0,0,104,105,5,13,0,0,105,106,5,10,0,0,106,107,3,24,12,0,107,108,
        5,11,0,0,108,109,3,2,1,0,109,21,1,0,0,0,110,114,5,14,0,0,111,113,
        3,2,1,0,112,111,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,
        1,0,0,0,115,117,1,0,0,0,116,114,1,0,0,0,117,118,5,15,0,0,118,23,
        1,0,0,0,119,120,5,34,0,0,120,121,5,16,0,0,121,124,3,24,12,0,122,
        124,3,26,13,0,123,119,1,0,0,0,123,122,1,0,0,0,124,25,1,0,0,0,125,
        130,3,28,14,0,126,127,5,17,0,0,127,129,3,28,14,0,128,126,1,0,0,0,
        129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,27,1,0,0,0,132,
        130,1,0,0,0,133,138,3,30,15,0,134,135,5,18,0,0,135,137,3,30,15,0,
        136,134,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,
        139,29,1,0,0,0,140,138,1,0,0,0,141,146,3,32,16,0,142,143,7,1,0,0,
        143,145,3,32,16,0,144,142,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,
        0,146,147,1,0,0,0,147,31,1,0,0,0,148,146,1,0,0,0,149,154,3,34,17,
        0,150,151,7,2,0,0,151,153,3,34,17,0,152,150,1,0,0,0,153,156,1,0,
        0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,33,1,0,0,0,156,154,1,0,0,
        0,157,162,3,36,18,0,158,159,7,3,0,0,159,161,3,36,18,0,160,158,1,
        0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,35,1,0,
        0,0,164,162,1,0,0,0,165,170,3,38,19,0,166,167,7,4,0,0,167,169,3,
        38,19,0,168,166,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,
        1,0,0,0,171,37,1,0,0,0,172,170,1,0,0,0,173,174,5,24,0,0,174,179,
        3,38,19,0,175,176,5,29,0,0,176,179,3,38,19,0,177,179,3,40,20,0,178,
        173,1,0,0,0,178,175,1,0,0,0,178,177,1,0,0,0,179,39,1,0,0,0,180,181,
        5,10,0,0,181,182,3,24,12,0,182,183,5,11,0,0,183,187,1,0,0,0,184,
        187,3,42,21,0,185,187,5,34,0,0,186,180,1,0,0,0,186,184,1,0,0,0,186,
        185,1,0,0,0,187,41,1,0,0,0,188,189,7,5,0,0,189,43,1,0,0,0,15,47,
        60,73,92,102,114,123,130,138,146,154,162,170,178,186
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'int'", "'float'", "'bool'", "'string'", 
                     "','", "'read'", "'write'", "'if'", "'('", "')'", "'else'", 
                     "'while'", "'{'", "'}'", "'='", "'||'", "'&&'", "'=='", 
                     "'!='", "'<'", "'>'", "'+'", "'-'", "'.'", "'*'", "'/'", 
                     "'%'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IntegerLiteral", "FloatLiteral", 
                      "BooleanLiteral", "StringLiteral", "Identifier", "WS", 
                      "LINE_COMMENT" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_type = 2
    RULE_declStmt = 3
    RULE_idList = 4
    RULE_readStmt = 5
    RULE_writeStmt = 6
    RULE_exprStmt = 7
    RULE_exprList = 8
    RULE_ifStmt = 9
    RULE_whileStmt = 10
    RULE_blockStmt = 11
    RULE_expr = 12
    RULE_logicalOrExpr = 13
    RULE_logicalAndExpr = 14
    RULE_equalityExpr = 15
    RULE_relationalExpr = 16
    RULE_additiveExpr = 17
    RULE_multiplicativeExpr = 18
    RULE_unaryExpr = 19
    RULE_primaryExpr = 20
    RULE_literal = 21

    ruleNames =  [ "prog", "statement", "type", "declStmt", "idList", "readStmt", 
                   "writeStmt", "exprStmt", "exprList", "ifStmt", "whileStmt", 
                   "blockStmt", "expr", "logicalOrExpr", "logicalAndExpr", 
                   "equalityExpr", "relationalExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "primaryExpr", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    IntegerLiteral=30
    FloatLiteral=31
    BooleanLiteral=32
    StringLiteral=33
    Identifier=34
    WS=35
    LINE_COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33839671230) != 0):
                self.state = 44
                self.statement()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStmt(self):
            return self.getTypedRuleContext(ExprParser.IfStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)


    class ReadStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def readStmt(self):
            return self.getTypedRuleContext(ExprParser.ReadStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStatement" ):
                listener.enterReadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStatement" ):
                listener.exitReadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStatement" ):
                return visitor.visitReadStatement(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exprStmt(self):
            return self.getTypedRuleContext(ExprParser.ExprStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStatement" ):
                return visitor.visitEmptyStatement(self)
            else:
                return visitor.visitChildren(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def writeStmt(self):
            return self.getTypedRuleContext(ExprParser.WriteStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStatement" ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStatement" ):
                listener.exitWriteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStatement" ):
                return visitor.visitWriteStatement(self)
            else:
                return visitor.visitChildren(self)


    class BlockStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def blockStmt(self):
            return self.getTypedRuleContext(ExprParser.BlockStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whileStmt(self):
            return self.getTypedRuleContext(ExprParser.WhileStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def declStmt(self):
            return self.getTypedRuleContext(ExprParser.DeclStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatement" ):
                listener.enterDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatement" ):
                listener.exitDeclarationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationStatement" ):
                return visitor.visitDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5]:
                localctx = ExprParser.DeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.declStmt()
                pass
            elif token in [7]:
                localctx = ExprParser.ReadStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.readStmt()
                pass
            elif token in [8]:
                localctx = ExprParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.writeStmt()
                pass
            elif token in [9]:
                localctx = ExprParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.ifStmt()
                pass
            elif token in [13]:
                localctx = ExprParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.whileStmt()
                pass
            elif token in [14]:
                localctx = ExprParser.BlockStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.blockStmt()
                pass
            elif token in [10, 24, 29, 30, 31, 32, 33, 34]:
                localctx = ExprParser.ExpressionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 58
                self.exprStmt()
                pass
            elif token in [1]:
                localctx = ExprParser.EmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 59
                self.match(ExprParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ExprParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)


        def idList(self):
            return self.getTypedRuleContext(ExprParser.IdListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_declStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclStmt" ):
                listener.enterDeclStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclStmt" ):
                listener.exitDeclStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclStmt" ):
                return visitor.visitDeclStmt(self)
            else:
                return visitor.visitChildren(self)




    def declStmt(self):

        localctx = ExprParser.DeclStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.type_()
            self.state = 65
            self.idList()
            self.state = 66
            self.match(ExprParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.Identifier)
            else:
                return self.getToken(ExprParser.Identifier, i)

        def getRuleIndex(self):
            return ExprParser.RULE_idList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdList" ):
                listener.enterIdList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdList" ):
                listener.exitIdList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = ExprParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ExprParser.Identifier)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 69
                self.match(ExprParser.T__5)
                self.state = 70
                self.match(ExprParser.Identifier)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(ExprParser.IdListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_readStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)




    def readStmt(self):

        localctx = ExprParser.ReadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_readStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(ExprParser.T__6)
            self.state = 77
            self.idList()
            self.state = 78
            self.match(ExprParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprList(self):
            return self.getTypedRuleContext(ExprParser.ExprListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_writeStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStmt" ):
                listener.enterWriteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStmt" ):
                listener.exitWriteStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)




    def writeStmt(self):

        localctx = ExprParser.WriteStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_writeStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ExprParser.T__7)
            self.state = 81
            self.exprList()
            self.state = 82
            self.match(ExprParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_exprStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)




    def exprStmt(self):

        localctx = ExprParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.expr()
            self.state = 85
            self.match(ExprParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = ExprParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.expr()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 88
                self.match(ExprParser.T__5)
                self.state = 89
                self.expr()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = ExprParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(ExprParser.T__8)
            self.state = 96
            self.match(ExprParser.T__9)
            self.state = 97
            self.expr()
            self.state = 98
            self.match(ExprParser.T__10)
            self.state = 99
            self.statement()
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 100
                self.match(ExprParser.T__11)
                self.state = 101
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = ExprParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(ExprParser.T__12)
            self.state = 105
            self.match(ExprParser.T__9)
            self.state = 106
            self.expr()
            self.state = 107
            self.match(ExprParser.T__10)
            self.state = 108
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_blockStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStmt" ):
                listener.enterBlockStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStmt" ):
                listener.exitBlockStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def blockStmt(self):

        localctx = ExprParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ExprParser.T__13)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33839671230) != 0):
                self.state = 111
                self.statement()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self.match(ExprParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicalOrExpr(self):
            return self.getTypedRuleContext(ExprParser.LogicalOrExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ExprParser.Identifier, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = ExprParser.AssignExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(ExprParser.Identifier)
                self.state = 120
                self.match(ExprParser.T__15)
                self.state = 121
                self.expr()
                pass

            elif la_ == 2:
                localctx = ExprParser.OrExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.logicalOrExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LogicalAndExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.LogicalAndExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_logicalOrExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpr" ):
                listener.enterLogicalOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpr" ):
                listener.exitLogicalOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpr" ):
                return visitor.visitLogicalOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpr(self):

        localctx = ExprParser.LogicalOrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logicalOrExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.logicalAndExpr()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 126
                self.match(ExprParser.T__16)
                self.state = 127
                self.logicalAndExpr()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.EqualityExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.EqualityExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_logicalAndExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpr" ):
                listener.enterLogicalAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpr" ):
                listener.exitLogicalAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpr" ):
                return visitor.visitLogicalAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpr(self):

        localctx = ExprParser.LogicalAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_logicalAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.equalityExpr()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 134
                self.match(ExprParser.T__17)
                self.state = 135
                self.equalityExpr()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.RelationalExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.RelationalExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_equalityExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpr(self):

        localctx = ExprParser.EqualityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_equalityExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.relationalExpr()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 142
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 143
                self.relationalExpr()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.AdditiveExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_relationalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpr(self):

        localctx = ExprParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.additiveExpr()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 150
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 151
                self.additiveExpr()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.MultiplicativeExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpr(self):

        localctx = ExprParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.multiplicativeExpr()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0):
                self.state = 158
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 159
                self.multiplicativeExpr()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.UnaryExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_multiplicativeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpr(self):

        localctx = ExprParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.unaryExpr()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0):
                self.state = 166
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 167
                self.unaryExpr()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(ExprParser.UnaryExprContext,0)


        def primaryExpr(self):
            return self.getTypedRuleContext(ExprParser.PrimaryExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = ExprParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unaryExpr)
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(ExprParser.T__23)
                self.state = 174
                self.unaryExpr()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(ExprParser.T__28)
                self.state = 176
                self.unaryExpr()
                pass
            elif token in [10, 30, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.primaryExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def literal(self):
            return self.getTypedRuleContext(ExprParser.LiteralContext,0)


        def Identifier(self):
            return self.getToken(ExprParser.Identifier, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_primaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = ExprParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_primaryExpr)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(ExprParser.T__9)
                self.state = 181
                self.expr()
                self.state = 182
                self.match(ExprParser.T__10)
                pass
            elif token in [30, 31, 32, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.literal()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.match(ExprParser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(ExprParser.IntegerLiteral, 0)

        def FloatLiteral(self):
            return self.getToken(ExprParser.FloatLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(ExprParser.BooleanLiteral, 0)

        def StringLiteral(self):
            return self.getToken(ExprParser.StringLiteral, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ExprParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





