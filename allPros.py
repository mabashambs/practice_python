#Sorting Techniques
"""
def BubbleSort(list1):
      for i in range(len(list1)-1,0,-1):
            for j in range(i):
                  if list1[j]>list1[j+1]:
                        list1[j],list1[j+1]=list1[j+1],list1[j]

def SelectionSort(list1):
      for i in range(len(list1)-1):
            small = i
            for j in range(i,len(list1)):
                  if list1[small]>list1[j]:
                        small = j
            list1[i],list1[small]=list1[small],list1[i]


list1 = [10,9,8,7,6,5]
BubbleSort(list1)
print(list1)

SelectionSort(list1)
print(list1)
"""
#Prime Number Checker
"""
def isPrime(val):
      if val < 2:
            return False
      else:
            for i in range(2,val):
                  if (val%i==0):
                        return False
                  else :
                        return True
val = int(input("Enter a number:"))
if isPrime(val):
      print("Is Prime")
else :
      print("Not Prime")
"""
#Prime Numbers Calculater {lowerBound,UpperBound}
"""
def PrimeCounter(low,upp):
      for i in range(low,upp+1):
            if low>2:
                  for j in range(2,i):
                        if i%j==0:
                              break
                        else:
                              print(i)
                              break



low,upp = 5,20
PrimeCounter(low,upp)
"""
#Palindrome Checker
"""
def Palindrome(num):
      if num == num[::-1]:
            return True
      else:
            return False
if Palindrome(input("Enter a name or Number : ")):
      print("is palindrome")
else:
      print("Not Palindrome")

"""
#Factorial Finder
"""
def fact(num):
      if num==0:
            return 1
      else:
            return num*fact(num-1)

res = fact(int(input("enter a num")))

print(res)
"""
#Searching Algorithms
"""
def LinearSearch(list1,val):
      for i in range(0,len(list1)):
            if list1[i]==val:
                  print("Item Found at",i,"Index")
                  break
      else:
            print("Not Found")

def BinarySearch(list1,val):
      low = 0
      upp = len(list1)-1
      while low<=upp:
            mid = (low+upp)//2
            if list1[mid] == val:
                  return True
            else:
                  if list1[mid]<val:
                        low = mid+1
                  else:
                        upp = mid-1

list1 = [12,33,42,1,22,44,55,45]
val = int(input("entera integer : "))
if LinearSearch(list1,val):
      print("found")
else:
      print("Not Found")          
list1 = [2,3,4,11,22,33,44,55,66,67]
val = int(input("entera integer : "))
if BinarySearch(list1,val):
      print("found")
else:
      print("Not Found")

"""
#Fibonacci series
"""
def fibSeries(val):
      a = 0
      b = 1
      print(a)
      print(b)
      for i in range(1,val):
            c = a+b
            a = b
            b = c
            print(b)
            
fibSeries(9)
def fibVal(n):
      if n < 0:
            print("Enter valid digit..")
      elif n == 0:
            return 0
      elif n == 1 or n==2 :
            return 1
      else :
            return fib(n-1) + fib(n-2)
            
res = fibVal(9)
print(res)
"""





























