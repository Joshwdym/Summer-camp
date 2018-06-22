print("""Welcome to Madllibs
You'll be asked for different nouns and verbs, try to keep these fun

Stop

Run Config Name
Command:

madlib.py
Runner: Python 2
CWD
ENV
ny""")

noun1=raw_input("Please provide a noun")
noun2=raw_input("Please provide a noun")
building=raw_input("Please provide the title of a building")
verb=raw_input("Please provide a verb")
madlibs = ("""learning to drive is a tricky process. There are a few
1.Keep two %s on the steeing wheel at all times.
2.Step on the %s to speed up and the %s to slow down.
3.Your parents will just LOVE it if you %s the radio 
4.Make sure to honk your horn when you %s on a street sign.""")
print(madlibs %(noun1,noun2,building,verb))