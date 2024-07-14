# # Count digit in a Number 

# # def CountNumber(num):
# #     cnt =0
# #     while num > 0:
# #         num =num// 10
# #         cnt +=1
# #     return cnt

# # num = int(input())
# # ans = CountNumber(num)
# # print(ans)

# # Output PS D:-
# # 122122
# # 6


# # def CountNumber(num):
# #     return len(str(num))

# # num = int(input())
# # ans = CountNumber(num)
# # print(ans)

# # Output PS D:-
# # 122122
# # 6



# #  Reverse A number
# def numberReverse(num):
#     ans =0
#     while num > 0:
#         rem =num% 10
#         ans = ans*10+rem
#         num =num // 10
#     return ans
# num = int(input())
# ans = numberReverse(num)
# print(ans)
   

# #    Output
# # 132455
# # 554231

# # Pallindrome
# def numberReverse(num):
#     ans =0
#     while num > 0:
#         rem =num% 10
#         ans = ans*10+rem
#         num =num // 10
#     return ans

# def pallindrome(num):
#     return num == numberReverse(num)

# num = int(input())
# ans = pallindrome(num)
# print(ans)
   
# # Output
# # 654545
# # False

# # GDC or HCF

# def gcd(a, b):
#     divisor = min(a, b)
#     dividend = max(a, b)

#     while dividend % divisor != 0:
#         temp = dividend
#         dividend = divisor
#         divisor = temp % divisor
        
#     return divisor

# # num = int(input())
# ans = gcd(13, 12)
# print(ans)

# #Armstrong

# def CountNumber(num):
#     cnt =0
#     while num > 0:
#         num =num// 10
#         cnt +=1
#     return cnt

# def armstrong(num):
#     ans =0
#     k =CountNumber(num)
#     temp =num
#     while num >0:
#         rem =num%10
#         ans =ans+ rem**K
#         num =num//10
#     return temp ==ans 

# ans = armstrong(153)
# print(ans)


#print all Devisers

# def numDeviser(num):
#     for i in range(1,num+1):
#         if num%i ==0:
#            print(i)


# numDeviser(132)          
# 
# 
# check for the prime  


# def IsPrime(num):
#     if num<2:
#         return False
#     i=2
#     while i*i<=num:
#         if num%1==0:\
        
#           return False
#         i+1
#         return True
    
#     ans = IsPrime(1232)
#     print(ans)