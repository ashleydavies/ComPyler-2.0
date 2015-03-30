__author__ = 'Ashley'

class FileReader():
    """ The FileReader class allows the lexer to quickly request new characters """
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open("{0}.AScript".format(file_name))
        self.throwback_char = False
        self.line_number = 1
        self.char_number = 0
        self.last_char = -1

    def get_char(self):
        if self.throwback_char:
            # If a character was returned we use that instead
            assert self.last_char != -1, "Error in reading file: Failed to access character returned from lexer."
            self.throwback_char = False
            return self.last_char
        else:
            self.last_char = self.file.read(1)
            self.char_number += 1

            if self.last_char == "\n":
                self.increment_line_number()
                self.char_number = 0

            return self.last_char

    def return_char(self):
        self.throwback_char = True

    def get_open(self):
        return not self.file.closed

    def increment_line_number(self):
        self.line_number += 1