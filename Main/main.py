# Cristian Santiago Vargas Ortiz
# Juan Esteban Rozo Urbina
# Juan Camilo Acosta Rojas
import sys
from antlr4 import *
from gen.BCCLexer import BCCLexer
from gen.BCCParser import BCCParser
from MyVisitor import MyVisitor


def main(argv):
    # directory = os.path.dirname(__file__)
    # file = open(directory+"/input.txt", "wt")
    # file.writelines(sys.stdin.readlines())
    # file.close()
    # input_stream = FileStream(directory+"/input.txt", 'utf-8')
    input_stream = InputStream("".join(sys.stdin.readlines()))
    lexer = BCCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BCCParser(stream)
    tree = parser.prog()
    visitor = MyVisitor()
    visitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
