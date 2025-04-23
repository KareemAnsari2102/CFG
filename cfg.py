from collections import defaultdict

class CFG:
    def __init__(self):
        self.productions = defaultdict(list)
        self.start_symbol = None

    def add_production(self, lhs, rhs_list):
        for rhs in rhs_list:
            self.productions[lhs].append(rhs)

    def set_start(self, symbol):
        self.start_symbol = symbol
