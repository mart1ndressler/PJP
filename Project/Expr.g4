grammar Expr;
prog: statement* EOF;

statement: declStmt      #DeclarationStatement
         | readStmt      #ReadStatement
         | writeStmt     #WriteStatement
         | ifStmt        #IfStatement
         | whileStmt     #WhileStatement
         | blockStmt     #BlockStatement
         | exprStmt      #ExpressionStatement
         | ';'           #EmptyStatement
         ;

type: 'int' | 'float' | 'bool' | 'string';
declStmt: type idList ';';
idList: Identifier (',' Identifier)* ;

readStmt: 'read' idList ';';
writeStmt: 'write' exprList ';';
exprStmt: expr ';';
exprList: expr (',' expr)* ;

ifStmt: 'if' '(' expr ')' statement ('else' statement)?;
whileStmt: 'while' '(' expr ')' statement;
blockStmt: '{' statement* '}';

expr: Identifier '=' expr    #AssignExpr
    | logicalOrExpr          #OrExpr
    ;

logicalOrExpr: logicalAndExpr ( '||' logicalAndExpr )*;
logicalAndExpr: equalityExpr ( '&&' equalityExpr )*;
equalityExpr: relationalExpr ( ( '==' | '!=' ) relationalExpr )*;
relationalExpr: additiveExpr ( ( '<' | '>' ) additiveExpr )*;
additiveExpr: multiplicativeExpr ( ( '+' | '-' | '.' ) multiplicativeExpr )*;
multiplicativeExpr: unaryExpr ( ( '*' | '/' | '%' ) unaryExpr )*;
unaryExpr: '-' unaryExpr | '!' unaryExpr | primaryExpr;
primaryExpr: '(' expr ')' | literal | Identifier;

literal: IntegerLiteral
       | FloatLiteral
       | BooleanLiteral
       | StringLiteral;

IntegerLiteral: [0-9]+ ;
FloatLiteral: [0-9]+ '.' [0-9]+ ;
BooleanLiteral: 'true' | 'false' ;
StringLiteral: '"' ( ~["\\] | '\\' . )* '"' ;
Identifier: [a-zA-Z] [a-zA-Z0-9]* ;
WS: [ \t\r\n]+ -> skip ;
LINE_COMMENT: '//' ~[\r\n]* -> skip ;