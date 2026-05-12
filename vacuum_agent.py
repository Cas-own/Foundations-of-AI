def vacuum_agent(location, status):
    """
    Logic for a Simple Reflex Agent:
    - If current square is Dirty -> Suck.
    - If in A and Clean -> Move Right to B.
    - If in B and Clean -> Move Left to A.
    """
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Move Right'
    elif location == 'B':
        return 'Move Left'

# Test the agent with the four possible scenarios
test_cases = [('A', 'Dirty'), ('A', 'Clean'), ('B', 'Dirty'), ('B', 'Clean')]

print("--- Vacuum Agent Test ---")
for loc, stat in test_cases:
    action = vacuum_agent(loc, stat)
    print(f"Location {loc} is {stat} -> Action: {action}")