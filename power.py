def power(base,p):
    res =1
    while p>0:  
      if p%2 == 0:
         base = base *base
      else:
         p =p-1
         res =res *base
    return res



print(power(10,30))

         
