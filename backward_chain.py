import sys

"""
implementation notes:
- a rule/clause is represented by an array of strings
  - each string in the array represents a literal/atom
- a knowledge base is represented by an array of such rules (i.e. an array of
  arrays of strings)
"""

def read_rules(path_to_file):
    """Reads rules from the given file and returns the knowledge_base.
    """
    rules = []

    with open(path_to_file) as input_file:
        for line in input_file:
            # remove any whitespace surrounding the rule
            line = line.strip()
            if not line:
                continue

            rule = line.split()
            rules.append(rule)

    if rules:
        return rules
    else:
        return []

def head(rule):
    """Returns the head of the given rule.
    """
    return rule[0]

def body(rule):
    """Returns the body of the given rule.
    """
    return rule[1:]

def body_to_string(body):
    """Returns a string representation of the given body.
    """
    string = ""

    first = True
    for literal in body:
        if first:
            string += literal
            first = False
        else:
            string += " ^ " + literal

    return string

def query_to_string(query):
    """Returns a string representation of the given query.
    """
    return "?" + body_to_string(query)

def goals_to_string(goals):
    """Returns a string representation of the given goals.
    """
    return "goals: " + body_to_string(goals)

def rule_to_string(rule):
    """Returns a string representation of the given rule.
    """
    if len(rule) == 1:
        return head(rule)
    else:
        return "{} => {}".format(body_to_string(body(rule)), head(rule))

def print_knowledge_base(knowledge_base):
    """Prints the given knowledge base.
    """
    for rule in knowledge_base:
        print(rule_to_string(rule))

def solve(goals, knowledge_base, recursion_depth):
    """Derives given query from given knowledge_base. Prints the derivation.
    """
    print("{}{}".format("  " * (recursion_depth - 1), goals_to_string(goals)))
    if not goals:
        return True

    a = goals[0]
    goals = goals[1:]

    for rule in knowledge_base:
        if head(rule) == a:
            print("{}Substituting '{}' in goals with '{}'"
                    .format("  " * recursion_depth, a, body_to_string(body(rule))))
            if solve(body(rule) + goals, knowledge_base, recursion_depth + 1):
                return True

    return False

if len(sys.argv) < 3:
    print("usage:")
    print("$ python3 backward_chain.py <path-to-file> <query>...")
    print("or")
    print("$ ./backward_chain.py <path-to-file> <query>...")
else:
    # knowledge_base is an array of arrays of strings
    path_to_file = sys.argv[1]
    knowledge_base = read_rules(path_to_file)

    # query is an array of strings
    query = sys.argv[2:]

    print("Knowledge Base:")
    print_knowledge_base(knowledge_base)
    print()
    print("Query:")
    print(query_to_string(query))
    print()
    print("Derivation:")
    entailed = solve(query, knowledge_base, 1)

    if entailed:
        print()
        print("The knowledge base entails the query.")
    else:
        print()
        print("The knowledge base does not entail the query.")
