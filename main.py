# THIS IS THE MAIN FILE

import collections  # I used the collections.Counter container in order to implement multisets
import functions

multisetA = collections.Counter()
multisetB = collections.Counter()  # We have 2 sets in order to check the operations

setclassA = functions.multiSet(multisetA, "y")
setclassB = functions.multiSet(multisetB, "y") # Now we create the 2 multiSet class objects to work with
                                               # This is the only major difference in main, from now on it's mostly just the UI like it was in the first project

check = '1'

while check != '0':
    print("Please chose an option:\n1 - Create multiset A\n2 - Create multiset B\n3 - Check number of elements\n4 - "
          "Check if the multiset is empty\n5 - Check if an element is in the multiset\n6 - Calculate the support\n7 - "
          "Calculate k(e, M)\n8 - Perform set operations\n9 - Display multiset\n0 - Exit\n")
    check = input("#")
    if check == '1':  # We add elements to A
        setclassA.createset()
    if check == '2':  # We add elements to B
        setclassB.createset()
    if check == '3':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We count the elements in A
            setclassA.nrofelements()
        elif temp == 'B' or temp == 'b':  # We count the elements in B
            setclassB.nrofelements()
        else:
            print("Not a valid input")
    if check == '4':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We check if A is empty
            setclassA.issetempty()
        elif temp == 'B' or temp == 'b':  # We check if B is empty
            setclassB.issetempty()
        else:
            print("Not a valid input")
    if check == '5':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We check if a specified element exists in A
            setclassA.elementexists()
        elif temp == 'B' or temp == 'b':  # We check if a specified element exists in B
            setclassB.elementexists()
        else:
            print("Not a valid input")
    if check == '6':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We calculate the support of A
            setclassA.supp()
        elif temp == 'B' or temp == 'b':
            setclassA.supp()  # We calculate the support of B
        else:
            print("Not a valid input")
    if check == '7':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We calculate k(e, A)
            setclassA.nrofoccurrances()
        elif temp == 'B' or temp == 'b':  # We calculate k(e, B)
            setclassB.nrofoccurrances()
        else:
            print("Not a valid input")
    if check == '8':  # We select the operation we want to perform
        temp = input("Which operation would you like to perform:\n1 - Inclusion(A subset of B)\n2 - Union(A | B)\n3 - "
                     "Subtraction(A - B)\n4 - "
                     "Intersection(A & B)\n5 - Comparrison\n# ")
        if temp == '1':  # We check if A is a subset of B
            setclassA.inclusion(setclassB.multi)
        if temp == '2':  # We unite A and B
            setclassA.union(setclassB.multi)
        if temp == '3':  # We subtract B from A
            setclassA.subtraction(setclassB.multi)
        if temp == '4':  # We intersect A and B
            setclassA.intersection(setclassB.multi)
        if temp == '5':  # We compare A and B
            setclassA.compare(setclassB.multi)
    if check == '9':
        temp = input("Which set would you like to perform this operation for?(A/B) ")
        if temp == 'A' or temp == 'a':  # We output A
            print("A = ")
            setclassA.outputset()
        elif temp == 'B' or temp == 'b':  # We output B
            print("B = ")
            setclassB.outputset()
        else:
            print("Not a valid input")