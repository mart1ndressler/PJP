def tokenize(text):
    text = "\n".join(line.split("//")[0] for line in text.split("\n"))
    tokens, i = [], 0
    token_types = {"+": "OP", "-": "OP", "*": "OP", "/": "OP", "(": "LPAR", ")": "RPAR", ";": "SEMICOLON"}

    while i < len(text):
        char = text[i]
        
        if char in " \t\n":
            i += 1
            continue
        if char.isdigit():
            start = i
            while i < len(text) and text[i].isdigit(): i += 1
            tokens.append(("NUM", text[start:i]))
            continue
        if char.isalpha():
            start = i
            while i < len(text) and text[i].isalnum(): i += 1
            word = text[start:i]
            tokens.append((word.upper() if word in {"div", "mod"} else "ID", None if word in {"div", "mod"} else word))
            continue
        if char in token_types:
            tokens.append((token_types[char], char if token_types[char] == "OP" else None))
            i += 1
            continue
        
        tokens.append(("OTHERS", char))
        i += 1
    return tokens

def main():
    input_text = ""
    while True:
        line = input()
        if not line: break
        input_text += line + "\n"
    for token in tokenize(input_text): print(f"{token[0]}:{token[1]}" if token[1] else token[0])
    
if __name__ == "__main__": main()