import sys

from sayings import hello

if len(sys.argv) == 2:
  hello(sys.argv[1])

students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin"}