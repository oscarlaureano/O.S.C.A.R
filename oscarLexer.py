# Generated from oscar.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


import rules


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"B\u0291\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b")
        buf.write(u"\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write(u"\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write(u"\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3")
        buf.write(u"\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25")
        buf.write(u"\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3")
        buf.write(u"\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3")
        buf.write(u"\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3!")
        buf.write(u"\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write(u"#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&")
        buf.write(u"\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3")
        buf.write(u".\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write(u"\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3")
        buf.write(u"\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write(u"\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3")
        buf.write(u"\65\3\65\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5")
        buf.write(u"\67\u023d\n\67\38\38\38\38\38\38\38\38\38\58\u0248\n")
        buf.write(u"8\39\39\39\39\59\u024e\n9\3:\3:\3;\3;\3;\3;\3<\3<\7<")
        buf.write(u"\u0258\n<\f<\16<\u025b\13<\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write(u"=\3=\3=\5=\u0268\n=\3>\6>\u026b\n>\r>\16>\u026c\3?\6")
        buf.write(u"?\u0270\n?\r?\16?\u0271\3?\3?\7?\u0276\n?\f?\16?\u0279")
        buf.write(u"\13?\3@\3@\3@\7@\u027e\n@\f@\16@\u0281\13@\3@\3@\3A\3")
        buf.write(u"A\3A\3A\3A\3A\7A\u028b\nA\fA\16A\u028e\13A\3A\3A\2\2")
        buf.write(u"B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write(u"\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write(u"/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K")
        buf.write(u"\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8")
        buf.write(u"o9q:s;u<w=y>{?}@\177A\u0081B\3\2\7\4\2>>@@\7\2*+]]__")
        buf.write(u"}}\177\177\5\2\13\f\17\17\"\"\4\2C\\c|\5\2\62;C\\c|\2")
        buf.write(u"\u02c4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write(u"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write(u"\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write(u"\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write(u"#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write(u"\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write(u"\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write(u"\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write(u"\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write(u"Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write(u"\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write(u"\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write(u"\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write(u"\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write(u"\2\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u008a\3\2\2\2\7\u008c")
        buf.write(u"\3\2\2\2\t\u0090\3\2\2\2\13\u0095\3\2\2\2\r\u009a\3\2")
        buf.write(u"\2\2\17\u009c\3\2\2\2\21\u009e\3\2\2\2\23\u00a0\3\2\2")
        buf.write(u"\2\25\u00a2\3\2\2\2\27\u00a9\3\2\2\2\31\u00ab\3\2\2\2")
        buf.write(u"\33\u00af\3\2\2\2\35\u00b1\3\2\2\2\37\u00b3\3\2\2\2!")
        buf.write(u"\u00b6\3\2\2\2#\u00bb\3\2\2\2%\u00c1\3\2\2\2\'\u00c6")
        buf.write(u"\3\2\2\2)\u00c8\3\2\2\2+\u00ca\3\2\2\2-\u00cc\3\2\2\2")
        buf.write(u"/\u00ce\3\2\2\2\61\u00d0\3\2\2\2\63\u00d4\3\2\2\2\65")
        buf.write(u"\u00da\3\2\2\2\67\u00e1\3\2\2\29\u00e6\3\2\2\2;\u00eb")
        buf.write(u"\3\2\2\2=\u00ef\3\2\2\2?\u00f1\3\2\2\2A\u00f3\3\2\2\2")
        buf.write(u"C\u00f9\3\2\2\2E\u00fe\3\2\2\2G\u0107\3\2\2\2I\u010e")
        buf.write(u"\3\2\2\2K\u0114\3\2\2\2M\u0119\3\2\2\2O\u011e\3\2\2\2")
        buf.write(u"Q\u0124\3\2\2\2S\u012e\3\2\2\2U\u0133\3\2\2\2W\u013a")
        buf.write(u"\3\2\2\2Y\u0141\3\2\2\2[\u0145\3\2\2\2]\u0149\3\2\2\2")
        buf.write(u"_\u0150\3\2\2\2a\u0155\3\2\2\2c\u015c\3\2\2\2e\u0166")
        buf.write(u"\3\2\2\2g\u0170\3\2\2\2i\u017a\3\2\2\2k\u0181\3\2\2\2")
        buf.write(u"m\u023c\3\2\2\2o\u0247\3\2\2\2q\u024d\3\2\2\2s\u024f")
        buf.write(u"\3\2\2\2u\u0251\3\2\2\2w\u0255\3\2\2\2y\u0267\3\2\2\2")
        buf.write(u"{\u026a\3\2\2\2}\u026f\3\2\2\2\177\u027a\3\2\2\2\u0081")
        buf.write(u"\u0284\3\2\2\2\u0083\u0084\7%\2\2\u0084\u0085\7q\2\2")
        buf.write(u"\u0085\u0086\7u\2\2\u0086\u0087\7e\2\2\u0087\u0088\7")
        buf.write(u"c\2\2\u0088\u0089\7t\2\2\u0089\4\3\2\2\2\u008a\u008b")
        buf.write(u"\7=\2\2\u008b\6\3\2\2\2\u008c\u008d\7f\2\2\u008d\u008e")
        buf.write(u"\7g\2\2\u008e\u008f\7h\2\2\u008f\b\3\2\2\2\u0090\u0091")
        buf.write(u"\7x\2\2\u0091\u0092\7q\2\2\u0092\u0093\7k\2\2\u0093\u0094")
        buf.write(u"\7f\2\2\u0094\n\3\2\2\2\u0095\u0096\7o\2\2\u0096\u0097")
        buf.write(u"\7c\2\2\u0097\u0098\7k\2\2\u0098\u0099\7p\2\2\u0099\f")
        buf.write(u"\3\2\2\2\u009a\u009b\7*\2\2\u009b\16\3\2\2\2\u009c\u009d")
        buf.write(u"\7.\2\2\u009d\20\3\2\2\2\u009e\u009f\7+\2\2\u009f\22")
        buf.write(u"\3\2\2\2\u00a0\u00a1\7}\2\2\u00a1\24\3\2\2\2\u00a2\u00a3")
        buf.write(u"\7t\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6")
        buf.write(u"\7w\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7p\2\2\u00a8\26")
        buf.write(u"\3\2\2\2\u00a9\u00aa\7\177\2\2\u00aa\30\3\2\2\2\u00ab")
        buf.write(u"\u00ac\7x\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7t\2\2\u00ae")
        buf.write(u"\32\3\2\2\2\u00af\u00b0\7]\2\2\u00b0\34\3\2\2\2\u00b1")
        buf.write(u"\u00b2\7_\2\2\u00b2\36\3\2\2\2\u00b3\u00b4\7k\2\2\u00b4")
        buf.write(u"\u00b5\7h\2\2\u00b5 \3\2\2\2\u00b6\u00b7\7g\2\2\u00b7")
        buf.write(u"\u00b8\7n\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba\7g\2\2\u00ba")
        buf.write(u"\"\3\2\2\2\u00bb\u00bc\7r\2\2\u00bc\u00bd\7t\2\2\u00bd")
        buf.write(u"\u00be\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0")
        buf.write(u"$\3\2\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7g\2\2\u00c3")
        buf.write(u"\u00c4\7c\2\2\u00c4\u00c5\7f\2\2\u00c5&\3\2\2\2\u00c6")
        buf.write(u"\u00c7\7-\2\2\u00c7(\3\2\2\2\u00c8\u00c9\7/\2\2\u00c9")
        buf.write(u"*\3\2\2\2\u00ca\u00cb\7,\2\2\u00cb,\3\2\2\2\u00cc\u00cd")
        buf.write(u"\7\61\2\2\u00cd.\3\2\2\2\u00ce\u00cf\7\'\2\2\u00cf\60")
        buf.write(u"\3\2\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7p\2\2\u00d2")
        buf.write(u"\u00d3\7v\2\2\u00d3\62\3\2\2\2\u00d4\u00d5\7h\2\2\u00d5")
        buf.write(u"\u00d6\7n\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7c\2\2\u00d8")
        buf.write(u"\u00d9\7v\2\2\u00d9\64\3\2\2\2\u00da\u00db\7u\2\2\u00db")
        buf.write(u"\u00dc\7v\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de\7k\2\2\u00de")
        buf.write(u"\u00df\7p\2\2\u00df\u00e0\7i\2\2\u00e0\66\3\2\2\2\u00e1")
        buf.write(u"\u00e2\7d\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7q\2\2\u00e4")
        buf.write(u"\u00e5\7n\2\2\u00e58\3\2\2\2\u00e6\u00e7\7n\2\2\u00e7")
        buf.write(u"\u00e8\7k\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write(u":\3\2\2\2\u00eb\u00ec\7h\2\2\u00ec\u00ed\7q\2\2\u00ed")
        buf.write(u"\u00ee\7t\2\2\u00ee<\3\2\2\2\u00ef\u00f0\7?\2\2\u00f0")
        buf.write(u">\3\2\2\2\u00f1\u00f2\7<\2\2\u00f2@\3\2\2\2\u00f3\u00f4")
        buf.write(u"\7y\2\2\u00f4\u00f5\7j\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7")
        buf.write(u"\7n\2\2\u00f7\u00f8\7g\2\2\u00f8B\3\2\2\2\u00f9\u00fa")
        buf.write(u"\7o\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd")
        buf.write(u"\7p\2\2\u00fdD\3\2\2\2\u00fe\u00ff\7x\2\2\u00ff\u0100")
        buf.write(u"\7c\2\2\u0100\u0101\7t\2\2\u0101\u0102\7k\2\2\u0102\u0103")
        buf.write(u"\7c\2\2\u0103\u0104\7p\2\2\u0104\u0105\7e\2\2\u0105\u0106")
        buf.write(u"\7g\2\2\u0106F\3\2\2\2\u0107\u0108\7o\2\2\u0108\u0109")
        buf.write(u"\7g\2\2\u0109\u010a\7f\2\2\u010a\u010b\7k\2\2\u010b\u010c")
        buf.write(u"\7c\2\2\u010c\u010d\7p\2\2\u010dH\3\2\2\2\u010e\u010f")
        buf.write(u"\7u\2\2\u010f\u0110\7v\2\2\u0110\u0111\7f\2\2\u0111\u0112")
        buf.write(u"\7g\2\2\u0112\u0113\7x\2\2\u0113J\3\2\2\2\u0114\u0115")
        buf.write(u"\7j\2\2\u0115\u0116\7g\2\2\u0116\u0117\7c\2\2\u0117\u0118")
        buf.write(u"\7f\2\2\u0118L\3\2\2\2\u0119\u011a\7v\2\2\u011a\u011b")
        buf.write(u"\7c\2\2\u011b\u011c\7k\2\2\u011c\u011d\7n\2\2\u011dN")
        buf.write(u"\3\2\2\2\u011e\u011f\7w\2\2\u011f\u0120\7p\2\2\u0120")
        buf.write(u"\u0121\7k\2\2\u0121\u0122\7q\2\2\u0122\u0123\7p\2\2\u0123")
        buf.write(u"P\3\2\2\2\u0124\u0125\7k\2\2\u0125\u0126\7p\2\2\u0126")
        buf.write(u"\u0127\7v\2\2\u0127\u0128\7g\2\2\u0128\u0129\7t\2\2\u0129")
        buf.write(u"\u012a\7u\2\2\u012a\u012b\7g\2\2\u012b\u012c\7e\2\2\u012c")
        buf.write(u"\u012d\7v\2\2\u012dR\3\2\2\2\u012e\u012f\7h\2\2\u012f")
        buf.write(u"\u0130\7k\2\2\u0130\u0131\7p\2\2\u0131\u0132\7f\2\2\u0132")
        buf.write(u"T\3\2\2\2\u0133\u0134\7k\2\2\u0134\u0135\7o\2\2\u0135")
        buf.write(u"\u0136\7r\2\2\u0136\u0137\7q\2\2\u0137\u0138\7t\2\2\u0138")
        buf.write(u"\u0139\7v\2\2\u0139V\3\2\2\2\u013a\u013b\7n\2\2\u013b")
        buf.write(u"\u013c\7g\2\2\u013c\u013d\7p\2\2\u013d\u013e\7i\2\2\u013e")
        buf.write(u"\u013f\7v\2\2\u013f\u0140\7j\2\2\u0140X\3\2\2\2\u0141")
        buf.write(u"\u0142\7o\2\2\u0142\u0143\7k\2\2\u0143\u0144\7p\2\2\u0144")
        buf.write(u"Z\3\2\2\2\u0145\u0146\7o\2\2\u0146\u0147\7c\2\2\u0147")
        buf.write(u"\u0148\7z\2\2\u0148\\\3\2\2\2\u0149\u014a\7e\2\2\u014a")
        buf.write(u"\u014b\7q\2\2\u014b\u014c\7p\2\2\u014c\u014d\7e\2\2\u014d")
        buf.write(u"\u014e\7c\2\2\u014e\u014f\7v\2\2\u014f^\3\2\2\2\u0150")
        buf.write(u"\u0151\7u\2\2\u0151\u0152\7q\2\2\u0152\u0153\7t\2\2\u0153")
        buf.write(u"\u0154\7v\2\2\u0154`\3\2\2\2\u0155\u0156\7u\2\2\u0156")
        buf.write(u"\u0157\7r\2\2\u0157\u0158\7n\2\2\u0158\u0159\7k\2\2\u0159")
        buf.write(u"\u015a\7e\2\2\u015a\u015b\7g\2\2\u015bb\3\2\2\2\u015c")
        buf.write(u"\u015d\7j\2\2\u015d\u015e\7k\2\2\u015e\u015f\7u\2\2\u015f")
        buf.write(u"\u0160\7v\2\2\u0160\u0161\7q\2\2\u0161\u0162\7i\2\2\u0162")
        buf.write(u"\u0163\7t\2\2\u0163\u0164\7c\2\2\u0164\u0165\7o\2\2\u0165")
        buf.write(u"d\3\2\2\2\u0166\u0167\7r\2\2\u0167\u0168\7k\2\2\u0168")
        buf.write(u"\u0169\7g\2\2\u0169\u016a\7a\2\2\u016a\u016b\7e\2\2\u016b")
        buf.write(u"\u016c\7j\2\2\u016c\u016d\7c\2\2\u016d\u016e\7t\2\2\u016e")
        buf.write(u"\u016f\7v\2\2\u016ff\3\2\2\2\u0170\u0171\7d\2\2\u0171")
        buf.write(u"\u0172\7c\2\2\u0172\u0173\7t\2\2\u0173\u0174\7a\2\2\u0174")
        buf.write(u"\u0175\7i\2\2\u0175\u0176\7t\2\2\u0176\u0177\7c\2\2\u0177")
        buf.write(u"\u0178\7r\2\2\u0178\u0179\7j\2\2\u0179h\3\2\2\2\u017a")
        buf.write(u"\u017b\7g\2\2\u017b\u017c\7z\2\2\u017c\u017d\7r\2\2\u017d")
        buf.write(u"\u017e\7q\2\2\u017e\u017f\7t\2\2\u017f\u0180\7v\2\2\u0180")
        buf.write(u"j\3\2\2\2\u0181\u0182\7\60\2\2\u0182\u0183\7e\2\2\u0183")
        buf.write(u"\u0184\7u\2\2\u0184\u0185\7x\2\2\u0185l\3\2\2\2\u0186")
        buf.write(u"\u0187\7%\2\2\u0187\u0188\7q\2\2\u0188\u0189\7u\2\2\u0189")
        buf.write(u"\u018a\7e\2\2\u018a\u018b\7c\2\2\u018b\u023d\7t\2\2\u018c")
        buf.write(u"\u018d\7h\2\2\u018d\u018e\7q\2\2\u018e\u023d\7t\2\2\u018f")
        buf.write(u"\u0190\7y\2\2\u0190\u0191\7j\2\2\u0191\u0192\7k\2\2\u0192")
        buf.write(u"\u0193\7n\2\2\u0193\u023d\7g\2\2\u0194\u0195\7k\2\2\u0195")
        buf.write(u"\u023d\7h\2\2\u0196\u0197\7g\2\2\u0197\u0198\7n\2\2\u0198")
        buf.write(u"\u0199\7u\2\2\u0199\u023d\7g\2\2\u019a\u019b\7k\2\2\u019b")
        buf.write(u"\u019c\7p\2\2\u019c\u023d\7v\2\2\u019d\u019e\7h\2\2\u019e")
        buf.write(u"\u019f\7n\2\2\u019f\u01a0\7q\2\2\u01a0\u01a1\7c\2\2\u01a1")
        buf.write(u"\u023d\7v\2\2\u01a2\u01a3\7u\2\2\u01a3\u01a4\7v\2\2\u01a4")
        buf.write(u"\u01a5\7t\2\2\u01a5\u01a6\7k\2\2\u01a6\u01a7\7p\2\2\u01a7")
        buf.write(u"\u023d\7i\2\2\u01a8\u01a9\7d\2\2\u01a9\u01aa\7q\2\2\u01aa")
        buf.write(u"\u01ab\7q\2\2\u01ab\u023d\7n\2\2\u01ac\u01ad\7n\2\2\u01ad")
        buf.write(u"\u01ae\7k\2\2\u01ae\u01af\7u\2\2\u01af\u023d\7v\2\2\u01b0")
        buf.write(u"\u01b1\7o\2\2\u01b1\u01b2\7k\2\2\u01b2\u023d\7p\2\2\u01b3")
        buf.write(u"\u01b4\7o\2\2\u01b4\u01b5\7c\2\2\u01b5\u023d\7z\2\2\u01b6")
        buf.write(u"\u01b7\7o\2\2\u01b7\u01b8\7g\2\2\u01b8\u01b9\7c\2\2\u01b9")
        buf.write(u"\u023d\7p\2\2\u01ba\u01bb\7o\2\2\u01bb\u01bc\7q\2\2\u01bc")
        buf.write(u"\u01bd\7f\2\2\u01bd\u023d\7g\2\2\u01be\u01bf\7x\2\2\u01bf")
        buf.write(u"\u01c0\7c\2\2\u01c0\u01c1\7t\2\2\u01c1\u01c2\7k\2\2\u01c2")
        buf.write(u"\u01c3\7c\2\2\u01c3\u01c4\7p\2\2\u01c4\u01c5\7e\2\2\u01c5")
        buf.write(u"\u023d\7g\2\2\u01c6\u01c7\7u\2\2\u01c7\u01c8\7v\2\2\u01c8")
        buf.write(u"\u01c9\7f\2\2\u01c9\u01ca\7g\2\2\u01ca\u023d\7x\2\2\u01cb")
        buf.write(u"\u01cc\7o\2\2\u01cc\u01cd\7g\2\2\u01cd\u01ce\7f\2\2\u01ce")
        buf.write(u"\u01cf\7k\2\2\u01cf\u01d0\7c\2\2\u01d0\u023d\7p\2\2\u01d1")
        buf.write(u"\u01d2\7v\2\2\u01d2\u01d3\7c\2\2\u01d3\u01d4\7k\2\2\u01d4")
        buf.write(u"\u023d\7n\2\2\u01d5\u01d6\7j\2\2\u01d6\u01d7\7g\2\2\u01d7")
        buf.write(u"\u01d8\7c\2\2\u01d8\u023d\7f\2\2\u01d9\u01da\7t\2\2\u01da")
        buf.write(u"\u01db\7g\2\2\u01db\u01dc\7c\2\2\u01dc\u023d\7f\2\2\u01dd")
        buf.write(u"\u01de\7r\2\2\u01de\u01df\7t\2\2\u01df\u01e0\7k\2\2\u01e0")
        buf.write(u"\u01e1\7p\2\2\u01e1\u023d\7v\2\2\u01e2\u01e3\7t\2\2\u01e3")
        buf.write(u"\u01e4\7g\2\2\u01e4\u01e5\7v\2\2\u01e5\u01e6\7w\2\2\u01e6")
        buf.write(u"\u01e7\7t\2\2\u01e7\u023d\7p\2\2\u01e8\u01e9\7n\2\2\u01e9")
        buf.write(u"\u01ea\7g\2\2\u01ea\u01eb\7p\2\2\u01eb\u01ec\7i\2\2\u01ec")
        buf.write(u"\u01ed\7v\2\2\u01ed\u023d\7j\2\2\u01ee\u01ef\7c\2\2\u01ef")
        buf.write(u"\u01f0\7p\2\2\u01f0\u023d\7f\2\2\u01f1\u01f2\7q\2\2\u01f2")
        buf.write(u"\u023d\7t\2\2\u01f3\u01f4\7k\2\2\u01f4\u01f5\7o\2\2\u01f5")
        buf.write(u"\u01f6\7r\2\2\u01f6\u01f7\7q\2\2\u01f7\u01f8\7t\2\2\u01f8")
        buf.write(u"\u023d\7v\2\2\u01f9\u01fa\7g\2\2\u01fa\u01fb\7z\2\2\u01fb")
        buf.write(u"\u01fc\7r\2\2\u01fc\u01fd\7q\2\2\u01fd\u01fe\7t\2\2\u01fe")
        buf.write(u"\u023d\7v\2\2\u01ff\u0200\7r\2\2\u0200\u0201\7k\2\2\u0201")
        buf.write(u"\u0202\7g\2\2\u0202\u0203\7a\2\2\u0203\u0204\7e\2\2\u0204")
        buf.write(u"\u0205\7j\2\2\u0205\u0206\7c\2\2\u0206\u0207\7t\2\2\u0207")
        buf.write(u"\u023d\7v\2\2\u0208\u0209\7j\2\2\u0209\u020a\7k\2\2\u020a")
        buf.write(u"\u020b\7u\2\2\u020b\u020c\7v\2\2\u020c\u020d\7q\2\2\u020d")
        buf.write(u"\u020e\7i\2\2\u020e\u020f\7t\2\2\u020f\u0210\7c\2\2\u0210")
        buf.write(u"\u023d\7o\2\2\u0211\u0212\7d\2\2\u0212\u0213\7c\2\2\u0213")
        buf.write(u"\u0214\7t\2\2\u0214\u0215\7a\2\2\u0215\u0216\7i\2\2\u0216")
        buf.write(u"\u0217\7t\2\2\u0217\u0218\7c\2\2\u0218\u0219\7r\2\2\u0219")
        buf.write(u"\u023d\7j\2\2\u021a\u021b\7e\2\2\u021b\u021c\7q\2\2\u021c")
        buf.write(u"\u021d\7p\2\2\u021d\u021e\7e\2\2\u021e\u021f\7c\2\2\u021f")
        buf.write(u"\u023d\7v\2\2\u0220\u0221\7u\2\2\u0221\u0222\7r\2\2\u0222")
        buf.write(u"\u0223\7n\2\2\u0223\u0224\7k\2\2\u0224\u0225\7e\2\2\u0225")
        buf.write(u"\u023d\7g\2\2\u0226\u0227\7h\2\2\u0227\u0228\7k\2\2\u0228")
        buf.write(u"\u0229\7p\2\2\u0229\u023d\7f\2\2\u022a\u022b\7w\2\2\u022b")
        buf.write(u"\u022c\7p\2\2\u022c\u022d\7k\2\2\u022d\u022e\7q\2\2\u022e")
        buf.write(u"\u023d\7p\2\2\u022f\u0230\7k\2\2\u0230\u0231\7p\2\2\u0231")
        buf.write(u"\u0232\7v\2\2\u0232\u0233\7g\2\2\u0233\u0234\7t\2\2\u0234")
        buf.write(u"\u0235\7u\2\2\u0235\u0236\7g\2\2\u0236\u0237\7e\2\2\u0237")
        buf.write(u"\u023d\7v\2\2\u0238\u0239\7u\2\2\u0239\u023a\7q\2\2\u023a")
        buf.write(u"\u023b\7t\2\2\u023b\u023d\7v\2\2\u023c\u0186\3\2\2\2")
        buf.write(u"\u023c\u018c\3\2\2\2\u023c\u018f\3\2\2\2\u023c\u0194")
        buf.write(u"\3\2\2\2\u023c\u0196\3\2\2\2\u023c\u019a\3\2\2\2\u023c")
        buf.write(u"\u019d\3\2\2\2\u023c\u01a2\3\2\2\2\u023c\u01a8\3\2\2")
        buf.write(u"\2\u023c\u01ac\3\2\2\2\u023c\u01b0\3\2\2\2\u023c\u01b3")
        buf.write(u"\3\2\2\2\u023c\u01b6\3\2\2\2\u023c\u01ba\3\2\2\2\u023c")
        buf.write(u"\u01be\3\2\2\2\u023c\u01c6\3\2\2\2\u023c\u01cb\3\2\2")
        buf.write(u"\2\u023c\u01d1\3\2\2\2\u023c\u01d5\3\2\2\2\u023c\u01d9")
        buf.write(u"\3\2\2\2\u023c\u01dd\3\2\2\2\u023c\u01e2\3\2\2\2\u023c")
        buf.write(u"\u01e8\3\2\2\2\u023c\u01ee\3\2\2\2\u023c\u01f1\3\2\2")
        buf.write(u"\2\u023c\u01f3\3\2\2\2\u023c\u01f9\3\2\2\2\u023c\u01ff")
        buf.write(u"\3\2\2\2\u023c\u0208\3\2\2\2\u023c\u0211\3\2\2\2\u023c")
        buf.write(u"\u021a\3\2\2\2\u023c\u0220\3\2\2\2\u023c\u0226\3\2\2")
        buf.write(u"\2\u023c\u022a\3\2\2\2\u023c\u022f\3\2\2\2\u023c\u0238")
        buf.write(u"\3\2\2\2\u023dn\3\2\2\2\u023e\u0248\t\2\2\2\u023f\u0240")
        buf.write(u"\7@\2\2\u0240\u0248\7?\2\2\u0241\u0242\7>\2\2\u0242\u0248")
        buf.write(u"\7?\2\2\u0243\u0244\7#\2\2\u0244\u0248\7?\2\2\u0245\u0246")
        buf.write(u"\7?\2\2\u0246\u0248\7?\2\2\u0247\u023e\3\2\2\2\u0247")
        buf.write(u"\u023f\3\2\2\2\u0247\u0241\3\2\2\2\u0247\u0243\3\2\2")
        buf.write(u"\2\u0247\u0245\3\2\2\2\u0248p\3\2\2\2\u0249\u024a\7(")
        buf.write(u"\2\2\u024a\u024e\7(\2\2\u024b\u024c\7~\2\2\u024c\u024e")
        buf.write(u"\7~\2\2\u024d\u0249\3\2\2\2\u024d\u024b\3\2\2\2\u024e")
        buf.write(u"r\3\2\2\2\u024f\u0250\t\3\2\2\u0250t\3\2\2\2\u0251\u0252")
        buf.write(u"\t\4\2\2\u0252\u0253\3\2\2\2\u0253\u0254\b;\2\2\u0254")
        buf.write(u"v\3\2\2\2\u0255\u0259\t\5\2\2\u0256\u0258\t\6\2\2\u0257")
        buf.write(u"\u0256\3\2\2\2\u0258\u025b\3\2\2\2\u0259\u0257\3\2\2")
        buf.write(u"\2\u0259\u025a\3\2\2\2\u025ax\3\2\2\2\u025b\u0259\3\2")
        buf.write(u"\2\2\u025c\u025d\7a\2\2\u025d\u025e\7v\2\2\u025e\u025f")
        buf.write(u"\7t\2\2\u025f\u0260\7w\2\2\u0260\u0268\7g\2\2\u0261\u0262")
        buf.write(u"\7a\2\2\u0262\u0263\7h\2\2\u0263\u0264\7c\2\2\u0264\u0265")
        buf.write(u"\7n\2\2\u0265\u0266\7u\2\2\u0266\u0268\7g\2\2\u0267\u025c")
        buf.write(u"\3\2\2\2\u0267\u0261\3\2\2\2\u0268z\3\2\2\2\u0269\u026b")
        buf.write(u"\4\62;\2\u026a\u0269\3\2\2\2\u026b\u026c\3\2\2\2\u026c")
        buf.write(u"\u026a\3\2\2\2\u026c\u026d\3\2\2\2\u026d|\3\2\2\2\u026e")
        buf.write(u"\u0270\4\62;\2\u026f\u026e\3\2\2\2\u0270\u0271\3\2\2")
        buf.write(u"\2\u0271\u026f\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u0273")
        buf.write(u"\3\2\2\2\u0273\u0277\7\60\2\2\u0274\u0276\4\62;\2\u0275")
        buf.write(u"\u0274\3\2\2\2\u0276\u0279\3\2\2\2\u0277\u0275\3\2\2")
        buf.write(u"\2\u0277\u0278\3\2\2\2\u0278~\3\2\2\2\u0279\u0277\3\2")
        buf.write(u"\2\2\u027a\u027f\7$\2\2\u027b\u027e\t\6\2\2\u027c\u027e")
        buf.write(u"\5u;\2\u027d\u027b\3\2\2\2\u027d\u027c\3\2\2\2\u027e")
        buf.write(u"\u0281\3\2\2\2\u027f\u027d\3\2\2\2\u027f\u0280\3\2\2")
        buf.write(u"\2\u0280\u0282\3\2\2\2\u0281\u027f\3\2\2\2\u0282\u0283")
        buf.write(u"\7$\2\2\u0283\u0080\3\2\2\2\u0284\u028c\7]\2\2\u0285")
        buf.write(u"\u028b\5\177@\2\u0286\u028b\5{>\2\u0287\u028b\5}?\2\u0288")
        buf.write(u"\u028b\5y=\2\u0289\u028b\5\u0081A\2\u028a\u0285\3\2\2")
        buf.write(u"\2\u028a\u0286\3\2\2\2\u028a\u0287\3\2\2\2\u028a\u0288")
        buf.write(u"\3\2\2\2\u028a\u0289\3\2\2\2\u028b\u028e\3\2\2\2\u028c")
        buf.write(u"\u028a\3\2\2\2\u028c\u028d\3\2\2\2\u028d\u028f\3\2\2")
        buf.write(u"\2\u028e\u028c\3\2\2\2\u028f\u0290\7_\2\2\u0290\u0082")
        buf.write(u"\3\2\2\2\17\2\u023c\u0247\u024d\u0259\u0267\u026c\u0271")
        buf.write(u"\u0277\u027d\u027f\u028a\u028c\3\b\2\2")
        return buf.getvalue()


class oscarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    RESERVED = 54
    RELACIONALES = 55
    LOGICOS = 56
    DELIMITADORES = 57
    WS = 58
    ID = 59
    CTE_B = 60
    CTE_I = 61
    CTE_F = 62
    CTE_STRING = 63
    LIST = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'#oscar'", u"';'", u"'def'", u"'void'", u"'main'", u"'('", 
            u"','", u"')'", u"'{'", u"'return'", u"'}'", u"'var'", u"'['", 
            u"']'", u"'if'", u"'else'", u"'print'", u"'read'", u"'+'", u"'-'", 
            u"'*'", u"'/'", u"'%'", u"'int'", u"'float'", u"'string'", u"'bool'", 
            u"'list'", u"'for'", u"'='", u"':'", u"'while'", u"'mean'", 
            u"'variance'", u"'median'", u"'stdev'", u"'head'", u"'tail'", 
            u"'union'", u"'intersect'", u"'find'", u"'import'", u"'length'", 
            u"'min'", u"'max'", u"'concat'", u"'sort'", u"'splice'", u"'histogram'", 
            u"'pie_chart'", u"'bar_graph'", u"'export'", u"'.csv'" ]

    symbolicNames = [ u"<INVALID>",
            u"RESERVED", u"RELACIONALES", u"LOGICOS", u"DELIMITADORES", 
            u"WS", u"ID", u"CTE_B", u"CTE_I", u"CTE_F", u"CTE_STRING", u"LIST" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"T__10", u"T__11", 
                  u"T__12", u"T__13", u"T__14", u"T__15", u"T__16", u"T__17", 
                  u"T__18", u"T__19", u"T__20", u"T__21", u"T__22", u"T__23", 
                  u"T__24", u"T__25", u"T__26", u"T__27", u"T__28", u"T__29", 
                  u"T__30", u"T__31", u"T__32", u"T__33", u"T__34", u"T__35", 
                  u"T__36", u"T__37", u"T__38", u"T__39", u"T__40", u"T__41", 
                  u"T__42", u"T__43", u"T__44", u"T__45", u"T__46", u"T__47", 
                  u"T__48", u"T__49", u"T__50", u"T__51", u"T__52", u"RESERVED", 
                  u"RELACIONALES", u"LOGICOS", u"DELIMITADORES", u"WS", 
                  u"ID", u"CTE_B", u"CTE_I", u"CTE_F", u"CTE_STRING", u"LIST" ]

    grammarFileName = u"oscar.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(oscarLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


