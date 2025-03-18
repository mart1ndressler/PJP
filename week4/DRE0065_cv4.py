def parse_grammar(text):
    g = {}
    for line in text.splitlines():
        line = line.strip()
        if not line: continue
        if line.startswith("{") and line.endswith("}") and ":" not in line: continue
        c, s = line.find(":"), line.rfind(";")
        if c == -1 or s == -1: continue
        prods = [alt.strip().split() for alt in line[c+1:s].strip().split("|") if alt.strip()]
        g[line[:c].strip()[0]] = prods
    return g

def compute_nullable(g):
    n = {nt: False for nt in g}
    changed = True
    while changed:
        changed = False
        for nt, prods in g.items():
            if n[nt]: continue
            for p in prods:
                if len(p) == 1 and p[0] == "{e}":
                    n[nt] = True
                    changed = True
                    break
                all_null = True
                for s in p:
                    if s == "{e}": continue
                    if s.isupper():
                        if not n.get(s, False):
                            all_null = False
                            break
                    else:
                        all_null = False
                        break
                if all_null:
                    n[nt] = True
                    changed = True
                    break
    return n

def compute_first(g, n):
    f = {nt: set() for nt in g}
    changed = True
    while changed:
        changed = False
        for nt, prods in g.items():
            for p in prods:
                res = set()
                for s in p:
                    if s == "{e}":
                        res.add("{e}")
                        break
                    elif s.islower():
                        res.add(s)
                        break
                    elif s.isupper():
                        res |= (f[s] - {"{e}"})
                        if "{e}" not in f[s]: break
                else: res.add("{e}")
                before = len(f[nt])
                f[nt] |= res
                if len(f[nt]) > before: changed = True
    return f

def first_prod(p, f):
    res = set()
    for s in p:
        if s == "{e}":
            res.add("{e}")
            break
        elif s.islower():
            res.add(s)
            break
        elif s.isupper():
            res |= (f[s] - {"{e}"})
            if "{e}" not in f[s]: break
    else: res.add("{e}")
    return res

def compute_follow(g, f, n, start):
    fol = {nt: set() for nt in g}
    fol[start].add("$")
    changed = True
    while changed:
        changed = False
        for nt, prods in g.items():
            for p in prods:
                for i, s in enumerate(p):
                    if not s.isupper(): continue
                    beta = set()
                    for ns in p[i+1:]:
                        if ns == "{e}": continue
                        elif ns.islower():
                            beta.add(ns)
                            break
                        elif ns.isupper():
                            beta |= (f[ns] - {"{e}"})
                            if "{e}" not in f[ns]: break
                    before = len(fol[s])
                    fol[s] |= beta
                    else_nullable = True
                    for ns in p[i+1:]:
                        if ns.islower() or (ns.isupper() and "{e}" not in f[ns]):
                            else_nullable = False
                            break
                    if else_nullable: fol[s] |= fol[nt]
                    if len(fol[s]) > before: changed = True
    return fol

def is_ll1(g, f, fol):
    for nt, prods in g.items():
        for i in range(len(prods)):
            for j in range(i+1, len(prods)):
                first_i = first_prod(prods[i], f)
                first_j = first_prod(prods[j], f)
                if (first_i - {"{e}"}) & (first_j - {"{e}"}): return False
                if "{e}" in first_i:
                    if (first_j - {"{e}"}) & fol[nt]: return False
                if "{e}" in first_j:
                    if (first_i - {"{e}"}) & fol[nt]: return False
    return True

def main():
    lines = []
    blank = 0
    while True:
        try:
            l = input()
        except EOFError:
            break
        if l.strip() == "":
            blank += 1
            if blank >= 2: break
        else: blank = 0
        lines.append(l)

    text = "\n".join(lines)
    g = parse_grammar(text)
    if not g:
        print("It is not LL1 grammar")
        return
    start = list(g.keys())[0]
    n = compute_nullable(g)
    f = compute_first(g, n)
    fol = compute_follow(g, f, n, start)

    if is_ll1(g, f, fol): print("It is LL1 grammar")
    else: print("It is not LL1 grammar")

if __name__ == "__main__": main()