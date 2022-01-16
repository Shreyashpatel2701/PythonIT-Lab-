Array = []
Reverse_Array = []
Add_Array = []

print("Enter the Number OF Elements Required in  Array")

n = int(input())

for i in range(n) :
    print("Enter the Value to be inserted at position : " + str(i) + " OF array")
    value_to_insert = int(input())
    Array.append(value_to_insert)
print("The given array is : ")
print(Array)

# METHOD 5 : TO REVERSE ARRAY
Reverse_Array =Array.copy()
Reverse_Array.reverse()

# METHOD 4 : TO REVERSE ARRAY
"""for i in Array :
      Reverse_Array.append(i)
Reverse_Array.sort( reverse = True)"""

# METHOD 3 : TO REVERSE ARRAY
"""Reverse_Array =Array[::-1]"""

# METHOD 2 : TO REVERSE ARRAY
"""Reverse_Array = [ i for i in Array]
Reverse_Array.reverse()"""

# METHOD 1 : TO REVERSE ARRAY
""""for i in Array :
      Reverse_Array.append(i)
Reverse_Array.reverse()"""

print("The reversed Array is : ")
print(Reverse_Array)

for i in range(len(Array)):
    Add_Array.append(Array[i] + Reverse_Array[i])
print("The addition of two array is : ")
print(Add_Array)
