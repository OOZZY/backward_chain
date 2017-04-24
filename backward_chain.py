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

def is_resolvable(goals, rule):
    """Returns whether the given clauses/rules are resolvable.

    Specifically, returns whether head(rule) is in goals.
    """
    return head(rule) in goals

def resolve(goals, rule):
    """Returns the resolution of the given clauses/rules.

    Specifically, replaces occurence of head(rule) in goals with body(rule).
    """
    print("Substituting '{}' in goals with '{}'"
            .format(head(rule), body_to_string(body(rule))))
    atom_index = goals.index(head(rule))
    return goals[0:atom_index] + body(rule) + goals[atom_index+1:]

def derive_query(query, knowledge_base):
    """Derives given query from given knowledge_base. Prints the derivation.
    """
    goals = query
    print(goals_to_string(goals))

    # following variable is used to keep track of the number of times we have
    # chosen a rule from the knowledge base that couldn't be resolved with the
    # goals. this variable will get reset to 0 whenever we do find a rule from
    # the knowledge base that could be resolved with the goals. this variable
    # is used to terminate the following loops if further derivation is not
    # possible
    unresolvable_rule_count = 0

    # iterates through the rules in the knowledge base over and over again.
    # the iteration stops when a terminating condition is satisfied
    done = False
    while not done:
        for rule in knowledge_base:
            if is_resolvable(goals, rule):
                unresolvable_rule_count = 0
                goals = resolve(goals, rule)
                print(goals_to_string(goals))
                if not goals:
                    print()
                    print("The knowledge base entails the query.")
                    done = True
                    break
            else:
                unresolvable_rule_count += 1
                if unresolvable_rule_count == len(knowledge_base):
                    print("Further derivation is not possible.")
                    print()
                    print("The knowledge base does not entail the query.")
                    done = True
                    break

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
    derive_query(query, knowledge_base)
