
from typing import List
from lexer import Lexer


file = '''
package main

import "core:fmt"

main :: proc() {
    fmt.println("Hello Wolrld!")
}

'''

lex = Lexer(file)

print("PARSING...")
lex.print_text()
print("==========")
result = lex.parse()

if result == False:
    print("Parsing Failed")
else:
    print("Parsing Success")
    for item, i in result:
        try:
            print(f"TOKEN[{i}] '{item.type}' = {item.value}")
        except:
            print(f"### [{i}] IS NOT A TOKEN")
            pass
        
        pass
    pass
