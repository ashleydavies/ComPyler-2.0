__author__ = 'Ashley'
from enum import Enum
import sys
import utils
from utils.FancyPrint import FancyPrint


if __name__ == "__main__":
    f_out = FancyPrint(64)
    f_out.line("Loading Compiler", utils.Alignment.Center)
    f_out.line_break()
    f_out.line("Initializing Lexer")
    f_out.line("Initializing Tokenizer")
    f_out.line("Initializing Emitter")
    f_out.line("")
    f_out.line("End")
    f_out.stop()