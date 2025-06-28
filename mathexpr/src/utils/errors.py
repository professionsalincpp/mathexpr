# Errors 

class MathExprError(Exception):
    """Raised when mathematical error occurs"""
    def __init__(self,message):
        """
        Class for mathematical error
        """
        self.message = message
        
        super().__init__(self.message)

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message

    def __unicode__(self):
        return self.message

class ParserError(MathExprError):
    """Raised when syntax error occurs"""

class LexerError(MathExprError):
    """Raised when lexer error occurs"""
    
class UndefinedIdentifierError(Exception):
    """Raised when undefined identifier is encountered"""

class UnknownBinaryOperatorError(Exception):
    """Raised when unknown binary operator is encountered"""

class UnknownUnaryOperatorError(Exception):
    """Raised when unknown unary operator is encountered"""

class UnsupportedError(Exception):
    """Raised when unsupported operation is encountered"""

