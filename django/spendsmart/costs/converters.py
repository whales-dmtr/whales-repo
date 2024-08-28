class SpecStr:
    """String without underscore, numbers and backspace"""
    regex = r"[A-Za-z\-]+"

    def to_python(self, value):
        return str(value)
    
    def to_url(self, value):
        return str(value)
