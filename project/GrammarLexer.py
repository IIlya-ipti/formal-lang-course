# Generated from project/Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,31,200,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,0,1,0,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,
        1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,25,1,25,
        1,25,1,26,1,26,1,26,1,26,1,27,4,27,174,8,27,11,27,12,27,175,1,27,
        1,27,1,28,1,28,5,28,182,8,28,10,28,12,28,185,9,28,1,29,1,29,1,29,
        5,29,190,8,29,10,29,12,29,193,9,29,3,29,195,8,29,1,30,1,30,1,30,
        1,30,0,0,31,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,
        23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,
        45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,1,0,5,3,0,
        9,10,13,13,32,32,1,0,97,122,2,0,48,57,97,122,1,0,49,57,1,0,48,57,
        203,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,
        0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,
        0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,
        0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,
        0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,
        0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,
        0,61,1,0,0,0,1,63,1,0,0,0,3,67,1,0,0,0,5,70,1,0,0,0,7,76,1,0,0,0,
        9,78,1,0,0,0,11,85,1,0,0,0,13,92,1,0,0,0,15,97,1,0,0,0,17,106,1,
        0,0,0,19,111,1,0,0,0,21,115,1,0,0,0,23,118,1,0,0,0,25,120,1,0,0,
        0,27,122,1,0,0,0,29,124,1,0,0,0,31,126,1,0,0,0,33,128,1,0,0,0,35,
        130,1,0,0,0,37,132,1,0,0,0,39,134,1,0,0,0,41,136,1,0,0,0,43,139,
        1,0,0,0,45,146,1,0,0,0,47,152,1,0,0,0,49,162,1,0,0,0,51,165,1,0,
        0,0,53,168,1,0,0,0,55,173,1,0,0,0,57,179,1,0,0,0,59,194,1,0,0,0,
        61,196,1,0,0,0,63,64,5,108,0,0,64,65,5,101,0,0,65,66,5,116,0,0,66,
        2,1,0,0,0,67,68,5,105,0,0,68,69,5,115,0,0,69,4,1,0,0,0,70,71,5,103,
        0,0,71,72,5,114,0,0,72,73,5,97,0,0,73,74,5,112,0,0,74,75,5,104,0,
        0,75,6,1,0,0,0,76,77,5,61,0,0,77,8,1,0,0,0,78,79,5,114,0,0,79,80,
        5,101,0,0,80,81,5,109,0,0,81,82,5,111,0,0,82,83,5,118,0,0,83,84,
        5,101,0,0,84,10,1,0,0,0,85,86,5,118,0,0,86,87,5,101,0,0,87,88,5,
        114,0,0,88,89,5,116,0,0,89,90,5,101,0,0,90,91,5,120,0,0,91,12,1,
        0,0,0,92,93,5,101,0,0,93,94,5,100,0,0,94,95,5,103,0,0,95,96,5,101,
        0,0,96,14,1,0,0,0,97,98,5,118,0,0,98,99,5,101,0,0,99,100,5,114,0,
        0,100,101,5,116,0,0,101,102,5,105,0,0,102,103,5,99,0,0,103,104,5,
        101,0,0,104,105,5,115,0,0,105,16,1,0,0,0,106,107,5,102,0,0,107,108,
        5,114,0,0,108,109,5,111,0,0,109,110,5,109,0,0,110,18,1,0,0,0,111,
        112,5,97,0,0,112,113,5,100,0,0,113,114,5,100,0,0,114,20,1,0,0,0,
        115,116,5,116,0,0,116,117,5,111,0,0,117,22,1,0,0,0,118,119,5,91,
        0,0,119,24,1,0,0,0,120,121,5,44,0,0,121,26,1,0,0,0,122,123,5,93,
        0,0,123,28,1,0,0,0,124,125,5,40,0,0,125,30,1,0,0,0,126,127,5,41,
        0,0,127,32,1,0,0,0,128,129,5,124,0,0,129,34,1,0,0,0,130,131,5,94,
        0,0,131,36,1,0,0,0,132,133,5,46,0,0,133,38,1,0,0,0,134,135,5,38,
        0,0,135,40,1,0,0,0,136,137,5,46,0,0,137,138,5,46,0,0,138,42,1,0,
        0,0,139,140,5,114,0,0,140,141,5,101,0,0,141,142,5,116,0,0,142,143,
        5,117,0,0,143,144,5,114,0,0,144,145,5,110,0,0,145,44,1,0,0,0,146,
        147,5,119,0,0,147,148,5,104,0,0,148,149,5,101,0,0,149,150,5,114,
        0,0,150,151,5,101,0,0,151,46,1,0,0,0,152,153,5,114,0,0,153,154,5,
        101,0,0,154,155,5,97,0,0,155,156,5,99,0,0,156,157,5,104,0,0,157,
        158,5,97,0,0,158,159,5,98,0,0,159,160,5,108,0,0,160,161,5,101,0,
        0,161,48,1,0,0,0,162,163,5,105,0,0,163,164,5,110,0,0,164,50,1,0,
        0,0,165,166,5,98,0,0,166,167,5,121,0,0,167,52,1,0,0,0,168,169,5,
        102,0,0,169,170,5,111,0,0,170,171,5,114,0,0,171,54,1,0,0,0,172,174,
        7,0,0,0,173,172,1,0,0,0,174,175,1,0,0,0,175,173,1,0,0,0,175,176,
        1,0,0,0,176,177,1,0,0,0,177,178,6,27,0,0,178,56,1,0,0,0,179,183,
        7,1,0,0,180,182,7,2,0,0,181,180,1,0,0,0,182,185,1,0,0,0,183,181,
        1,0,0,0,183,184,1,0,0,0,184,58,1,0,0,0,185,183,1,0,0,0,186,195,5,
        48,0,0,187,191,7,3,0,0,188,190,7,4,0,0,189,188,1,0,0,0,190,193,1,
        0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,195,1,0,0,0,193,191,1,
        0,0,0,194,186,1,0,0,0,194,187,1,0,0,0,195,60,1,0,0,0,196,197,5,34,
        0,0,197,198,7,1,0,0,198,199,5,34,0,0,199,62,1,0,0,0,5,0,175,183,
        191,194,1,6,0,0
    ]

class GrammarLexer(Lexer):

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
    WS = 28
    VAR = 29
    NUM = 30
    CHAR = 31

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'let'", "'is'", "'graph'", "'='", "'remove'", "'vertex'", "'edge'", 
            "'vertices'", "'from'", "'add'", "'to'", "'['", "','", "']'", 
            "'('", "')'", "'|'", "'^'", "'.'", "'&'", "'..'", "'return'", 
            "'where'", "'reachable'", "'in'", "'by'", "'for'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "VAR", "NUM", "CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "WS", "VAR", "NUM", "CHAR" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


