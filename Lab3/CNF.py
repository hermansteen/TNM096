from sympy import subsets
#deepcopy
import copy


class Clause:
    def __init__(self):
        self.p = set()
        self.n = set()

    def __str__(self):
        return f"{' '.join(self.p)} {' '.join(['¬' + x for x in self.n])}"


def resolution(A, B):
    C = Clause()
    # if intersecton between A.n and B.n is empty
    if not A.p.intersection(B.n) and not A.n.intersection(B.p):
        return False

    # if intersection between A.n and B.n is not empty
    if A.p.intersection(B.n):
        # pick a random element from the intersection
        a = A.p.intersection(B.n).pop()
        # remove the element from both A.n and B.n
        A.p.remove(a)
        B.n.remove(a)
    else:
        # pick a random element from the intersection
        a = A.n.intersection(B.p).pop()
        # remove the element from both A.n and B.p
        A.n.remove(a)
        B.p.remove(a)
    C.p = A.p.union(B.p)
    C.n = A.n.union(B.n)
    # if C is a tautology
    if C.p.intersection(C.n):
        return False
    return C


def solver(KB):
    while True:
        S = set()
        KB_ = copy.deepcopy(KB)
        # for each pair of clauses C1, C2 in KB
        for A in KB:
            for B in KB:
                if A == B:
                    continue
                C = resolution(A, B)
                # if C is not false
                if C:
                    # add C to S
                    S = S | {C}
        if not S:
            return KB
        # add all clauses in S to KB
        KB = incorporate(S, KB)
        print('S:')
        for C in S:
            print(C)

        print('KB:')
        for C in KB:
            print(C)
        # until KB' = KB
        if KB_ == copy.deepcopy(KB):
            return set(KB)


def incorporate(S, KB):
    # for each C in S
    for A in S:
        KB = incorporate_clause(A, KB)
    return KB


def incorporate_clause(A, KB):
    for B in KB:
        if B.p == A.p and B.n == A.n:
            return KB
    for B in KB:
        if A.p.issubset(B.p) and A.n.issubset(B.n):
            return KB
        if A.p.issubset(B.n) and A.n.issubset(B.p):
            KB.remove(B)
    KB = KB | {A}
    return KB


def main():
    A = Clause()
    A.p = set(['c', 't'])
    A.n = set(['b'])
    B = Clause()
    B.p = set(['z', 'b'])
    B.n = set(['c'])
    C = resolution(A, B)
    print(C)


def bob():
    KB = set()
    # sun ∧ money ⇒ ice
    # money ∧ ¬ice ⇔ movie
    # ¬sun ∧ ¬money ⇒ cry
    C1 = Clause()
    C1.n = set(['sun', 'money'])
    C1.p = set(['ice'])

    C2 = Clause()
    C2.p = set(['movie', 'ice'])
    C2.n = set(['money'])

    C3 = Clause()
    C3.p = set(['money'])
    C3.n = set(['movie'])

    C4 = Clause()
    C4.n = set(['movie', 'ice'])

    C5 = Clause()
    C5.p = set(['movie'])

    C6 = Clause()
    C6.p = set(['cry', 'sun', 'money'])

    # add all clauses to set KB
    KB = KB | {C1}
    KB = KB | {C2}
    KB = KB | {C3}
    KB = KB | {C4}
    KB = KB | {C5}
    KB = KB | {C6}

    for A in KB:
        print(A)

    KB = solver(KB)
    for A in KB:
        print(A)


bob()
