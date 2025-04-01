def tokenize(s):
    tokens, i = [], 0
    while i < len(s):
        c = s[i]
        if c.isspace(): i += 1
        elif c.isdigit():
            j = i
            while i < len(s) and s[i].isdigit(): i += 1
            tokens.append(("NUM", int(s[j:i])))
        elif c in "+-*/":
            tokens.append(("OP", c))
            i += 1
        elif c == '(':
            tokens.append(("LPAR", c))
            i += 1
        elif c == ')':
            tokens.append(("RPAR", c))
            i += 1
        else:
            tokens.append(("INVALID", c))
            i += 1
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        
    def cur(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    def eat(self, t=None, v=None):
        token = self.cur()
        if token is None or (t and token[0] != t) or (v and token[1] != v): raise Exception()
        self.pos += 1
        return token

    def E(self):
        val = self.T()
        return self.E1(val)

    def E1(self, val):
        token = self.cur()
        if token and token[0] == "OP" and token[1] in "+-":
            op = token[1]
            self.eat("OP", op)
            t = self.T()
            return self.E1(val + t) if op == '+' else self.E1(val - t)
        return val

    def T(self):
        val = self.F()
        return self.T1(val)

    def T1(self, val):
        token = self.cur()
        if token and token[0] == "OP" and token[1] in "*/":
            op = token[1]
            self.eat("OP", op)
            f = self.F()
            if op == '*': return self.T1(val * f)
            else:
                if f == 0: raise Exception()
                return self.T1(val // f)
        return val

    def F(self):
        token = self.cur()
        if token is None: raise Exception()
        if token[0] == "NUM":
            self.eat("NUM")
            return token[1]
        if token[0] == "LPAR":
            self.eat("LPAR")
            val = self.E()
            self.eat("RPAR")
            return val
        raise Exception()

def main():
    try: n = int(input().strip())
    except:
        print("ERROR")
        return
    for _ in range(n):
        try: expr = input().strip()
        except: break
        try:
            tokens = tokenize(expr)
            if any(t[0] == "INVALID" for t in tokens): raise Exception()
            parser = Parser(tokens)
            result = parser.E()
            if parser.pos != len(tokens): raise Exception()
            print(result)
        except: print("ERROR")

if __name__ == "__main__": main()