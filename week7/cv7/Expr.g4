grammar Expr;

prog: stat+;
stat: expr ';';
expr
    : expr op=('*'|'/') expr     #MulDiv
    | expr op=('+'|'-') expr     #AddSub
    | '(' expr ')'               #Parens
    | NUMBER                     #Number
    ;
NUMBER
    : '0x' [0-9a-fA-F]+ 
    | '0' [0-7]+
    | [1-9][0-9]*
    | '0'
    ;
WS: [ \t\r\n]+ -> skip;