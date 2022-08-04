# In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:

# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   sum = 0  
   temp = num  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
            print(num)