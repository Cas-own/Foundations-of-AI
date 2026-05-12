class FamilyKnowledgeBase:
    def __init__(self):
        # Facts
        self.parents = [('john', 'mary'), ('john', 'jeff'), ('ann', 'mary'), ('mary', 'james')]
        self.males = ['john', 'jeff', 'james']
        self.females = ['ann', 'mary']

    def get_father(self, child):
        # Rule: father(X, Y) :- parent(X, Y), male(X).
        for p, c in self.parents:
            if c == child and p in self.males:
                return p
        return None

    def get_grandparent(self, grandchild):
        # Rule: grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
        for p, child in self.parents:
            for p2, gchild in self.parents:
                if gchild == grandchild and child == p2:
                    return p
        return None

# Testing the Knowledge-Based Agent
kb = FamilyKnowledgeBase()
print("--- Task 3: Prolog Knowledge Base Test ---")
print(f"Who is the father of mary? -> {kb.get_father('mary')}")
print(f"Who is the grandparent of james? -> {kb.get_grandparent('james')}")