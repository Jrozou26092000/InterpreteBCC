# Generated from /home/juanr/Semestre 2020-2/Lenguajes de Programación/InterpreteBCC/grammar/BCC.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\62")
        buf.write("\u00ed\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\7\2$\n\2\f\2\16")
        buf.write("\2\'\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3")
        buf.write("\63\n\3\f\3\16\3\66\13\3\5\38\n\3\3\3\3\3\5\3<\n\3\3\3")
        buf.write("\3\3\3\4\5\4A\n\4\3\4\7\4D\n\4\f\4\16\4G\13\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\7\5O\n\5\f\5\16\5R\13\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\7\7\\\n\7\f\7\16\7_\13\7\3\7\3\7\5")
        buf.write("\7c\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0097")
        buf.write("\n\b\3\t\3\t\3\t\3\t\5\t\u009d\n\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u00a3\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\7\f\u00b1\n\f\f\f\16\f\u00b4\13\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00bc\n\r\3\16\3\16\3\16\5\16\u00c1\n")
        buf.write("\16\3\17\3\17\3\17\7\17\u00c6\n\17\f\17\16\17\u00c9\13")
        buf.write("\17\3\20\3\20\3\20\7\20\u00ce\n\20\f\20\16\20\u00d1\13")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00e3\n\21\f\21\16")
        buf.write("\21\u00e6\13\21\5\21\u00e8\n\21\3\21\5\21\u00eb\n\21\3")
        buf.write("\21\2\2\22\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \2\6")
        buf.write("\3\2\r\16\3\2\20\25\3\2\26\27\3\2\30\32\2\u0101\2%\3\2")
        buf.write("\2\2\4*\3\2\2\2\6@\3\2\2\2\bJ\3\2\2\2\nU\3\2\2\2\fb\3")
        buf.write("\2\2\2\16\u0096\3\2\2\2\20\u00a2\3\2\2\2\22\u00a4\3\2")
        buf.write("\2\2\24\u00a7\3\2\2\2\26\u00ab\3\2\2\2\30\u00bb\3\2\2")
        buf.write("\2\32\u00bd\3\2\2\2\34\u00c2\3\2\2\2\36\u00ca\3\2\2\2")
        buf.write(" \u00ea\3\2\2\2\"$\5\4\3\2#\"\3\2\2\2$\'\3\2\2\2%#\3\2")
        buf.write("\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\5\6\4\2)\3\3\2\2")
        buf.write("\2*+\7\3\2\2+,\7\35\2\2,-\7\4\2\2-.\7\61\2\2.\67\7\5\2")
        buf.write("\2/\64\5\n\6\2\60\61\7\6\2\2\61\63\5\n\6\2\62\60\3\2\2")
        buf.write("\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\658\3\2\2")
        buf.write("\2\66\64\3\2\2\2\67/\3\2\2\2\678\3\2\2\289\3\2\2\29;\7")
        buf.write("\7\2\2:<\5\b\5\2;:\3\2\2\2;<\3\2\2\2<=\3\2\2\2=>\5\f\7")
        buf.write("\2>\5\3\2\2\2?A\5\b\5\2@?\3\2\2\2@A\3\2\2\2AE\3\2\2\2")
        buf.write("BD\5\16\b\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2FH")
        buf.write("\3\2\2\2GE\3\2\2\2HI\7\b\2\2I\7\3\2\2\2JK\7\t\2\2KP\5")
        buf.write("\n\6\2LM\7\6\2\2MO\5\n\6\2NL\3\2\2\2OR\3\2\2\2PN\3\2\2")
        buf.write("\2PQ\3\2\2\2QS\3\2\2\2RP\3\2\2\2ST\7\n\2\2T\t\3\2\2\2")
        buf.write("UV\7\62\2\2VW\7\4\2\2WX\7\61\2\2X\13\3\2\2\2Y]\7\13\2")
        buf.write("\2Z\\\5\16\b\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2")
        buf.write("\2^`\3\2\2\2_]\3\2\2\2`c\7\f\2\2ac\5\16\b\2bY\3\2\2\2")
        buf.write("ba\3\2\2\2c\r\3\2\2\2de\7 \2\2ef\5\26\f\2fg\7\n\2\2g\u0097")
        buf.write("\3\2\2\2hi\7!\2\2ij\7\62\2\2j\u0097\7\n\2\2kl\7\"\2\2")
        buf.write("lm\5\24\13\2mn\5\22\n\2n\u0097\3\2\2\2op\7#\2\2pq\5\24")
        buf.write("\13\2qr\5\22\n\2rs\7$\2\2st\5\f\7\2t\u0097\3\2\2\2uv\7")
        buf.write("%\2\2vw\5\24\13\2wx\5\22\n\2x\u0097\3\2\2\2yz\5\22\n\2")
        buf.write("z{\7&\2\2{|\5\24\13\2|\u0097\3\2\2\2}~\7\'\2\2~\177\5")
        buf.write("\26\f\2\177\u0080\7\n\2\2\u0080\u0097\3\2\2\2\u0081\u0082")
        buf.write("\7(\2\2\u0082\u0097\5\f\7\2\u0083\u0084\7)\2\2\u0084\u0085")
        buf.write("\7\36\2\2\u0085\u0086\7\4\2\2\u0086\u0097\5\f\7\2\u0087")
        buf.write("\u0088\7*\2\2\u0088\u0089\7\5\2\2\u0089\u008a\5\26\f\2")
        buf.write("\u008a\u008b\7\n\2\2\u008b\u008c\5\26\f\2\u008c\u008d")
        buf.write("\7\n\2\2\u008d\u008e\5\20\t\2\u008e\u008f\7\7\2\2\u008f")
        buf.write("\u0090\5\22\n\2\u0090\u0097\3\2\2\2\u0091\u0092\7+\2\2")
        buf.write("\u0092\u0097\7\n\2\2\u0093\u0094\7,\2\2\u0094\u0097\7")
        buf.write("\n\2\2\u0095\u0097\5\20\t\2\u0096d\3\2\2\2\u0096h\3\2")
        buf.write("\2\2\u0096k\3\2\2\2\u0096o\3\2\2\2\u0096u\3\2\2\2\u0096")
        buf.write("y\3\2\2\2\u0096}\3\2\2\2\u0096\u0081\3\2\2\2\u0096\u0083")
        buf.write("\3\2\2\2\u0096\u0087\3\2\2\2\u0096\u0091\3\2\2\2\u0096")
        buf.write("\u0093\3\2\2\2\u0096\u0095\3\2\2\2\u0097\17\3\2\2\2\u0098")
        buf.write("\u009c\7\62\2\2\u0099\u009a\7\37\2\2\u009a\u009d\5\26")
        buf.write("\f\2\u009b\u009d\t\2\2\2\u009c\u0099\3\2\2\2\u009c\u009b")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a3\7\n\2\2\u009f")
        buf.write("\u00a0\t\2\2\2\u00a0\u00a1\7\62\2\2\u00a1\u00a3\7\n\2")
        buf.write("\2\u00a2\u0098\3\2\2\2\u00a2\u009f\3\2\2\2\u00a3\21\3")
        buf.write("\2\2\2\u00a4\u00a5\7\17\2\2\u00a5\u00a6\5\f\7\2\u00a6")
        buf.write("\23\3\2\2\2\u00a7\u00a8\7\5\2\2\u00a8\u00a9\5\26\f\2\u00a9")
        buf.write("\u00aa\7\7\2\2\u00aa\25\3\2\2\2\u00ab\u00b2\5\30\r\2\u00ac")
        buf.write("\u00ad\7-\2\2\u00ad\u00b1\5\30\r\2\u00ae\u00af\7.\2\2")
        buf.write("\u00af\u00b1\5\30\r\2\u00b0\u00ac\3\2\2\2\u00b0\u00ae")
        buf.write("\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\27\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5")
        buf.write("\u00b6\7/\2\2\u00b6\u00b7\7\5\2\2\u00b7\u00b8\5\26\f\2")
        buf.write("\u00b8\u00b9\7\7\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00bc\5")
        buf.write("\32\16\2\u00bb\u00b5\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc")
        buf.write("\31\3\2\2\2\u00bd\u00c0\5\34\17\2\u00be\u00bf\t\3\2\2")
        buf.write("\u00bf\u00c1\5\34\17\2\u00c0\u00be\3\2\2\2\u00c0\u00c1")
        buf.write("\3\2\2\2\u00c1\33\3\2\2\2\u00c2\u00c7\5\36\20\2\u00c3")
        buf.write("\u00c4\t\4\2\2\u00c4\u00c6\5\36\20\2\u00c5\u00c3\3\2\2")
        buf.write("\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8")
        buf.write("\3\2\2\2\u00c8\35\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cf")
        buf.write("\5 \21\2\u00cb\u00cc\t\5\2\2\u00cc\u00ce\5 \21\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00cf\u00d0\3\2\2\2\u00d0\37\3\2\2\2\u00d1\u00cf\3\2")
        buf.write("\2\2\u00d2\u00eb\7\36\2\2\u00d3\u00eb\7\60\2\2\u00d4\u00d5")
        buf.write("\7\62\2\2\u00d5\u00eb\t\2\2\2\u00d6\u00d7\t\2\2\2\u00d7")
        buf.write("\u00eb\7\62\2\2\u00d8\u00eb\7\62\2\2\u00d9\u00da\7\5\2")
        buf.write("\2\u00da\u00db\5\26\f\2\u00db\u00dc\7\7\2\2\u00dc\u00eb")
        buf.write("\3\2\2\2\u00dd\u00de\7\35\2\2\u00de\u00e7\7\5\2\2\u00df")
        buf.write("\u00e4\5\26\f\2\u00e0\u00e1\7\6\2\2\u00e1\u00e3\5\26\f")
        buf.write("\2\u00e2\u00e0\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e7\u00df\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9\u00eb\7\7\2\2\u00ea\u00d2\3")
        buf.write("\2\2\2\u00ea\u00d3\3\2\2\2\u00ea\u00d4\3\2\2\2\u00ea\u00d6")
        buf.write("\3\2\2\2\u00ea\u00d8\3\2\2\2\u00ea\u00d9\3\2\2\2\u00ea")
        buf.write("\u00dd\3\2\2\2\u00eb!\3\2\2\2\27%\64\67;@EP]b\u0096\u009c")
        buf.write("\u00a2\u00b0\u00b2\u00bb\u00c0\u00c7\u00cf\u00e4\u00e7")
        buf.write("\u00ea")
        return buf.getvalue()


