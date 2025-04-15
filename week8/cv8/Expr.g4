grammar Expr;

prog: stat+;
stat: decl | expr ';';
decl: type idList ';';
type: 'int' | 'float';
idList: ID (',' ID)*;
expr: assignExpr;

assignExpr
    : addExpr ( '=' assignExpr )?     #Assignment
    ;

addExpr
    : addExpr op=('+'|'-') multExpr   #AddSub
    | multExpr                        #ToMult
    ;

multExpr
    : multExpr op=('*'|'/'|'%') atom  #MulDivMod
    | atom                            #ToAtom
    ;

atom
    : '(' expr ')'  #Parens
    | ID            #Variable
    | FLOAT         #Float
    | NUMBER        #Number
    ;

NUMBER: '0x' [0-9a-fA-F]+ 
    | '0' [0-7]+
    | [1-9][0-9]*
    | '0'
    ;

FLOAT: [0-9]+ '.' [0-9]+;
ID: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;