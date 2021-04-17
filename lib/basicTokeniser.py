class Token:
    """
    Stores a token type and a value
    """
    def __init__(self, type_, value_):
        self.type = type_
        self.value = value_

    def __repr__(self):
        return f"({self.type}, {self.value})"


class Lexer:
    digits = "1234567890"

    def __init__(self, code):
        self.code = code
        self.ptr = 0
        self.tokens = []

    def analyse(self):
        while self.ptr < len(self.code):
            char = self.code[self.ptr]
            if char in Lexer.digits:  # 1+1
                output = char
                i = self.ptr+1
                while i < len(self.code):
                    if self.code[i] in Lexer.digits:
                        output += self.code[i]
                        i += 1
                    else:
                        break
                self.ptr = i-1
                self.tokens.append(Token("INT", output))
            elif char == "+":
                self.tokens.append(Token("PLUS", None))
            else:
                self.tokens.append(Token("UNKNOWN", char))
            self.ptr += 1
        return self.tokens

    # Make simple data language e.g. x = 5; t = "T"; no = false;
    # Gonna need to rework interpreter (maybe using regex to simplify things)



