from collections import defaultdict

def is_ambiguous(cfg, max_depth=5):
    derivation_counts = defaultdict(int)

    def generate(symbols, depth):
        if depth > max_depth:
            return
        if all(s not in cfg.productions for s in symbols):
            s = ''.join(symbols)
            derivation_counts[s] += 1
            return
        for i, sym in enumerate(symbols):
            if sym in cfg.productions:
                for prod in cfg.productions[sym]:
                    new_symbols = symbols[:i] + prod + symbols[i+1:]
                    generate(new_symbols, depth + 1)
                break

    generate([cfg.start_symbol], 0)

    for string, count in derivation_counts.items():
        if count > 1:
            return True, string
    return False, None
