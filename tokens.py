TOKEN_PATTERNS = {
    'RESERVED': r'\b(int|float|if|else|while|print)\b',
    'NUMBER': r'\b\d+(\.\d+)?\b',
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'OPERATOR': r'[+\-*/=<>]+',
    'PAREN': r'[()]',
    'BRACE': r'[{}]',
    'SEMICOLON': r';'
}