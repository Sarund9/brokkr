

from enum import Enum
from typing import List

class TokenType(Enum):
    UNKNOWN = 0
    NAME = 1
    NUM = 2

class Token:
    type : TokenType = 0
    value : any


class Lexer:
    
    text : str
    
    def __init__(self, text:str):
        self.text = text
        pass

    def print_text(self):
        print(self.text)

    class CharType(Enum):
        IGNORE = 0
        

    def parse(self) -> List:
        list = []
        
        # ci is Char Index
        ci = 0
        while ci < self.text.len():
            
            
            ci += 1
            pass
        
        return list
