import re
from tokens import TOKEN_PATTERNS

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        pattern = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_PATTERNS.items())
        
        for match in re.finditer(pattern, self.code):
            token_type = match.lastgroup
            value = match.group(token_type).strip()

            if value:
                self.tokens.append((token_type, value))

        return self.tokens