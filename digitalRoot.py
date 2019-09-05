#Digital Root Program
#Digital Root is sum of all digit in a number Ex : 1234 then the Digital root will be 1+2+3+4 = 10


inputNumber = 5674
sum = 0
num=inputNumber 
while num > 0:
    sum = sum + (num % 10)
    num = int(num / 10)
print(f'Digital root of {inputNumber} is : {sum}')
