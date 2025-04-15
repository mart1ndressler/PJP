def main():
    import sys

    lines, blank_count = [], 0
    while True:
        try: line = input()
        except EOFError: break
        if line.strip() == "":
            blank_count += 1
            if blank_count >= 2: break
            continue
        else:
            blank_count = 0
            lines.append(line)
    
    data = "\n".join(lines).strip()
    if not data: return

    stack, memory = [], {}
    for line in data.splitlines():
        line = line.strip()
        if not line: continue
        parts = line.split()
        instr = parts[0]

        if instr == "PUSH":
            if len(parts) != 3: raise Exception("Invalid PUSH instruction format.")
            val_type = parts[1]
            n = parts[2]
            if val_type == "I": stack.append((int(n), "I"))
            elif val_type == "F": stack.append((float(n), "F"))
            else: raise Exception("Unknown type in PUSH instruction.")
        elif instr == "LOAD":
            if len(parts) != 2: raise Exception("Invalid LOAD instruction format.")
            var = parts[1]
            if var not in memory: raise Exception(f"Variable '{var}' is not declared.")
            stack.append(memory[var])
        elif instr == "SAVE":
            if len(parts) == 3:
                target_type = parts[1]
                var = parts[2]
            elif len(parts) == 2:
                var = parts[1]
                if var in memory: target_type = memory[var][1]
                else:
                    if not stack: raise Exception("Stack underflow on SAVE.")
                    value, current_type = stack[-1]
                    target_type = current_type
            else: raise Exception("Invalid SAVE instruction format.")

            if not stack: raise Exception("Stack underflow on SAVE.")
            value, from_type = stack.pop()
            if target_type == "I": value = int(value)
            elif target_type == "F": value = float(value)
            else: raise Exception("Unknown type in SAVE instruction.")
            memory[var] = (value, target_type)
        elif instr in {"ADD", "SUB", "MUL", "DIV", "MOD"}:
            if len(stack) < 2: raise Exception(f"Stack underflow on {instr}.")
            v2, t2 = stack.pop()
            v1, t1 = stack.pop()
            if instr == "ADD":
                result = (float(v1) + float(v2)) if (t1 == "F" or t2 == "F") else v1 + v2
                stack.append((result, "F" if (t1 == "F" or t2 == "F") else "I"))
            elif instr == "SUB":
                result = (float(v1) - float(v2)) if (t1 == "F" or t2 == "F") else v1 - v2
                stack.append((result, "F" if (t1 == "F" or t2 == "F") else "I"))
            elif instr == "MUL":
                result = (float(v1) * float(v2)) if (t1 == "F" or t2 == "F") else v1 * v2
                stack.append((result, "F" if (t1 == "F" or t2 == "F") else "I"))
            elif instr == "DIV":
                if v2 == 0 or v2 == 0.0: raise Exception("Division by zero.")
                result = (float(v1) / float(v2)) if (t1 == "F" or t2 == "F") else v1 // v2
                stack.append((result, "F" if (t1 == "F" or t2 == "F") else "I"))
            elif instr == "MOD":
                if t1 != "I" or t2 != "I": raise Exception("The modulo operator can only be used with integer values.")
                if v2 == 0: raise Exception("Division by zero.")
                result = v1 % v2
                stack.append((result, "I"))
        elif instr == "PRINT":
            if len(parts) != 2: raise Exception("Invalid PRINT instruction format.")
            print_type = parts[1]
            if not stack: raise Exception("Stack underflow on PRINT.")
            value, _ = stack.pop()
            if print_type == "I": print(int(value))
            elif print_type == "F": print(float(value))
            else: raise Exception("Unknown type in PRINT instruction.")
        else: raise Exception(f"Unknown instruction: {instr}")

if __name__ == "__main__": main()