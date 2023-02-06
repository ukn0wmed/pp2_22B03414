class InputOutputString:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())


string_io = InputOutputString()
string_io.get_string()
string_io.print_string()