n =5

for i in range(n):
    for j in range(1,n-i+1):
        print(j,end="")
    print()    


# Alphabet Pyramid

    rows = int(input("Enter the number of rows: "))  

#Outer for loop to handle number of rows  
for num in range(rows+1):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for i in range(num):  
            print(num, end=" ")       
  
        #End line after each row  
        print()



# Pattern Pyramid
        rows = int(input("Enter number of rows: "))

ascii_value = 65

#Outer for loop to handle number of rows  
for i in range(rows):
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print()

    # Inverted Number Pyramid
    rows = int(input("Enter the number of rows: "))  

#Outer for loop executing in reverse order
for i in range(rows + 1, 0, -1):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for j in range(0, i - 1):  
            print("* ", end=" ")       
  
        #End line after each row  
        print()


        #  Inverted Number Pyramid in Descending Order

        rows = int(input("Enter the number of rows: "))  

#Outer for loop executing in reverse order
for i in range(rows, 0, -1):  
    num = i
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
    for j in range(0, i):  
            print(num, end=" ")       
  
    #End line after each row  
    print()

    # Inverted Pyramid of a Digit

    rows = int(input("Enter the number of rows: "))  
num = rows  

#Outer for loop executing in reverse order
for i in range(rows, 0, -1):  
   #Inner for loop to handle number of columns  
    #values change according to the outer loop  
    for j in range(0, i):  
            print(num, end=" ")       
  
    #End line after each row  
    print()

    #  Pattern Semi-Pyramid

    rows = int(input("Enter the number of rows: "))  

#Outer for loop to handle number of rows  
for i in range(1, rows+1):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for j in range(1, i + 1):  
            print(j, end=" ")       
  
        #End line after each row  
        print()

        # Inverted Equilateral Pyramid of * Pattern

        rows = int(input("Enter the number of rows: "))  
m = (2*rows)-2

#Outer for loop to handle number of rows  
for i in range(rows-1,-1,-1):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for j in range(m,0,-1):  
            print(end=" ")
        #incrementing m after each loop
        m += 1 
        for j in range(0, i+1):  
            #printing triangle pyramid using asterik
            print("*",end=" ")              
  
        #End line after each row  
        print()