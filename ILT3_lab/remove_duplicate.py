
#Python program to remove duplicate characters of a given string


def remove_dup_word(string):
    # Used to split string around spaces.
    words = string.split()
     
    # To store individual visited words
    hsh = set()
    # Traverse through all words
    for word in words:
        # If current word is not seen before.
        if word not in hsh:
            print(word, end=" ")
            hsh.add(word)
 
# Driver function
print("the given string is\n String and String Function")
if __name__ == '__main__':
    string = "String and String Function"
    print("after removing string is")
    remove_dup_word(string)
