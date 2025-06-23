# Errors 

class ParserError(Exception):
    """Raised when syntax error occurs"""
    def __init__(self,message):
        """
        Class for syntax error
        """
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message

    def __unicode__(self):
        return self.message

    