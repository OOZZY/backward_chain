The program is written in Python 3 and so it requires Python 3 to run.

Run program:
$ ./backward_chain.py <knowledge-base-text-file> <query>...

The program read the given text file to get the rules of the knowledge base. The program assumes that the text file is in the format specified in the assignment.

The program outputs the knowledge base, the query, the derivation, and finally whether or not the knowledge base entails the query.

The following are the test cases I used:

./backward_chain.py example1.txt a
./backward_chain.py example2.txt r
./backward_chain.py example3.txt a
./backward_chain.py example4.txt a c
./backward_chain.py example5.txt a
./backward_chain.py example6.txt p # will run forever, stop program with CTRL-C
./backward_chain.py example6.txt q
./backward_chain.py example7.txt p # will run forever, stop program with CTRL-C
./backward_chain.py example7.txt q # will run forever, stop program with CTRL-C

The following are two example runs of the program (using the two examples in the assignment):

$ ./backward_chain.py example1.txt a
Knowledge Base:
p
p => q
d
q ^ j => g
f => e
f ^ d => c
d ^ g => c
e ^ d => c
j => b
b ^ c => a
j

Query:
?a

Derivation:
goals: a
  Substituting 'a' in goals with 'b ^ c'
  goals: b ^ c
    Substituting 'b' in goals with 'j'
    goals: j ^ c
      Substituting 'j' in goals with ''
      goals: c
        Substituting 'c' in goals with 'f ^ d'
        goals: f ^ d
        Substituting 'c' in goals with 'd ^ g'
        goals: d ^ g
          Substituting 'd' in goals with ''
          goals: g
            Substituting 'g' in goals with 'q ^ j'
            goals: q ^ j
              Substituting 'q' in goals with 'p'
              goals: p ^ j
                Substituting 'p' in goals with ''
                goals: j
                  Substituting 'j' in goals with ''
                  goals:

The knowledge base entails the query.

$ ./backward_chain.py example2.txt r
Knowledge Base:
p
p => q
p ^ q => r
s => r

Query:
?r

Derivation:
goals: r
  Substituting 'r' in goals with 'p ^ q'
  goals: p ^ q
    Substituting 'p' in goals with ''
    goals: q
      Substituting 'q' in goals with 'p'
      goals: p
        Substituting 'p' in goals with ''
        goals:

The knowledge base entails the query.
