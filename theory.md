Search in AI: This is the process of navigating from an initial state to a goal state by evaluating a sequence of actions.
Uninformed Search (Blind Search): The agent has no "hint" about how far the goal is. It explores nodes based solely on the structure of the map/tree.
Examples: BFS (Breadth-First Search), DFS (Depth-First Search).
Informed Search (Heuristic Search): The agent uses a "Heuristic" (h(n))—an educated guess or estimate—to prioritize which paths to explore first, making it much faster.
Examples: A* Search, Greedy Best-First Search.
Question 1c:
Definitions:
Valid: A formula is valid if it is True in every possible interpretation (all rows of the truth table are T).
Satisfiable: A formula is satisfiable if there is at least one interpretation where it is True (at least one T).
Falsifiable: A formula is falsifiable if there is at least one interpretation where it is False (at least one F).
truth table for P^Q -R
P Q R P \land Q \neg R Result (P \land Q \to \neg R)
T T T T F F
T T F T T T
T F T F F T
T F F F T T
F T T F F T
F T F F T T
F F T F F T
F F F F T T
Conclusion:
This formula is Satisfiable (Rows 2-8 are True).
This formula is Falsifiable (Row 1 is False).
This formula is NOT Valid (Because Row 1 is False).
Question 2(a)
PEAS Framework
Performance: Accuracy of DNA matches, speed of sequencing, and security of sensitive genetic data.
Environment: Laboratory settings, DNA databases, biological samples from victims, and reference samples from relatives.
Actuators: Display screens showing match results, printers for identification certificates, and automated database updates.
Sensors: Genomic sequencing hardware, barcode scanners for sample tracking, and high-resolution imaging sensors.
PAGE Framework
Percepts: Raw genetic sequences extracted from samples and metadata about the victims' families.
Actions: Sequencing DNA, comparing markers against a database, and flagging successful identifications.
Goals: Rapid and 100% accurate identification of all Shakabola victims.
Environment: The biological, digital, and legal landscape of the MMU Artificial Intelligence Institute.
Qustion 2C.
Search-Based Agents: These agents solve problems by looking ahead. They explore various sequences of actions (like a tree) to find a path to a goal, such as the A* algorithm you wrote for Question 1.
Knowledge-Based Agents: These agents use internal logic. They maintain a "Knowledge Base" (facts and rules) and use an inference engine to deduce new information or decide on an action, similar to the Prolog tasks in your assignment.