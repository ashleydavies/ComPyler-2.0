__author__ = 'Ashley'
import math
from components.filereader import FileReader
from enum import Enum

class Alignment(Enum):
    Left = 1
    Center = 2
    Right = 3


class FancyPrint:
    @staticmethod
    def quick(out_text, box_width=32):
        f_out = FancyPrint(box_width)
        f_out.line(out_text)
        f_out.stop()

    def __init__(self, box_width=32, left_space=1, start=True):
        self.box_width = box_width
        self.left_space = left_space
        if start:
            self.start()

    def start(self):
        print((" " * self.left_space) + "╔" + (self.box_width * "═") + "╗")

    def error(self, file_reader: FileReader, error_content):
        error_content = "Error [{0}, {1}]> {2}".format(file_reader.line_number, file_reader.char_number, error_content)
        self.line(error_content)
        self.stop()
        exit()

    def line(self, out_text, alignment=Alignment.Left, alignment_padding=1, runon=False):
        out_text = str(out_text)
        local_alignment_padding = alignment_padding

        if runon:
            local_alignment_padding += 2

        if len(out_text) > self.box_width - local_alignment_padding:
            end_char = self.box_width - local_alignment_padding
            self.line(out_text[:end_char], alignment, alignment_padding, runon)
            self.line(out_text[end_char:], alignment, alignment_padding, True)
            return

        space = (self.box_width - len(out_text)) / 2
        left_space = math.floor(space)
        right_space = math.ceil(space)

        if alignment == Alignment.Left:
            right_space += left_space - local_alignment_padding
            left_space = local_alignment_padding
        elif alignment == Alignment.Right:
            left_space += right_space - local_alignment_padding
            right_space = local_alignment_padding

        print((" " * self.left_space) + "║" + (left_space * " ") + out_text + (right_space * " ") + "║")

    def line_break(self):
        print((" " * self.left_space) + "╠" + (self.box_width * "═") + "╣")

    def stop(self):
        print((" " * self.left_space) + "╚" + (self.box_width * "═") + "╝")