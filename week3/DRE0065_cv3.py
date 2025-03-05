def parse_grammar(text):
    g = {}
    for line in text.splitlines():
        line = line.strip()
        if not line: continue
        if line.startswith("{") and line.endswith("}") and ":" not in line: continue
        c, s = line.find(":"), line.rfind(";")
        if c == -1 or s == -1: continue
        head = line[:c].strip()[0]
        body = line[c+1:s].strip()
        prods = [alt.strip().split() for alt in body.split("|") if alt.strip()]
        g[head] = prods
    return g

def compute_nullable(g):
    n = {nt: False for nt in g}
    changed = True
    while changed:
        changed = False
        for nt, prods in g.items():
            if n[nt]: continue
            for p in prods:
                if len(p) == 1 and p[0] == "{e}": n[nt] = True; changed = True; break
                all_null = True
                for s in p:
                    if s == "{e}": continue
                    if s.isupper():
                        if not n.get(s, False): all_null = False; break
                    else: all_null = False; break
                if all_null: n[nt] = True; changed = True; break
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
                    if s == "{e}": res.add("{e}"); break
                    elif s.islower(): res.add(s); break
                    elif s.isupper():
                        res |= (f[s] - {"{e}"})
                        if "{e}" not in f[s]: break
                else: res.add("{e}")
                if res - f[nt]: f[nt] |= res; changed = True
    return f

def first_prod(p, f):
    res = set()
    for s in p:
        if s == "{e}": res.add("{e}"); break
        elif s.islower(): res.add(s); break
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
                        elif ns.islower(): beta.add(ns); break
                        elif ns.isupper():
                            beta |= (f[ns] - {"{e}"})
                            if "{e}" not in f[ns]: break
                    before = len(fol[s])
                    fol[s] |= beta
                    else_nullable = True
                    for ns in p[i+1:]:
                        if ns.islower() or (ns.isupper() and "{e}" not in f[ns]): else_nullable = False; break
                    if else_nullable: fol[s] |= fol[nt]
                    if len(fol[s]) > before: changed = True
    return fol

def main():
    lines = []
    blank = 0
    while True:
        l = input()
        if l.strip() == "":
            blank += 1
            if blank >= 2: break
        else: blank = 0
        lines.append(l)
    text = "\n".join(lines)
    g = parse_grammar(text)
    if not g:
        print("Grammar not found.")
        return
    start = list(g.keys())[0]
    n = compute_nullable(g)
    f = compute_first(g, n)
    fol = compute_follow(g, f, n, start)
    for nt, prods in g.items():
        for p in prods: print("first[{}:{}] = {}".format(nt, "".join(p), " ".join(sorted(first_prod(p, f)))))
    for nt in sorted(g.keys()): print("follow[{}] = {}".format(nt, " ".join(sorted(fol[nt], key=lambda x: (x == "$", x)))))

if __name__ == "__main__": main()