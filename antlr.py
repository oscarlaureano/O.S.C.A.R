import sys
from antlr4 import *
from oscarLexer import oscarLexer
from oscarParser import oscarParser
from myListener import MyListener 

def main(argv):
  inp = FileStream(argv[1])
  lexer = oscarLexer(inp)
  stream = CommonTokenStream(lexer)
  parser = oscarParser(stream)
  tree = parser.programa()
# print(tree.toStringTree(recog=parser))

  output = open("output.oscar","w")

  listener = MyListener(output)

  walker = ParseTreeWalker()
  walker.walk(listener, tree)

  output.close()

if __name__ == '__main__':
  main(sys.argv)