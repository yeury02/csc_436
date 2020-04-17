# Below is the explanation on how execute my program

You do not need any alternative libraries to run the program

Have python 3 installed and that should do it

To run the program, simply follow this format: "py main.py (R) A B C D E F G (F) A,B C,D D,E"

replace (R) with the number of attributes in relation

A B C D E F G are the attributes, each attribute should be represented by a single character and have a space in between each other

replace (F) with how may functional dependencies there are

A,B C,D D,E are the functional dependencies... This format essentially is A->B, C->D, D->E

SO, two examples on how to run the program are:
        "py main.py 5 A B C D E 3 A,B C,D D,E"
        "py main.py 4 A B C D 2 A,BCD C,A"
        

