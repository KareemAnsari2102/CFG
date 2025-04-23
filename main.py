from cfg import CFG
from ambiguity_checker import is_ambiguous

def main():
    print("Enter the CFG in the following format:")
    print("Example: S -> aSb | ab")
    print("Type 'done' when you are finished.")

    cfg = CFG()
    start_symbol_set = False

    while True:
        line = input("Production: ").strip()
        if line.lower() == 'done':
            break
        if '->' not in line:
            print("Invalid format. Use 'A -> alpha | beta'")
            continue

        lhs, rhs = line.split('->')
        lhs = lhs.strip()
        rhs_options = [list(prod.strip()) for prod in rhs.strip().split('|')]

        if not start_symbol_set:
            cfg.set_start(lhs)
            start_symbol_set = True

        cfg.add_production(lhs, rhs_options)

    ambiguous, example = is_ambiguous(cfg)

    if ambiguous:
        print("\nThe grammar is AMBIGUOUS.")
        print(f"String with multiple derivations: '{example}'")
    else:
        print("\nThe grammar is NOT ambiguous.")

if __name__ == "__main__":
    main()
