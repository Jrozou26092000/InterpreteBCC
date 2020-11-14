import sys
import os
from antlr4 import *
from gen.BCCLexer import BCCLexer
from gen.BCCParser import BCCParser
from MyVisitor import MyVisitor


def main(argv):
    input_stream = FileStream(argv[1], 'utf-8')
    lexer = BCCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BCCParser(stream)
    tree = parser.prog()
    dirname = os.path.dirname(__file__)
    file = open(dirname+"/Resultado.ArnoldC", "wt")
    visitor = MyVisitor(file)
    visitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
