__author__ = 'Ashley'
import math
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

    def __init__(self, box_width=32, start=True):
        self.box_width = box_width
        if start:
            self.start()

    def start(self):
        print("/" + (self.box_width * "-") + "\\")

    def line(self, out_text, alignment=Alignment.Left, alignment_padding=1, runon=False):
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

        print("|" + (left_space * " ") + out_text + (right_space * " ") + "|")

    def line_break(self):
        print("|" + (self.box_width * "-") + "|")

    def stop(self):
        print("\\" + (self.box_width * "-") + "/")