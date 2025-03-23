def tokenize(s):
    tokens, i = [], 0
    while i < len(s):
        if s[i].isspace(): i += 1
        elif s[i].isdigit(): 
            start = i
            while i < len(s) and s[i].isdigit(): i += 1
            tokens.append(("NUM", s[start:i]))
        elif s[i] in "+-*/()":
            tokens.append((s[i], s[i]))
            i += 1
        else: return None
    return tokens

class Parser:
    def __init__(self, tokens): self.t, self.p, self.rules = tokens, 0, []
    def cur(self): return self.t[self.p][0] if self.p < len(self.t) else None
    def eat(self, val=None):
        if self.cur() is None: raise Exception()
        if val and self.cur() != val: raise Exception()
        self.p += 1

    def parseE(self):
        self.rules.append(1)
        self.parseT()
        self.parseE1()

    def parseE1(self):
        if self.cur() == '+':
            self.rules.append(2)
            self.eat('+')
            self.parseT()
            self.parseE1()
        elif self.cur() == '-':
            self.rules.append(3)
            self.eat('-')
            self.parseT()
            self.parseE1()
        else: self.rules.append(4)

    def parseT(self):
        self.rules.append(5)
        self.parseF()
        self.parseT1()

    def parseT1(self):
        if self.cur() == '*':
            self.rules.append(6)
            self.eat('*')
            self.parseF()
            self.parseT1()
        elif self.cur() == '/':
            self.rules.append(7)
            self.eat('/')
            self.parseF()
            self.parseT1()
        else: self.rules.append(8)

    def parseF(self):
        if self.cur() == '(':
            self.rules.append(9)
            self.eat('(')
            self.parseE()
            if self.cur() != ')': raise Exception()
            self.eat(')')
        elif self.cur() == 'NUM':
            self.rules.append(10)
            self.eat('NUM')
        else: raise Exception()

def main():
    N = int(input())
    for _ in range(N):
        line = input().strip()
        tok = tokenize(line)
        if not tok:
            print("ERROR")
            continue
        p = Parser(tok)
        try:
            p.parseE()
            if p.p != len(tok): raise Exception()
            print(" ".join(map(str, p.rules)))
        except: print("ERROR")

if __name__ == "__main__": main()