def is_safe(node, color, assignment, neighbors):
    """Check if any neighbor already has this color."""
    for neighbor in neighbors.get(node, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(nodes, colors, assignment, neighbors):
    """Recursive function to find the valid color for each region."""
    if len(assignment) == len(nodes):
        return assignment

    # Select the next region to color
    unassigned = [n for n in nodes if n not in assignment][0]

    for color in colors:
        if is_safe(unassigned, color, assignment, neighbors):
            assignment[unassigned] = color
            result = backtrack(nodes, colors, assignment, neighbors)
            if result is not None:
                return result
            # If it didn't work, remove the color and try the next one
            del assignment[unassigned]
    return None

# The Map of Australia
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': [] # Tasmania is an island, no neighbors!
}
colors = ['Red', 'Green', 'Blue']

# Execute the solver
solution = backtrack(regions, colors, {}, neighbors)

# Print the output to test
print("--- Task 2: CSP Map Coloring ---")
if solution:
    for region, color in solution.items():
        print(f"{region.ljust(4)} : {color}")
else:
    print("No valid coloring found.")