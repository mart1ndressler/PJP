import sys
from antlr4 import FileStream, CommonTokenStream
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprListener import MyErrorListener
from MyExprVisitor import MyExprVisitor

def main():
    input_file = sys.argv[1]
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)

    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.prog()
    if error_listener.errors:
        for err in error_listener.errors:
            print(err)
        print("Syntax errors found. Stopping computation.")
        sys.exit(1)

    type_checker = MyExprVisitor()
    type_checker.visit(tree)
    if type_checker.errors:
        for err in type_checker.errors:
            print(err)
        print("Type errors found. Stopping computation.")
        sys.exit(1)
    print("Syntactic and type checking succeeded.")

if __name__ == '__main__':
    main()