class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def match(self, expected_type):
        """Verifica se o próximo token corresponde ao esperado e avança se for o caso."""
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            self.pos += 1
            return True
        return False

    def parse(self):
        """Inicia a análise sintática percorrendo os tokens e validando as construções."""
        while self.pos < len(self.tokens):
            if not self.parse_statement():
                raise SyntaxError(f"Erro de sintaxe! Problema em {self.tokens[self.pos]}")

    def parse_statement(self):
        """Analisa diferentes tipos de comandos da linguagem"""
        if self.match('RESERVED'):
            token_value = self.tokens[self.pos - 1][1]
            if token_value in ('int', 'float'):
                return self.parse_variable_declaration()
            elif token_value == 'if':
                return self.parse_if_statement()
            elif token_value == 'while':
                return self.parse_while_statement()
            elif token_value == 'print':
                return self.parse_print_statement()
        
        if self.match('IDENTIFIER') and self.match('OPERATOR') and self.tokens[self.pos - 1][1] == '=':
            return self.parse_assignment()  

        return False

    def parse_assignment(self):
        """Analisa expressões de atribuição como x = x - 1;"""
        if not self.match('IDENTIFIER'):  
            return False

        if not self.match('OPERATOR') and self.tokens[self.pos - 1][1] in ('+', '-', '*', '/'):
            return False

        if not self.match('NUMBER') and not self.match('IDENTIFIER'):  
            return False

        return self.match('SEMICOLON')

    def parse_variable_declaration(self):
        """Analisa declarações de variáveis do tipo int e float, permitindo operações opcionais na atribuição."""
        if not (self.match('IDENTIFIER') and self.match('OPERATOR') and self.match('NUMBER')):
            return False

        while self.match('OPERATOR'):
            if not self.match('NUMBER') and not self.match('IDENTIFIER'):
                return False

        return self.match('SEMICOLON')

    def parse_if_statement(self):
        """Analisa declarações `if`, verificando a condição e o bloco de código."""
        if not (self.match('PAREN') and 
                self.match('IDENTIFIER') and 
                self.match('OPERATOR') and 
                self.match('NUMBER') and 
                self.match('PAREN') and 
                self.match('BRACE') and 
                self.parse_block() and 
                self.match('BRACE')):
            return False

        if self.match('RESERVED') and self.tokens[self.pos - 1][1] == 'else':
            return self.parse_else_statement()
        
        return True

    def parse_while_statement(self):
        """Analisa loops while corretamente"""
        if not (self.match('PAREN') and self.parse_condition() and self.match('PAREN')):  
            return False

        if not self.match('BRACE'):  
            return False

        while not self.match('BRACE'):
            if not self.parse_statement():
                return False

        return True

    def parse_else_statement(self):
        """Analisa o bloco `else`, garantindo que haja um bloco de código válido."""
        return self.match('BRACE') and self.parse_block() and self.match('BRACE')

    def parse_print_statement(self):
        """Analisa o comando `print`, garantindo a presença de parênteses e identificador."""
        return (self.match('PAREN') and 
                self.match('IDENTIFIER') and 
                self.match('PAREN') and 
                self.match('SEMICOLON'))

    def parse_condition(self):
        """Analisa condições booleanas dentro de if e while"""
        return (self.match('IDENTIFIER') and 
                self.match('OPERATOR') and 
                self.match('NUMBER') or self.match('IDENTIFIER'))

    def parse_block(self):
        """Analisa um bloco de código entre `{}` contendo múltiplas declarações."""
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] != 'BRACE':
            if not self.parse_statement():
                return False
        return True