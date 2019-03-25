// Generated from c:\Users\oscar\Documents\Compilador\ProyectoCompiladores\oscar.g4 by ANTLR 4.7.1

import rules

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class oscarLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, T__48=49, T__49=50, T__50=51, T__51=52, 
		T__52=53, RESERVED=54, RELACIONALES=55, LOGICOS=56, DELIMITADORES=57, 
		WS=58, ID=59, CTE_B=60, CTE_I=61, CTE_F=62, CTE_STRING=63, LIST=64;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
		"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
		"T__17", "T__18", "T__19", "T__20", "T__21", "T__22", "T__23", "T__24", 
		"T__25", "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", "T__32", 
		"T__33", "T__34", "T__35", "T__36", "T__37", "T__38", "T__39", "T__40", 
		"T__41", "T__42", "T__43", "T__44", "T__45", "T__46", "T__47", "T__48", 
		"T__49", "T__50", "T__51", "T__52", "RESERVED", "RELACIONALES", "LOGICOS", 
		"DELIMITADORES", "WS", "ID", "CTE_B", "CTE_I", "CTE_F", "CTE_STRING", 
		"LIST"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'#oscar'", "';'", "'def'", "'void'", "'main'", "'('", "','", "')'", 
		"'{'", "'return'", "'}'", "'var'", "'['", "']'", "'if'", "'else'", "'print'", 
		"'read'", "'+'", "'-'", "'*'", "'/'", "'%'", "'int'", "'float'", "'string'", 
		"'boolean'", "'list'", "'for'", "'='", "':'", "'while'", "'mean'", "'variance'", 
		"'median'", "'stdev'", "'head'", "'tail'", "'union'", "'intersect'", "'find'", 
		"'import'", "'length'", "'min'", "'max'", "'concat'", "'sort'", "'splice'", 
		"'histogram'", "'pie_chart'", "'bar_graph'", "'export'", "'.csv'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, "RESERVED", "RELACIONALES", "LOGICOS", 
		"DELIMITADORES", "WS", "ID", "CTE_B", "CTE_I", "CTE_F", "CTE_STRING", 
		"LIST"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public oscarLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "oscar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B\u0291\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3"+
		"\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t"+
		"\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3"+
		"\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3"+
		"\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3"+
		"\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3"+
		"\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3"+
		"\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 "+
		"\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3"+
		"$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'"+
		"\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+"+
		"\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/"+
		"\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3"+
		"\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3"+
		"\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3"+
		"\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3"+
		"\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\5\67\u0240\n\67\38\38\38\38\38\38\38\38\58\u024a\n8\39\39\39\39\5"+
		"9\u0250\n9\3:\3:\3;\3;\3;\3;\3<\3<\7<\u025a\n<\f<\16<\u025d\13<\3=\3="+
		"\3=\3=\3=\3=\3=\3=\3=\5=\u0268\n=\3>\6>\u026b\n>\r>\16>\u026c\3?\6?\u0270"+
		"\n?\r?\16?\u0271\3?\3?\7?\u0276\n?\f?\16?\u0279\13?\3@\3@\3@\7@\u027e"+
		"\n@\f@\16@\u0281\13@\3@\3@\3A\3A\3A\3A\3A\3A\7A\u028b\nA\fA\16A\u028e"+
		"\13A\3A\3A\2\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31"+
		"\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65"+
		"\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64"+
		"g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\3\2\7\4\2>>@@\7\2*+]]__}}\177"+
		"\177\5\2\13\f\17\17\"\"\4\2C\\c|\5\2\62;C\\c|\2\u02c4\2\3\3\2\2\2\2\5"+
		"\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2"+
		"\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33"+
		"\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2"+
		"\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2"+
		"\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2"+
		"\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K"+
		"\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2"+
		"\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2"+
		"\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q"+
		"\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2"+
		"\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u008a\3\2\2\2\7\u008c"+
		"\3\2\2\2\t\u0090\3\2\2\2\13\u0095\3\2\2\2\r\u009a\3\2\2\2\17\u009c\3\2"+
		"\2\2\21\u009e\3\2\2\2\23\u00a0\3\2\2\2\25\u00a2\3\2\2\2\27\u00a9\3\2\2"+
		"\2\31\u00ab\3\2\2\2\33\u00af\3\2\2\2\35\u00b1\3\2\2\2\37\u00b3\3\2\2\2"+
		"!\u00b6\3\2\2\2#\u00bb\3\2\2\2%\u00c1\3\2\2\2\'\u00c6\3\2\2\2)\u00c8\3"+
		"\2\2\2+\u00ca\3\2\2\2-\u00cc\3\2\2\2/\u00ce\3\2\2\2\61\u00d0\3\2\2\2\63"+
		"\u00d4\3\2\2\2\65\u00da\3\2\2\2\67\u00e1\3\2\2\29\u00e9\3\2\2\2;\u00ee"+
		"\3\2\2\2=\u00f2\3\2\2\2?\u00f4\3\2\2\2A\u00f6\3\2\2\2C\u00fc\3\2\2\2E"+
		"\u0101\3\2\2\2G\u010a\3\2\2\2I\u0111\3\2\2\2K\u0117\3\2\2\2M\u011c\3\2"+
		"\2\2O\u0121\3\2\2\2Q\u0127\3\2\2\2S\u0131\3\2\2\2U\u0136\3\2\2\2W\u013d"+
		"\3\2\2\2Y\u0144\3\2\2\2[\u0148\3\2\2\2]\u014c\3\2\2\2_\u0153\3\2\2\2a"+
		"\u0158\3\2\2\2c\u015f\3\2\2\2e\u0169\3\2\2\2g\u0173\3\2\2\2i\u017d\3\2"+
		"\2\2k\u0184\3\2\2\2m\u023f\3\2\2\2o\u0249\3\2\2\2q\u024f\3\2\2\2s\u0251"+
		"\3\2\2\2u\u0253\3\2\2\2w\u0257\3\2\2\2y\u0267\3\2\2\2{\u026a\3\2\2\2}"+
		"\u026f\3\2\2\2\177\u027a\3\2\2\2\u0081\u0284\3\2\2\2\u0083\u0084\7%\2"+
		"\2\u0084\u0085\7q\2\2\u0085\u0086\7u\2\2\u0086\u0087\7e\2\2\u0087\u0088"+
		"\7c\2\2\u0088\u0089\7t\2\2\u0089\4\3\2\2\2\u008a\u008b\7=\2\2\u008b\6"+
		"\3\2\2\2\u008c\u008d\7f\2\2\u008d\u008e\7g\2\2\u008e\u008f\7h\2\2\u008f"+
		"\b\3\2\2\2\u0090\u0091\7x\2\2\u0091\u0092\7q\2\2\u0092\u0093\7k\2\2\u0093"+
		"\u0094\7f\2\2\u0094\n\3\2\2\2\u0095\u0096\7o\2\2\u0096\u0097\7c\2\2\u0097"+
		"\u0098\7k\2\2\u0098\u0099\7p\2\2\u0099\f\3\2\2\2\u009a\u009b\7*\2\2\u009b"+
		"\16\3\2\2\2\u009c\u009d\7.\2\2\u009d\20\3\2\2\2\u009e\u009f\7+\2\2\u009f"+
		"\22\3\2\2\2\u00a0\u00a1\7}\2\2\u00a1\24\3\2\2\2\u00a2\u00a3\7t\2\2\u00a3"+
		"\u00a4\7g\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7t\2\2"+
		"\u00a7\u00a8\7p\2\2\u00a8\26\3\2\2\2\u00a9\u00aa\7\177\2\2\u00aa\30\3"+
		"\2\2\2\u00ab\u00ac\7x\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7t\2\2\u00ae"+
		"\32\3\2\2\2\u00af\u00b0\7]\2\2\u00b0\34\3\2\2\2\u00b1\u00b2\7_\2\2\u00b2"+
		"\36\3\2\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7h\2\2\u00b5 \3\2\2\2\u00b6"+
		"\u00b7\7g\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba\7g\2\2"+
		"\u00ba\"\3\2\2\2\u00bb\u00bc\7r\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be\7k"+
		"\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0$\3\2\2\2\u00c1\u00c2"+
		"\7t\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7f\2\2\u00c5"+
		"&\3\2\2\2\u00c6\u00c7\7-\2\2\u00c7(\3\2\2\2\u00c8\u00c9\7/\2\2\u00c9*"+
		"\3\2\2\2\u00ca\u00cb\7,\2\2\u00cb,\3\2\2\2\u00cc\u00cd\7\61\2\2\u00cd"+
		".\3\2\2\2\u00ce\u00cf\7\'\2\2\u00cf\60\3\2\2\2\u00d0\u00d1\7k\2\2\u00d1"+
		"\u00d2\7p\2\2\u00d2\u00d3\7v\2\2\u00d3\62\3\2\2\2\u00d4\u00d5\7h\2\2\u00d5"+
		"\u00d6\7n\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7v\2\2"+
		"\u00d9\64\3\2\2\2\u00da\u00db\7u\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7"+
		"t\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7i\2\2\u00e0\66"+
		"\3\2\2\2\u00e1\u00e2\7d\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7q\2\2\u00e4"+
		"\u00e5\7n\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8\7p\2\2"+
		"\u00e88\3\2\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec\7u\2"+
		"\2\u00ec\u00ed\7v\2\2\u00ed:\3\2\2\2\u00ee\u00ef\7h\2\2\u00ef\u00f0\7"+
		"q\2\2\u00f0\u00f1\7t\2\2\u00f1<\3\2\2\2\u00f2\u00f3\7?\2\2\u00f3>\3\2"+
		"\2\2\u00f4\u00f5\7<\2\2\u00f5@\3\2\2\2\u00f6\u00f7\7y\2\2\u00f7\u00f8"+
		"\7j\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb\7g\2\2\u00fb"+
		"B\3\2\2\2\u00fc\u00fd\7o\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7c\2\2\u00ff"+
		"\u0100\7p\2\2\u0100D\3\2\2\2\u0101\u0102\7x\2\2\u0102\u0103\7c\2\2\u0103"+
		"\u0104\7t\2\2\u0104\u0105\7k\2\2\u0105\u0106\7c\2\2\u0106\u0107\7p\2\2"+
		"\u0107\u0108\7e\2\2\u0108\u0109\7g\2\2\u0109F\3\2\2\2\u010a\u010b\7o\2"+
		"\2\u010b\u010c\7g\2\2\u010c\u010d\7f\2\2\u010d\u010e\7k\2\2\u010e\u010f"+
		"\7c\2\2\u010f\u0110\7p\2\2\u0110H\3\2\2\2\u0111\u0112\7u\2\2\u0112\u0113"+
		"\7v\2\2\u0113\u0114\7f\2\2\u0114\u0115\7g\2\2\u0115\u0116\7x\2\2\u0116"+
		"J\3\2\2\2\u0117\u0118\7j\2\2\u0118\u0119\7g\2\2\u0119\u011a\7c\2\2\u011a"+
		"\u011b\7f\2\2\u011bL\3\2\2\2\u011c\u011d\7v\2\2\u011d\u011e\7c\2\2\u011e"+
		"\u011f\7k\2\2\u011f\u0120\7n\2\2\u0120N\3\2\2\2\u0121\u0122\7w\2\2\u0122"+
		"\u0123\7p\2\2\u0123\u0124\7k\2\2\u0124\u0125\7q\2\2\u0125\u0126\7p\2\2"+
		"\u0126P\3\2\2\2\u0127\u0128\7k\2\2\u0128\u0129\7p\2\2\u0129\u012a\7v\2"+
		"\2\u012a\u012b\7g\2\2\u012b\u012c\7t\2\2\u012c\u012d\7u\2\2\u012d\u012e"+
		"\7g\2\2\u012e\u012f\7e\2\2\u012f\u0130\7v\2\2\u0130R\3\2\2\2\u0131\u0132"+
		"\7h\2\2\u0132\u0133\7k\2\2\u0133\u0134\7p\2\2\u0134\u0135\7f\2\2\u0135"+
		"T\3\2\2\2\u0136\u0137\7k\2\2\u0137\u0138\7o\2\2\u0138\u0139\7r\2\2\u0139"+
		"\u013a\7q\2\2\u013a\u013b\7t\2\2\u013b\u013c\7v\2\2\u013cV\3\2\2\2\u013d"+
		"\u013e\7n\2\2\u013e\u013f\7g\2\2\u013f\u0140\7p\2\2\u0140\u0141\7i\2\2"+
		"\u0141\u0142\7v\2\2\u0142\u0143\7j\2\2\u0143X\3\2\2\2\u0144\u0145\7o\2"+
		"\2\u0145\u0146\7k\2\2\u0146\u0147\7p\2\2\u0147Z\3\2\2\2\u0148\u0149\7"+
		"o\2\2\u0149\u014a\7c\2\2\u014a\u014b\7z\2\2\u014b\\\3\2\2\2\u014c\u014d"+
		"\7e\2\2\u014d\u014e\7q\2\2\u014e\u014f\7p\2\2\u014f\u0150\7e\2\2\u0150"+
		"\u0151\7c\2\2\u0151\u0152\7v\2\2\u0152^\3\2\2\2\u0153\u0154\7u\2\2\u0154"+
		"\u0155\7q\2\2\u0155\u0156\7t\2\2\u0156\u0157\7v\2\2\u0157`\3\2\2\2\u0158"+
		"\u0159\7u\2\2\u0159\u015a\7r\2\2\u015a\u015b\7n\2\2\u015b\u015c\7k\2\2"+
		"\u015c\u015d\7e\2\2\u015d\u015e\7g\2\2\u015eb\3\2\2\2\u015f\u0160\7j\2"+
		"\2\u0160\u0161\7k\2\2\u0161\u0162\7u\2\2\u0162\u0163\7v\2\2\u0163\u0164"+
		"\7q\2\2\u0164\u0165\7i\2\2\u0165\u0166\7t\2\2\u0166\u0167\7c\2\2\u0167"+
		"\u0168\7o\2\2\u0168d\3\2\2\2\u0169\u016a\7r\2\2\u016a\u016b\7k\2\2\u016b"+
		"\u016c\7g\2\2\u016c\u016d\7a\2\2\u016d\u016e\7e\2\2\u016e\u016f\7j\2\2"+
		"\u016f\u0170\7c\2\2\u0170\u0171\7t\2\2\u0171\u0172\7v\2\2\u0172f\3\2\2"+
		"\2\u0173\u0174\7d\2\2\u0174\u0175\7c\2\2\u0175\u0176\7t\2\2\u0176\u0177"+
		"\7a\2\2\u0177\u0178\7i\2\2\u0178\u0179\7t\2\2\u0179\u017a\7c\2\2\u017a"+
		"\u017b\7r\2\2\u017b\u017c\7j\2\2\u017ch\3\2\2\2\u017d\u017e\7g\2\2\u017e"+
		"\u017f\7z\2\2\u017f\u0180\7r\2\2\u0180\u0181\7q\2\2\u0181\u0182\7t\2\2"+
		"\u0182\u0183\7v\2\2\u0183j\3\2\2\2\u0184\u0185\7\60\2\2\u0185\u0186\7"+
		"e\2\2\u0186\u0187\7u\2\2\u0187\u0188\7x\2\2\u0188l\3\2\2\2\u0189\u018a"+
		"\7%\2\2\u018a\u018b\7q\2\2\u018b\u018c\7u\2\2\u018c\u018d\7e\2\2\u018d"+
		"\u018e\7c\2\2\u018e\u0240\7t\2\2\u018f\u0190\7h\2\2\u0190\u0191\7q\2\2"+
		"\u0191\u0240\7t\2\2\u0192\u0193\7y\2\2\u0193\u0194\7j\2\2\u0194\u0195"+
		"\7k\2\2\u0195\u0196\7n\2\2\u0196\u0240\7g\2\2\u0197\u0198\7k\2\2\u0198"+
		"\u0240\7h\2\2\u0199\u019a\7g\2\2\u019a\u019b\7n\2\2\u019b\u019c\7u\2\2"+
		"\u019c\u0240\7g\2\2\u019d\u019e\7k\2\2\u019e\u019f\7p\2\2\u019f\u0240"+
		"\7v\2\2\u01a0\u01a1\7h\2\2\u01a1\u01a2\7n\2\2\u01a2\u01a3\7q\2\2\u01a3"+
		"\u01a4\7c\2\2\u01a4\u0240\7v\2\2\u01a5\u01a6\7u\2\2\u01a6\u01a7\7v\2\2"+
		"\u01a7\u01a8\7t\2\2\u01a8\u01a9\7k\2\2\u01a9\u01aa\7p\2\2\u01aa\u0240"+
		"\7i\2\2\u01ab\u01ac\7d\2\2\u01ac\u01ad\7q\2\2\u01ad\u01ae\7q\2\2\u01ae"+
		"\u0240\7n\2\2\u01af\u01b0\7n\2\2\u01b0\u01b1\7k\2\2\u01b1\u01b2\7u\2\2"+
		"\u01b2\u0240\7v\2\2\u01b3\u01b4\7o\2\2\u01b4\u01b5\7k\2\2\u01b5\u0240"+
		"\7p\2\2\u01b6\u01b7\7o\2\2\u01b7\u01b8\7c\2\2\u01b8\u0240\7z\2\2\u01b9"+
		"\u01ba\7o\2\2\u01ba\u01bb\7g\2\2\u01bb\u01bc\7c\2\2\u01bc\u0240\7p\2\2"+
		"\u01bd\u01be\7o\2\2\u01be\u01bf\7q\2\2\u01bf\u01c0\7f\2\2\u01c0\u0240"+
		"\7g\2\2\u01c1\u01c2\7x\2\2\u01c2\u01c3\7c\2\2\u01c3\u01c4\7t\2\2\u01c4"+
		"\u01c5\7k\2\2\u01c5\u01c6\7c\2\2\u01c6\u01c7\7p\2\2\u01c7\u01c8\7e\2\2"+
		"\u01c8\u0240\7g\2\2\u01c9\u01ca\7u\2\2\u01ca\u01cb\7v\2\2\u01cb\u01cc"+
		"\7f\2\2\u01cc\u01cd\7g\2\2\u01cd\u0240\7x\2\2\u01ce\u01cf\7o\2\2\u01cf"+
		"\u01d0\7g\2\2\u01d0\u01d1\7f\2\2\u01d1\u01d2\7k\2\2\u01d2\u01d3\7c\2\2"+
		"\u01d3\u0240\7p\2\2\u01d4\u01d5\7v\2\2\u01d5\u01d6\7c\2\2\u01d6\u01d7"+
		"\7k\2\2\u01d7\u0240\7n\2\2\u01d8\u01d9\7j\2\2\u01d9\u01da\7g\2\2\u01da"+
		"\u01db\7c\2\2\u01db\u0240\7f\2\2\u01dc\u01dd\7t\2\2\u01dd\u01de\7g\2\2"+
		"\u01de\u01df\7c\2\2\u01df\u0240\7f\2\2\u01e0\u01e1\7r\2\2\u01e1\u01e2"+
		"\7t\2\2\u01e2\u01e3\7k\2\2\u01e3\u01e4\7p\2\2\u01e4\u0240\7v\2\2\u01e5"+
		"\u01e6\7t\2\2\u01e6\u01e7\7g\2\2\u01e7\u01e8\7v\2\2\u01e8\u01e9\7w\2\2"+
		"\u01e9\u01ea\7t\2\2\u01ea\u0240\7p\2\2\u01eb\u01ec\7n\2\2\u01ec\u01ed"+
		"\7g\2\2\u01ed\u01ee\7p\2\2\u01ee\u01ef\7i\2\2\u01ef\u01f0\7v\2\2\u01f0"+
		"\u0240\7j\2\2\u01f1\u01f2\7c\2\2\u01f2\u01f3\7p\2\2\u01f3\u0240\7f\2\2"+
		"\u01f4\u01f5\7q\2\2\u01f5\u0240\7t\2\2\u01f6\u01f7\7k\2\2\u01f7\u01f8"+
		"\7o\2\2\u01f8\u01f9\7r\2\2\u01f9\u01fa\7q\2\2\u01fa\u01fb\7t\2\2\u01fb"+
		"\u0240\7v\2\2\u01fc\u01fd\7g\2\2\u01fd\u01fe\7z\2\2\u01fe\u01ff\7r\2\2"+
		"\u01ff\u0200\7q\2\2\u0200\u0201\7t\2\2\u0201\u0240\7v\2\2\u0202\u0203"+
		"\7r\2\2\u0203\u0204\7k\2\2\u0204\u0205\7g\2\2\u0205\u0206\7a\2\2\u0206"+
		"\u0207\7e\2\2\u0207\u0208\7j\2\2\u0208\u0209\7c\2\2\u0209\u020a\7t\2\2"+
		"\u020a\u0240\7v\2\2\u020b\u020c\7j\2\2\u020c\u020d\7k\2\2\u020d\u020e"+
		"\7u\2\2\u020e\u020f\7v\2\2\u020f\u0210\7q\2\2\u0210\u0211\7i\2\2\u0211"+
		"\u0212\7t\2\2\u0212\u0213\7c\2\2\u0213\u0240\7o\2\2\u0214\u0215\7d\2\2"+
		"\u0215\u0216\7c\2\2\u0216\u0217\7t\2\2\u0217\u0218\7a\2\2\u0218\u0219"+
		"\7i\2\2\u0219\u021a\7t\2\2\u021a\u021b\7c\2\2\u021b\u021c\7r\2\2\u021c"+
		"\u0240\7j\2\2\u021d\u021e\7e\2\2\u021e\u021f\7q\2\2\u021f\u0220\7p\2\2"+
		"\u0220\u0221\7e\2\2\u0221\u0222\7c\2\2\u0222\u0240\7v\2\2\u0223\u0224"+
		"\7u\2\2\u0224\u0225\7r\2\2\u0225\u0226\7n\2\2\u0226\u0227\7k\2\2\u0227"+
		"\u0228\7e\2\2\u0228\u0240\7g\2\2\u0229\u022a\7h\2\2\u022a\u022b\7k\2\2"+
		"\u022b\u022c\7p\2\2\u022c\u0240\7f\2\2\u022d\u022e\7w\2\2\u022e\u022f"+
		"\7p\2\2\u022f\u0230\7k\2\2\u0230\u0231\7q\2\2\u0231\u0240\7p\2\2\u0232"+
		"\u0233\7k\2\2\u0233\u0234\7p\2\2\u0234\u0235\7v\2\2\u0235\u0236\7g\2\2"+
		"\u0236\u0237\7t\2\2\u0237\u0238\7u\2\2\u0238\u0239\7g\2\2\u0239\u023a"+
		"\7e\2\2\u023a\u0240\7v\2\2\u023b\u023c\7u\2\2\u023c\u023d\7q\2\2\u023d"+
		"\u023e\7t\2\2\u023e\u0240\7v\2\2\u023f\u0189\3\2\2\2\u023f\u018f\3\2\2"+
		"\2\u023f\u0192\3\2\2\2\u023f\u0197\3\2\2\2\u023f\u0199\3\2\2\2\u023f\u019d"+
		"\3\2\2\2\u023f\u01a0\3\2\2\2\u023f\u01a5\3\2\2\2\u023f\u01ab\3\2\2\2\u023f"+
		"\u01af\3\2\2\2\u023f\u01b3\3\2\2\2\u023f\u01b6\3\2\2\2\u023f\u01b9\3\2"+
		"\2\2\u023f\u01bd\3\2\2\2\u023f\u01c1\3\2\2\2\u023f\u01c9\3\2\2\2\u023f"+
		"\u01ce\3\2\2\2\u023f\u01d4\3\2\2\2\u023f\u01d8\3\2\2\2\u023f\u01dc\3\2"+
		"\2\2\u023f\u01e0\3\2\2\2\u023f\u01e5\3\2\2\2\u023f\u01eb\3\2\2\2\u023f"+
		"\u01f1\3\2\2\2\u023f\u01f4\3\2\2\2\u023f\u01f6\3\2\2\2\u023f\u01fc\3\2"+
		"\2\2\u023f\u0202\3\2\2\2\u023f\u020b\3\2\2\2\u023f\u0214\3\2\2\2\u023f"+
		"\u021d\3\2\2\2\u023f\u0223\3\2\2\2\u023f\u0229\3\2\2\2\u023f\u022d\3\2"+
		"\2\2\u023f\u0232\3\2\2\2\u023f\u023b\3\2\2\2\u0240n\3\2\2\2\u0241\u024a"+
		"\t\2\2\2\u0242\u0243\7?\2\2\u0243\u024a\7@\2\2\u0244\u0245\7?\2\2\u0245"+
		"\u024a\7>\2\2\u0246\u0247\7#\2\2\u0247\u024a\7?\2\2\u0248\u024a\7#\2\2"+
		"\u0249\u0241\3\2\2\2\u0249\u0242\3\2\2\2\u0249\u0244\3\2\2\2\u0249\u0246"+
		"\3\2\2\2\u0249\u0248\3\2\2\2\u024ap\3\2\2\2\u024b\u024c\7(\2\2\u024c\u0250"+
		"\7(\2\2\u024d\u024e\7~\2\2\u024e\u0250\7~\2\2\u024f\u024b\3\2\2\2\u024f"+
		"\u024d\3\2\2\2\u0250r\3\2\2\2\u0251\u0252\t\3\2\2\u0252t\3\2\2\2\u0253"+
		"\u0254\t\4\2\2\u0254\u0255\3\2\2\2\u0255\u0256\b;\2\2\u0256v\3\2\2\2\u0257"+
		"\u025b\t\5\2\2\u0258\u025a\t\6\2\2\u0259\u0258\3\2\2\2\u025a\u025d\3\2"+
		"\2\2\u025b\u0259\3\2\2\2\u025b\u025c\3\2\2\2\u025cx\3\2\2\2\u025d\u025b"+
		"\3\2\2\2\u025e\u025f\7v\2\2\u025f\u0260\7t\2\2\u0260\u0261\7w\2\2\u0261"+
		"\u0268\7g\2\2\u0262\u0263\7h\2\2\u0263\u0264\7c\2\2\u0264\u0265\7n\2\2"+
		"\u0265\u0266\7u\2\2\u0266\u0268\7g\2\2\u0267\u025e\3\2\2\2\u0267\u0262"+
		"\3\2\2\2\u0268z\3\2\2\2\u0269\u026b\4\62;\2\u026a\u0269\3\2\2\2\u026b"+
		"\u026c\3\2\2\2\u026c\u026a\3\2\2\2\u026c\u026d\3\2\2\2\u026d|\3\2\2\2"+
		"\u026e\u0270\4\62;\2\u026f\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u026f"+
		"\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0277\7\60\2\2"+
		"\u0274\u0276\4\62;\2\u0275\u0274\3\2\2\2\u0276\u0279\3\2\2\2\u0277\u0275"+
		"\3\2\2\2\u0277\u0278\3\2\2\2\u0278~\3\2\2\2\u0279\u0277\3\2\2\2\u027a"+
		"\u027f\7$\2\2\u027b\u027e\t\6\2\2\u027c\u027e\5u;\2\u027d\u027b\3\2\2"+
		"\2\u027d\u027c\3\2\2\2\u027e\u0281\3\2\2\2\u027f\u027d\3\2\2\2\u027f\u0280"+
		"\3\2\2\2\u0280\u0282\3\2\2\2\u0281\u027f\3\2\2\2\u0282\u0283\7$\2\2\u0283"+
		"\u0080\3\2\2\2\u0284\u028c\7]\2\2\u0285\u028b\5\177@\2\u0286\u028b\5{"+
		">\2\u0287\u028b\5}?\2\u0288\u028b\5y=\2\u0289\u028b\5\u0081A\2\u028a\u0285"+
		"\3\2\2\2\u028a\u0286\3\2\2\2\u028a\u0287\3\2\2\2\u028a\u0288\3\2\2\2\u028a"+
		"\u0289\3\2\2\2\u028b\u028e\3\2\2\2\u028c\u028a\3\2\2\2\u028c\u028d\3\2"+
		"\2\2\u028d\u028f\3\2\2\2\u028e\u028c\3\2\2\2\u028f\u0290\7_\2\2\u0290"+
		"\u0082\3\2\2\2\17\2\u023f\u0249\u024f\u025b\u0267\u026c\u0271\u0277\u027d"+
		"\u027f\u028a\u028c\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}