class BCCParser ( Parser ):

    grammarFileName = "BCC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "':'", "'('", "','", "')'", 
                     "'end'", "'var'", "';'", "'{'", "'}'", "'++'", "'--'", 
                     "'do'", "'<'", "'=='", "'<='", "'>'", "'>='", "'!='", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'print'", "'input'", 
                     "'when'", "'if'", "'else'", "<INVALID>", "<INVALID>", 
                     "'return'", "'loop'", "'repeat'", "'for'", "'next'", 
                     "'break'", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "COMMENT", "FID", "TK_NUM", "OPERATION", 
                      "PRINT", "INPUT", "WHEN", "IF", "ELSE", "CICLE", "CICLE2", 
                      "RETURN", "LOOP", "REPEAT", "FOR", "NEXT", "BREAK", 
                      "AND", "OR", "NOT", "TK_BOOL", "DATATYPE", "ID" ]

    RULE_prog = 0
    RULE_f = 1
    RULE_main_prog = 2
    RULE_stmt_var_list = 3
    RULE_var_dec = 4
    RULE_stmt_block = 5
    RULE_stmt = 6
    RULE_assignation = 7
    RULE_do_block = 8
    RULE_par_lexpr = 9
    RULE_lexpr = 10
    RULE_nexpr = 11
    RULE_rexpr = 12
    RULE_simple_expr = 13
    RULE_term = 14
    RULE_factor = 15

    ruleNames =  [ "prog", "f", "main_prog", "stmt_var_list", "var_dec", 
                   "stmt_block", "stmt", "assignation", "do_block", "par_lexpr", 
                   "lexpr", "nexpr", "rexpr", "simple_expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    WS=25
    COMMENT=26
    FID=27
    TK_NUM=28
    OPERATION=29
    PRINT=30
    INPUT=31
    WHEN=32
    IF=33
    ELSE=34
    CICLE=35
    CICLE2=36
    RETURN=37
    LOOP=38
    REPEAT=39
    FOR=40
    NEXT=41
    BREAK=42
    AND=43
    OR=44
    NOT=45
    TK_BOOL=46
    DATATYPE=47
    ID=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_prog(self):
            return self.getTypedRuleContext(BCCParser.Main_progContext,0)


        def f(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.FContext)
            else:
                return self.getTypedRuleContext(BCCParser.FContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = BCCParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__0:
                self.state = 32
                self.f()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.main_prog()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FID(self):
            return self.getToken(BCCParser.FID, 0)

        def DATATYPE(self):
            return self.getToken(BCCParser.DATATYPE, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(BCCParser.Stmt_blockContext,0)


        def var_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.Var_decContext)
            else:
                return self.getTypedRuleContext(BCCParser.Var_decContext,i)


        def stmt_var_list(self):
            return self.getTypedRuleContext(BCCParser.Stmt_var_listContext,0)


        def getRuleIndex(self):
            return BCCParser.RULE_f

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF" ):
                return visitor.visitF(self)
            else:
                return visitor.visitChildren(self)




    def f(self):

        localctx = BCCParser.FContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_f)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(BCCParser.T__0)
            self.state = 41
            self.match(BCCParser.FID)
            self.state = 42
            self.match(BCCParser.T__1)
            self.state = 43
            self.match(BCCParser.DATATYPE)
            self.state = 44
            self.match(BCCParser.T__2)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BCCParser.ID:
                self.state = 45
                self.var_dec()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BCCParser.T__3:
                    self.state = 46
                    self.match(BCCParser.T__3)
                    self.state = 47
                    self.var_dec()
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 55
            self.match(BCCParser.T__4)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BCCParser.T__6:
                self.state = 56
                self.stmt_var_list()


            self.state = 59
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_progContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_list(self):
            return self.getTypedRuleContext(BCCParser.Stmt_var_listContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.StmtContext)
            else:
                return self.getTypedRuleContext(BCCParser.StmtContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_main_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_prog" ):
                return visitor.visitMain_prog(self)
            else:
                return visitor.visitChildren(self)




    def main_prog(self):

        localctx = BCCParser.Main_progContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BCCParser.T__6:
                self.state = 61
                self.stmt_var_list()


            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__10) | (1 << BCCParser.T__11) | (1 << BCCParser.T__12) | (1 << BCCParser.PRINT) | (1 << BCCParser.INPUT) | (1 << BCCParser.WHEN) | (1 << BCCParser.IF) | (1 << BCCParser.CICLE) | (1 << BCCParser.RETURN) | (1 << BCCParser.LOOP) | (1 << BCCParser.REPEAT) | (1 << BCCParser.FOR) | (1 << BCCParser.NEXT) | (1 << BCCParser.BREAK) | (1 << BCCParser.ID))) != 0):
                self.state = 64
                self.stmt()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(BCCParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.Var_decContext)
            else:
                return self.getTypedRuleContext(BCCParser.Var_decContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_stmt_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_list" ):
                return visitor.visitStmt_var_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_list(self):

        localctx = BCCParser.Stmt_var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(BCCParser.T__6)
            self.state = 73
            self.var_dec()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__3:
                self.state = 74
                self.match(BCCParser.T__3)
                self.state = 75
                self.var_dec()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(BCCParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BCCParser.ID, 0)

        def DATATYPE(self):
            return self.getToken(BCCParser.DATATYPE, 0)

        def getRuleIndex(self):
            return BCCParser.RULE_var_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dec" ):
                return visitor.visitVar_dec(self)
            else:
                return visitor.visitChildren(self)




    def var_dec(self):

        localctx = BCCParser.Var_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(BCCParser.ID)
            self.state = 84
            self.match(BCCParser.T__1)
            self.state = 85
            self.match(BCCParser.DATATYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.StmtContext)
            else:
                return self.getTypedRuleContext(BCCParser.StmtContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_stmt_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = BCCParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt_block)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(BCCParser.T__8)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__10) | (1 << BCCParser.T__11) | (1 << BCCParser.T__12) | (1 << BCCParser.PRINT) | (1 << BCCParser.INPUT) | (1 << BCCParser.WHEN) | (1 << BCCParser.IF) | (1 << BCCParser.CICLE) | (1 << BCCParser.RETURN) | (1 << BCCParser.LOOP) | (1 << BCCParser.REPEAT) | (1 << BCCParser.FOR) | (1 << BCCParser.NEXT) | (1 << BCCParser.BREAK) | (1 << BCCParser.ID))) != 0):
                    self.state = 88
                    self.stmt()
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 94
                self.match(BCCParser.T__9)
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11, BCCParser.T__12, BCCParser.PRINT, BCCParser.INPUT, BCCParser.WHEN, BCCParser.IF, BCCParser.CICLE, BCCParser.RETURN, BCCParser.LOOP, BCCParser.REPEAT, BCCParser.FOR, BCCParser.NEXT, BCCParser.BREAK, BCCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(BCCParser.PRINT, 0)

        def lexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.LexprContext)
            else:
                return self.getTypedRuleContext(BCCParser.LexprContext,i)


        def INPUT(self):
            return self.getToken(BCCParser.INPUT, 0)

        def ID(self):
            return self.getToken(BCCParser.ID, 0)

        def WHEN(self):
            return self.getToken(BCCParser.WHEN, 0)

        def par_lexpr(self):
            return self.getTypedRuleContext(BCCParser.Par_lexprContext,0)


        def do_block(self):
            return self.getTypedRuleContext(BCCParser.Do_blockContext,0)


        def IF(self):
            return self.getToken(BCCParser.IF, 0)

        def ELSE(self):
            return self.getToken(BCCParser.ELSE, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(BCCParser.Stmt_blockContext,0)


        def CICLE(self):
            return self.getToken(BCCParser.CICLE, 0)

        def CICLE2(self):
            return self.getToken(BCCParser.CICLE2, 0)

        def RETURN(self):
            return self.getToken(BCCParser.RETURN, 0)

        def LOOP(self):
            return self.getToken(BCCParser.LOOP, 0)

        def REPEAT(self):
            return self.getToken(BCCParser.REPEAT, 0)

        def TK_NUM(self):
            return self.getToken(BCCParser.TK_NUM, 0)

        def FOR(self):
            return self.getToken(BCCParser.FOR, 0)

        def assignation(self):
            return self.getTypedRuleContext(BCCParser.AssignationContext,0)


        def NEXT(self):
            return self.getToken(BCCParser.NEXT, 0)

        def BREAK(self):
            return self.getToken(BCCParser.BREAK, 0)

        def getRuleIndex(self):
            return BCCParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BCCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmt)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(BCCParser.PRINT)
                self.state = 99
                self.lexpr()
                self.state = 100
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.INPUT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(BCCParser.INPUT)
                self.state = 103
                self.match(BCCParser.ID)
                self.state = 104
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.WHEN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.match(BCCParser.WHEN)
                self.state = 106
                self.par_lexpr()
                self.state = 107
                self.do_block()
                pass
            elif token in [BCCParser.IF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 109
                self.match(BCCParser.IF)
                self.state = 110
                self.par_lexpr()
                self.state = 111
                self.do_block()
                self.state = 112
                self.match(BCCParser.ELSE)
                self.state = 113
                self.stmt_block()
                pass
            elif token in [BCCParser.CICLE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 115
                self.match(BCCParser.CICLE)
                self.state = 116
                self.par_lexpr()
                self.state = 117
                self.do_block()
                pass
            elif token in [BCCParser.T__12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 119
                self.do_block()
                self.state = 120
                self.match(BCCParser.CICLE2)
                self.state = 121
                self.par_lexpr()
                pass
            elif token in [BCCParser.RETURN]:
                self.enterOuterAlt(localctx, 7)
                self.state = 123
                self.match(BCCParser.RETURN)
                self.state = 124
                self.lexpr()
                self.state = 125
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.LOOP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 127
                self.match(BCCParser.LOOP)
                self.state = 128
                self.stmt_block()
                pass
            elif token in [BCCParser.REPEAT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 129
                self.match(BCCParser.REPEAT)
                self.state = 130
                self.match(BCCParser.TK_NUM)
                self.state = 131
                self.match(BCCParser.T__1)
                self.state = 132
                self.stmt_block()
                pass
            elif token in [BCCParser.FOR]:
                self.enterOuterAlt(localctx, 10)
                self.state = 133
                self.match(BCCParser.FOR)
                self.state = 134
                self.match(BCCParser.T__2)
                self.state = 135
                self.lexpr()
                self.state = 136
                self.match(BCCParser.T__7)
                self.state = 137
                self.lexpr()
                self.state = 138
                self.match(BCCParser.T__7)
                self.state = 139
                self.assignation()
                self.state = 140
                self.match(BCCParser.T__4)
                self.state = 141
                self.do_block()
                pass
            elif token in [BCCParser.NEXT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 143
                self.match(BCCParser.NEXT)
                self.state = 144
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.BREAK]:
                self.enterOuterAlt(localctx, 12)
                self.state = 145
                self.match(BCCParser.BREAK)
                self.state = 146
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11, BCCParser.ID]:
                self.enterOuterAlt(localctx, 13)
                self.state = 147
                self.assignation()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BCCParser.ID, 0)

        def OPERATION(self):
            return self.getToken(BCCParser.OPERATION, 0)

        def lexpr(self):
            return self.getTypedRuleContext(BCCParser.LexprContext,0)


        def getRuleIndex(self):
            return BCCParser.RULE_assignation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignation" ):
                return visitor.visitAssignation(self)
            else:
                return visitor.visitChildren(self)




    def assignation(self):

        localctx = BCCParser.AssignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignation)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(BCCParser.ID)
                self.state = 154
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BCCParser.OPERATION]:
                    self.state = 151
                    self.match(BCCParser.OPERATION)
                    self.state = 152
                    self.lexpr()
                    pass
                elif token in [BCCParser.T__10, BCCParser.T__11]:
                    self.state = 153
                    _la = self._input.LA(1)
                    if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 156
                self.match(BCCParser.T__7)
                pass
            elif token in [BCCParser.T__10, BCCParser.T__11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 158
                self.match(BCCParser.ID)
                self.state = 159
                self.match(BCCParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_block(self):
            return self.getTypedRuleContext(BCCParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return BCCParser.RULE_do_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_block" ):
                return visitor.visitDo_block(self)
            else:
                return visitor.visitChildren(self)




    def do_block(self):

        localctx = BCCParser.Do_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_do_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(BCCParser.T__12)
            self.state = 163
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Par_lexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexpr(self):
            return self.getTypedRuleContext(BCCParser.LexprContext,0)


        def getRuleIndex(self):
            return BCCParser.RULE_par_lexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar_lexpr" ):
                return visitor.visitPar_lexpr(self)
            else:
                return visitor.visitChildren(self)




    def par_lexpr(self):

        localctx = BCCParser.Par_lexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_par_lexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(BCCParser.T__2)
            self.state = 166
            self.lexpr()
            self.state = 167
            self.match(BCCParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.NexprContext)
            else:
                return self.getTypedRuleContext(BCCParser.NexprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(BCCParser.AND)
            else:
                return self.getToken(BCCParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(BCCParser.OR)
            else:
                return self.getToken(BCCParser.OR, i)

        def getRuleIndex(self):
            return BCCParser.RULE_lexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexpr" ):
                return visitor.visitLexpr(self)
            else:
                return visitor.visitChildren(self)




    def lexpr(self):

        localctx = BCCParser.LexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_lexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.nexpr()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.AND or _la==BCCParser.OR:
                self.state = 174
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BCCParser.AND]:
                    self.state = 170
                    self.match(BCCParser.AND)
                    self.state = 171
                    self.nexpr()
                    pass
                elif token in [BCCParser.OR]:
                    self.state = 172
                    self.match(BCCParser.OR)
                    self.state = 173
                    self.nexpr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BCCParser.NOT, 0)

        def lexpr(self):
            return self.getTypedRuleContext(BCCParser.LexprContext,0)


        def rexpr(self):
            return self.getTypedRuleContext(BCCParser.RexprContext,0)


        def getRuleIndex(self):
            return BCCParser.RULE_nexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNexpr" ):
                return visitor.visitNexpr(self)
            else:
                return visitor.visitChildren(self)




    def nexpr(self):

        localctx = BCCParser.NexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_nexpr)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BCCParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(BCCParser.NOT)
                self.state = 180
                self.match(BCCParser.T__2)
                self.state = 181
                self.lexpr()
                self.state = 182
                self.match(BCCParser.T__4)
                pass
            elif token in [BCCParser.T__2, BCCParser.T__10, BCCParser.T__11, BCCParser.FID, BCCParser.TK_NUM, BCCParser.TK_BOOL, BCCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.rexpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.Simple_exprContext)
            else:
                return self.getTypedRuleContext(BCCParser.Simple_exprContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_rexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRexpr" ):
                return visitor.visitRexpr(self)
            else:
                return visitor.visitChildren(self)




    def rexpr(self):

        localctx = BCCParser.RexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_rexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.simple_expr()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__13) | (1 << BCCParser.T__14) | (1 << BCCParser.T__15) | (1 << BCCParser.T__16) | (1 << BCCParser.T__17) | (1 << BCCParser.T__18))) != 0):
                self.state = 188
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__13) | (1 << BCCParser.T__14) | (1 << BCCParser.T__15) | (1 << BCCParser.T__16) | (1 << BCCParser.T__17) | (1 << BCCParser.T__18))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 189
                self.simple_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.TermContext)
            else:
                return self.getTypedRuleContext(BCCParser.TermContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_simple_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_expr" ):
                return visitor.visitSimple_expr(self)
            else:
                return visitor.visitChildren(self)




    def simple_expr(self):

        localctx = BCCParser.Simple_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_simple_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.term()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BCCParser.T__19 or _la==BCCParser.T__20:
                self.state = 193
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__19 or _la==BCCParser.T__20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 194
                self.term()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.FactorContext)
            else:
                return self.getTypedRuleContext(BCCParser.FactorContext,i)


        def getRuleIndex(self):
            return BCCParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = BCCParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.factor()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__21) | (1 << BCCParser.T__22) | (1 << BCCParser.T__23))) != 0):
                self.state = 201
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__21) | (1 << BCCParser.T__22) | (1 << BCCParser.T__23))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 202
                self.factor()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_NUM(self):
            return self.getToken(BCCParser.TK_NUM, 0)

        def TK_BOOL(self):
            return self.getToken(BCCParser.TK_BOOL, 0)

        def ID(self):
            return self.getToken(BCCParser.ID, 0)

        def lexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BCCParser.LexprContext)
            else:
                return self.getTypedRuleContext(BCCParser.LexprContext,i)


        def FID(self):
            return self.getToken(BCCParser.FID, 0)

        def getRuleIndex(self):
            return BCCParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = BCCParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(BCCParser.TK_NUM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.match(BCCParser.TK_BOOL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.match(BCCParser.ID)
                self.state = 211
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                _la = self._input.LA(1)
                if not(_la==BCCParser.T__10 or _la==BCCParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 213
                self.match(BCCParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 214
                self.match(BCCParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 215
                self.match(BCCParser.T__2)
                self.state = 216
                self.lexpr()
                self.state = 217
                self.match(BCCParser.T__4)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 219
                self.match(BCCParser.FID)
                self.state = 220
                self.match(BCCParser.T__2)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BCCParser.T__2) | (1 << BCCParser.T__10) | (1 << BCCParser.T__11) | (1 << BCCParser.FID) | (1 << BCCParser.TK_NUM) | (1 << BCCParser.NOT) | (1 << BCCParser.TK_BOOL) | (1 << BCCParser.ID))) != 0):
                    self.state = 221
                    self.lexpr()
                    self.state = 226
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==BCCParser.T__3:
                        self.state = 222
                        self.match(BCCParser.T__3)
                        self.state = 223
                        self.lexpr()
                        self.state = 228
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 231
                self.match(BCCParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





