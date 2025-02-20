from lexer import Lexer
from parser import Parser

if __name__ == "__main__":
    # code = "int x = 10 + 3 * 5; float y = 5; if (x > 5) { print(x); } else { print(x); }"
    # code = "while (y > 0) { print(x); x = x - 1; }"
    # code = "int x = 5; while (x > 0) { print(x); x = x - 1; }"
    code = input()

    # Análise léxica
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    print("Análise Léxica:", tokens)

    # Análise sintática
    parser = Parser(tokens)
    try:
        parser.parse()
        print("Análise Sintática concluída com sucesso!")
    except SyntaxError as e:
        print(f"{e}")
