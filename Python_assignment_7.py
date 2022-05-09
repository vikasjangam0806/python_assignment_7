#Q-1 Reverse words in a given String in Python
# Function to reverse words of string 
  
def rev_sentence(sentence): 
  
    # first split the string into words 
    words = sentence.split(' ') 
  
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words)) 
  
    # finally return the joined string 
    return reverse_sentence 
  
if __name__ == "__main__": 
    input = 'Vikas jaywant jangam'
    print (rev_sentence(input))

#Q-2 Ways to remove i’th character from string in Python
# Python code to demonstrate
# method to remove i'th character
# Naive Method
  
# Initializing String 
test_str = "mrCHIKU"
  
# Printing original string 
print ("The original string is : " + test_str)
  
# Removing char at pos 3
# using loop
new_str = ""
  
for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]
  
# Printing string after removal  
print ("The string after removal of i'th character : " + new_str)

#Q-3 Python | Check if a Substring is Present in a Given String

# function to check if small string is 
# there in big string
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
            
# driver code
string = "geeks for geeks"
sub_str ="geek"
check(string, sub_str)

#Q-4 Python – Words Frequency in String Shorthands

# Python3 code to demonstrate working of 
# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()
  
# initializing string
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
  
# printing original string
print("The original string is : " + str(test_str))
  
# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()
res = {key: test_str.count(key) for key in test_str.split()}
  
# printing result 
print("The words frequency : " + str(res)) 

#Q-5 Python – Convert Snake case to Pascal case

# Python3 code to demonstrate working of 
# Convert Snake case to Pascal case
# Using title() + replace()
  
# initializing string
test_str = 'geeksforgeeks_is_best'
  
# printing original string
print("The original string is : " + test_str)
  
# Convert Snake case to Pascal case
# Using title() + replace()
res = test_str.replace("_", " ").title().replace(" ", "")
  
# printing result 
print("The String after changing case : " + str(res)) 

#Q-6 Find length of a string in python (4 ways)
# Python code to demonstrate string length 
# using len
  
str = "geeks"
print(len(str))

# Python code to demonstrate string length 
# using for loop
  
# Returns length of string
def findLen(str):
    counter = 0    
    for i in str:
        counter += 1
    return counter
  
  
str = "geeks"
print(findLen(str))

# Python code to demonstrate string length 
# using while loop.
  
# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter
  
str = "geeks"
print(findLen(str))


# Python code to demonstrate string length 
# using join and count
  
# Returns length of string
def findLen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(str)).count(some_random_str) + 1
  
str = "geeks"
print(findLen(str))

#Q-7 Python program to print even length words in a string

# Python3 program to print 
#  even length words in a string 
  
def printWords(s):
      
    # split the string 
    s = s.split(' ') 
      
    # iterate in words of string 
    for word in s: 
          
        # if length is even 
        if len(word)%2==0:
            print(word) 
  
  
# Driver Code 
s = "i am muskan" 
printWords(s) 

#Q-8 Python program to accept the strings which contains all vowels

# Python program to accept the strings
# which contains all the vowels
 
# Function for check if string
# is accepted or not
def check(string) :
 
    string = string.lower()
 
    # set() function convert "aeiou"
    # string into set of characters
    # i.e.vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels = set("aeiou")
 
    # set() function convert empty
    # dictionary into empty set
    s = set({})
 
    # looping through each
    # character of the string
    for char in string :
 
        # Check for the character is present inside
        # the vowels set or not. If present, then
        # add into the set s by using add method
        if char in vowels :
            s.add(char)
        else:
            pass
             
    # check the length of set s equal to length
    # of vowels set or not. If equal, string is 
    # accepted otherwise not
    if len(s) == len(vowels) :
        print("Accepted")
    else :
        print("Not Accepted")
 
 
# Driver code
if __name__ == "__main__" :
     
    string = "SEEquoiaL"
 
    # calling function
    check(string)

    #Q-9 Python | Count the Number of matching characters in a pair of string

    # Python code to count number of matching
# characters in a pair of strings
  
# count function
def count(str1, str2): 
    c, j = 0, 0
      
    # loop executes till length of str1 and 
    # stores value of str1 character by character 
    # and stores in i at each iteration.
    for i in str1:    
          
        # this will check if character extracted from
        # str1 is present in str2 or not(str2.find(i)
        # return -1 if not found otherwise return the 
        # starting occurrence index of that character
        # in str2) and j == str1.find(i) is used to 
        # avoid the counting of the duplicate characters
        # present in str1 found in str2
        if str2.find(i)>= 0 and j == str1.find(i): 
            c += 1
        j += 1
    print ('No. of matching characters are : ', c)
  
# Main function
def main(): 
    str1 ='aabcddekll12@' # first string
    str2 ='bb2211@55k' # second string
    count(str1, str2) # calling count function 
  
# Driver Code
if __name__=="__main__":
    main()


#Q-10 Remove all duplicates from a given string in Python


from collections import OrderedDict 
  
# Function to remove all duplicates from string 
# and order does not matter 
def removeDupWithoutOrder(str): 
  
    # set() --> A Set is an unordered collection 
    #         data type that is iterable, mutable, 
    #         and has no duplicate elements. 
    # "".join() --> It joins two adjacent elements in 
    #             iterable with any symbol defined in 
    #             "" ( double quotes ) and returns a 
    #             single string 
    return "".join(set(str)) 
  
# Function to remove all duplicates from string 
# and keep the order of characters same 
def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str)) 
  
# Driver program 
if __name__ == "__main__": 
    str = "geeksforgeeks"
    print ("Without Order = ",removeDupWithoutOrder(str)) 
    print ("With Order = ",removeDupWithOrder(str)) 


