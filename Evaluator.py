import math

class Evaluator:
    def __init__(self):
        pass

    def parse(self, expression, variables):
        class Parser:
            def __init__(self, expression, variables):
                self.expression = expression
                self.variables = variables
                self.pos = -1
                self.ch = None   

            def custom_round(self, number, decimal_places):
                factor = 10 ** decimal_places
                return round(number * factor) / factor

            def next_char(self):
                self.pos += 1
                self.ch = self.expression[self.pos] if self.pos < len(self.expression) else None
                
            def eat(self, char_to_eat):
                while self.ch == ' ':
                    self.next_char()
                if self.ch == char_to_eat:
                    self.next_char()
                    return True
                return False
            
            '''
            Beginning of the parsing algorithm
            '''
            def begin_parse(self):
                self.next_char()
                x = self.parse_expression()
                if self.pos < len(self.expression):
                    raise RuntimeError(f"Unexpected: {self.ch}")
                return x
            
            '''
            Addition and Subtraction Operations
            '''
            def parse_expression(self):
                x = self.parse_term()
                while True:
                    if self.eat('+'):
                        a = x
                        b = self.parse_term()
                        x = lambda a=a, b=b: a() + b()
                    elif self.eat('-'):
                        a = x
                        b = self.parse_term()
                        x = lambda a=a, b=b: a() - b()
                    else:
                        return x
            
            '''
            Multiplication, Division, and Modulo Operations
            '''    
            def parse_term(self):
                x = self.parse_factor()
                while True:
                    if self.eat('*'):
                        a = x
                        b = self.parse_factor()
                        x = lambda a=a, b=b: a() * b()
                    elif self.eat('/'):
                        a = x
                        b = self.parse_factor()
                        x = lambda a=a, b=b: a() / b()
                    elif self.eat('%'):
                        a = x
                        b = self.parse_factor()
                        x = lambda a=a, b=b: a() % b()
                    else:
                        return x
                    
            '''
            Unary +, -
            Operand and Variable processing
            Named Functions
            '''
            def parse_factor(self):
                if self.eat('+'): return self.parse_factor()
                if self.eat('-'):
                    x = self.parse_factor()
                    return lambda x=x: -x

                # Parsing operands
                x = -1
                startPos = self.pos
                if (self.eat('(')):
                    x = self.parse_expression()
                    if self.eat(')') == False: raise RuntimeError("Missing ')'")
                elif self.ch is not None and self.ch >= '0' and self.ch <= '9' or self.ch == '.':
                    while self.ch is not None and self.ch >= '0' and self.ch <= '9' or self.ch == '.': 
                        self.next_char()
                    value = float(self.expression[startPos : self.pos])
                    x = lambda: value
                
                # Parsing functions
                elif self.ch >= 'a' and self.ch <= 'z':
                    while self.ch is not None and self.ch >= 'a' and self.ch <= 'z' or self.ch == '1' or self.ch == '0':
                        self.next_char()
                    token = self.expression[startPos : self.pos]
                    if (self.eat('(')):
                        x = self.parse_expression()
                        x = self.get_function_expression(token, x)
                        if self.eat(')') == False: raise RuntimeError("Missing ')' after argument to " + token)
                    
                    # Variable
                    else:
                        if token == 'e':
                            x = lambda: math.e
                        else:
                            x = lambda token=token: self.variables.get(token, 0.0)
                
                # Unknown Character
                else:
                    raise RuntimeError(f"Unexpected: {self.ch}")
                    
                # Exponent
                if self.eat('^'):
                    a = x
                    b = self.parse_factor()
                    x = lambda a=a, b=b: math.pow(a(), b())
                
                return x
            
            
            '''
            Named Expression Lambdas
            '''
            # All named functions supported
            def get_function_expression(self, func, x):
                if func == 'sqrt':
                    return lambda x=x: math.sqrt(x())
                elif func == 'sin':
                    return lambda x=x: math.sin(math.radians(x()))
                elif func == 'cos':
                    return lambda x=x: math.cos(math.radians(x()))
                elif func == 'tan':
                    return lambda x=x: math.tan(math.radians(x()))
                elif func == 'round':
                    if self.eat(','):
                        a = x
                        b = self.parse_factor()
                        return lambda a=a, b=b: self.custom_round(a(), int(b()))
                    else:
                        raise RuntimeError("Missing second argument for round function")
                elif func == 'sqr':
                    return lambda x=x: math.pow(x(), 2.0)
                elif func == 'exp':
                    return lambda x=x: math.pow(math.e, x())
                elif func == 'ln':
                    return lambda x=x: math.log(x())
                elif func == 'log10':
                    return lambda x=x: math.log10(x())
                elif func == 'abs':
                    return lambda x=x: abs(x())
                elif func == 'neg':
                    return lambda x=x: -x()
                
                else:
                    raise RuntimeError(f"Unknown function: {func}")
                
            
        # Instantiate Parser and parse the expression
        parser_instance = Parser(expression, variables)
        result = parser_instance.begin_parse()
        return result()
