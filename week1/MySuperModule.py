#class definition
class ListKeeper:
    
    #initialising dictionary
    my_dictionary = {
        "fruits": ["apple", "banana"],
        "vegetables": ["Potato", "Tomato", "Onion"]
    }

    #dipslay function
    #to display all lists inside dictionary
    def show(self):
        print(self.my_dictionary)

    #add method
    #to add new list to dictionary
    def add(self, name, myList):
        self.my_dictionary[name]= myList
        print(self.my_dictionary)
        
    #append method
    #to append new element to list
    def append(self, name, myList):
        self.my_dictionary[name].append(myList)
        print(self.my_dictionary)

    #sort method    
    #to sort the specified list
    def sort(self, name):
        self.my_dictionary[name].sort()
        print(self.my_dictionary)

    #delete method
    #to delete the specified list
    def delete(self, name):
        del self.my_dictionary[name]
        print(self.my_dictionary)
