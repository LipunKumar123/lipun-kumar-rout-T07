
'''

print("--------------------implimenting palindrome using for loop-------------------")
print("*****************************************************************************")
#allowing user to give an input
str1= input("enter something here:-")
#lets take an empty string
#the purpose of this is to append the reversed string to it
str2=""
#now iterating through sequence of characters using for loop
for i in str1:
    str2=i+str2

#now comparing both the strings
#string entered by user and the reversed string
#if both are equal then its a palindrome or else not a palindrome
if str1==str2:
    print("the string is palindrome")
else:
    print("the string is not palindrome")

print("**********************************************************************************")
print("----------------------------------------------------------------------------------")

'''

'''
print("############### question number two ###################")
print("finding sum of two digits in output")
print("we will take two inputs for this operation")

import functools
n1=int(input("enter the first number:-"))
n2=int(input("enter the second number:-"))

#using list comprehension for iterating through digits
#for both the numbers


result1=[int(i) for i in str(n1)]
result2=[int(i) for i in str(n2)]

result=result1+result2

final_answer= functools.reduce((lambda a,b : a+b),result)
print("final answer is :",final_answer)



'''


'''

def reverse_String(text):
    index = -1

    # iterate from the last index until half of the index

    for i in range(len(text) - 1, int(len(text) / 2), -1):

        # match character is alphabet or not
        #and that is stored in a temperarory variable and later for swapping purpose
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text



str = "a!!!b.c.d,e'f,ghi"
print("Input string: ", str)
str = reverse_String(list(str))
print("Output string: ", "".join(str))

print("******************************************************************************")
print("******************************************************************************")


'''

'''

print("********* to find out elements duplicate count output in dictionary format **********")
print("_____________________________________________________________________________________")
my_list=["a","b","c","d","n","a","b","m","n","m"]
# above is the given list
#we will deaclare an empty dictionary

freq={}
#now a for loop to iterate over the sequence of elements

for items in my_list:
    if items in freq:
        freq[items]+=1
    else:
        freq[items]=1

for key,value in freq.items():
    print(f'{key}: {value}')
#here formatted string has been used to provide readability

'''

'''

# question number 5
#we will first try to slice the t1 and t2 accordingly

t1= (1,2,3,"a","c")
t2=("b","d",9,8,7)

#slicing these tuples
t3=t2[2:]
t4=t2[:2]
res=t3+t4
print(res)

result=tuple(map(lambda i, j: i + j,t1,res))
print(result)

print("_______________________________________________________________________________")
print("_______________________________________________________________________________")

'''

'''
print("-----------------------------------------------------------------------------")
print("we will here remove leading zeroes from the below IP address")
print("-----------------------------------------------------------------------------")

# here replace method is used which takes 0 and a empty string as arguments
#to replace zeroes with empty string
str1= "216.08.094.196"
print("the IP adress is:",str1)
res=str1.replace("0",'')
print("result after replacing is:-",res)

print("-----------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------")

'''


'''
print("------------------------------------------------------------------------------")
print("******************************************************************************")
#question number seven
#input the list


empty_list=[]
def remove_nesting(lst):
    for i in lst:
        if type(i)==list:
            remove_nesting(i)
        else:
            empty_list.append(i)

lst = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
print("the list is: ",lst)
remove_nesting(lst)
print('after removing:',empty_list)
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")

'''