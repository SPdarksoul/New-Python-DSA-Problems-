# def printName(n):
#     if n == 0:
#         return
#     print("sagar")
#     printName(n - 1)  

# printName(5) 

# print 1 to n recursion
# def printNumber(i, n):
#     if i > n:
#         return
#     print(i)
#     printNumber(i + 1, n)

# printNumber(1, 10)


# print n to 1 using recursion
# def printNumber( n):
#     if n <0:
#         return
#     print(n)
#     printNumber(n - 1)

# printNumber( 10)

# factorial of a number

# def fact (i,n):
#     if i > n:
#         return 1
#     return 1*fact(i+1,n)

# ans =fact(12)
# print(ans)



# def factorial (n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)

# ans =factorial(6)
# print(ans)

# Sum of first n numbers

# def sum_of_first_n_numbers(n):
#     total_sum = 0
#     for i in range(n + 1):
#         total_sum += i
#     return total_sum

# print(sum_of_first_n_numbers(10))\




# reversed an array
# arr = [1, 2, 3, 4, 5]
# arr.reverse()
# print(arr) 


# lst = list(map(int,input().split()))

# n =len(lst)

# for i in range(n//2):
#    lst[i],lst[n-1-i]=lst[n-1-i],lst[i]

# print(lst)

# def reverse(s, e, lst):
#     if s >= e:
#         return
#     lst[s], lst[e] = lst[e], lst[s]
#     reverse(s + 1, e - 1, lst)

# lst = [1, 2, 3, 4, 5]
# reverse(0, len(lst) - 1, lst)
# print(lst)

# string = input()
# def reverse(s, e, string):
#     if s >= e:
#         return
#     string[s], string[e] = string[e], string[s]
#     reverse(s + 1, e - 1, string)
#  reverse(0, len(string) - 1, string)   


# Check  if a string is palindrome

# Str = input("Enter a string: ")

# def palindrome(s, e, Str):
#     if s >= e:
#         return True
#     if Str[s] != Str[e]:
#         return False
#     return palindrome(s + 1, e - 1, Str)
      
# ans = palindrome(0, len(Str) - 1, Str)
# print(ans)