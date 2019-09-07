#this Program performe Division with out using / operator 
#purpose of this program is to understand how division works beside / operator


a = 390 #nomerator
b = 21 #denominator
count = 0
flag = False
a_is_greater = False
floating_pre = 0

if a > 0 and b > 0 and a > b:

    a_is_greater = True
    while b < a:
        while count*b <= a:
            count = count+1
            flag = True
        count = count - 1
        a = a - (count * b)
        print(count, end='')
        if flag == False:
            break
        else:
            count = 0
            flag = False



if b > 0 and a > 0 and b > a:

    if a_is_greater:
       print('.', end='')

    else:
        print('0.', end='')
    while a < b :
        floating_pre += 1
        while a < b:
            a = a * 10
        while b < a:
            while count * b <= a:
                count = count + 1
                flag = True
            count = count - 1
            a = a - (count * b)
            print(count, end='')
            if flag == False:
                break
            else:
                count = 0
                flag = False
        if floating_pre>5 or a == 0:
            break

