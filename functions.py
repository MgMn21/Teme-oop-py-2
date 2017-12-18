# THIS FILE CONTAINS FUNCTION AND CLASS DECLARATIONS

class multiSet:  # Here we have the multiSet clas which will contain a collections.Counter container, a checker for the UI elements and the functions
    def __init__(self, multiset, cheker):
        self.multi = multiset
        self.check = cheker

    def createset(self):  # This adds elements to a multiset
        self.check = "y"  # This is for the interface options
        while self.check != "n" and self.check != "N":
            elem = input("Element: ")
            occur = input("# of occurrences: ")  # We input the element and the number of times it shows upp in the set

            occur = int(occur)

            temp = {elem: occur}  # We store the element and the number of occurrences in a temporary container
            self.multi.update(temp)  # We update the set with the new element

            self.check = input("Do you want to add another element?(y/n): ")  # This gives the option of adding
                                                                              # another element

    def outputset(self):  # This method outputs the contents of our set
        lst = list(self.multi.elements())  # Since elements are stores as a pair of key: occurrences in .Counter we put the keys into a list
        lst.sort()  # We sort them
        print(lst)  # And we output them

    def nrofelements(self):  # This calculates the total number of elements
        s = sum(self.multi.values())  # Since .Counter stores the number of occurrences for each element all we have to do is add them upp
        print("# of elements in the set: {}".format(s))

    def issetempty(self):  # This checks if the set is empty
        s = sum(self.multi.values())  # If the sum of all occurrences is 0 that means we have no items in the set, so the set is empty
        if s == 0:
            print("Yes, the multiset is empty.")
        else:
            print("No, the multiset has {} elements.".format(s))

    def elementexists(self):  # This checks if a specified element exists in the set
        key = input("Which element do you wish to check? ")  # First we input the element

        temp = self.multi[key]  # We check the number of occurrences the element has

        if temp == 0:  # If the number of occurrences is 0 it means our element is not in the set
            print("The multiset does not contain the specified element.")
        else:
            print("The element {} exists in the multiset.".format(key))

    def supp(self):  # This calculates the support of our multiset
        temp = set(self.multi)  # Since the support is the set of unique elements in our multiset all we have to do is convert our counter into a standard set
        # thus we obtain a set of unique elements from our original multiset
        print(temp)

    def nrofoccurrances(self):  # This outputs the number of occurrences of a specified element
        e = input("Please enter the element you wish to search: ")
        temp = self.multi[e]  # The collections.Counter container already stores the number of occurrences of an element
        print("k(e, M) = {}".format(temp))  # So all we have to do is print that number

    def inclusion(self, container):  # This checks if our multiset is a subset of another multiset
        if all(container[key] >= self.multi[key] for key in self.multi):  # For our set to be included in another multiset that multiset needs to contain all the items in our set
            print(
                "Yes, A is a subset of B.")  # and those items need to occur more times then they do in our original set
        else:
            print("A is not a subset of B.")

    def union(self, mset2):  # This performs the union operation for 2 sets and prints the result
        temp = self.multi | mset2  # We store the result in a temporary container
        temp = list(temp.elements())  # and then we output that result, like we do in the outputset() function
        temp.sort()
        print("The resulting multiset is {}".format(temp))

    def subtraction(self, mset2):  # This subtracts a set from our original set and prints the result
        self.multi = self.multi - mset2  # First we do the subtraction
        temp = list(self.multi.elements())  # Then we output the result using the same method as in outputset
        print("A = {}".format(temp))

    def intersection(self, mset2):  # This performs the intersection of 2 sets
        temp = self.multi & mset2  # We perform the intersection
        temp = list(temp.elements())  # We print as above
        temp.sort()
        print("The resulting multiset is {}".format(temp))

    def compare(self, msetB):  # This performs a comparison between 2 sets by using the inclusion method
        if self.multi == msetB:  # If the sets are perfectly equal
            print("Multiset A is equal to B.")
        elif all(self.multi[key] >= msetB[key] for key in msetB):  # If the set B is a subset of A then A is larger than B
            print("Multiset A is larger than B")
        elif all(msetB[key] >= self.multi[key] for key in self.multi):  # If the set A is a subset of B then B is larger than A
            print("Multiset A is smaller than B")
        elif msetB != self.multi:  # If none of the above apply then the 2 sets are distinct
            print("Multiset A is distinct from B")