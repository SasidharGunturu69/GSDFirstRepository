31 Jan 2024
a = 10
b = 'c'
c = 2.10
d = 2 + 3j
# a='abc'
e = c + a
f = 20
print(a, b, c, d, e, f, a // f)
g = True
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g))
# print(help(string))

a = 10
b = "abc"
c = 20.15
print(a, b, c)

TEST_LIST = [1, 2, 3, 4, 5]
L2 = ['abc', 'def', 'ghi']
print(TEST_LIST)
L2.append('jkl')
print(L2)
L2.insert(4, "mno")
print(L2)
L3 = TEST_LIST + L2
print(L3)
# print(L2[0] + TEST_LIST[0])

L1 = [1, 2, 3, 4, 5]
L2 = ['Ram', 'Raj', 'Shiva', 'Sai', 'Jaya']
L1 = L1 + L2
print(L1)

name_str = 'Witty'
for i in range(1, 6):
    print(name_str)

for i in range(1, 6):
    print(i)

print("1 to 5 without 3")

for i in range(1, 6):
    if i != 3:
        print(i)
#   else:
#       continue

# write a python program to find those numbers which are divisible by 7 and multiples of 5
# between 1500 and 2700
mult7n5=[]
for num in range(1500,2701):
    if (num%7 == 0) :
        if (num%5 == 0) :
            print (num,"is divisible by 7 and a multiple of 5")
            mult7n5.append(num)
        else:
            print (num,"is divisible by 7 and NOT a multiple of 5")
    else:
        print (num,"is not divisible by 7")
print(mult7n5)

# write a python program to find even/odd numbers
num_list=[-34,45,76,-31,9,85,22,55,-60,100]
for num in num_list:
    if num%2:
        print (num, "is odd")
    else:
        print (num,"is even")
# write a python program to find negative and positive integers
    if num<0:
        print (num, "is negative")
    else:
        print (num, "is positive")

# write a python that prints 0 to 6 except 3,6
for num in range(0,7):
    if (num !=3 and num != 6):
        print (num)

#Fibonacci Series
prev_prev_num=1
prev_num=1
next_num=prev_num + prev_prev_num
fib_list=[]
fib_list.append(prev_prev_num)
fib_list.append(prev_num)
fib_list.append(next_num)
for num in range (0,20):
    prev_num = next_num
    next_num = prev_num + prev_prev_num
    prev_prev_num = prev_num
    fib_list.append(next_num)
    print(num+1,':',fib_list[num],'',end= '')
print("\nEnd Lengthy Code")

x,y=0,1
num=0
while num<20:
    num += 1
    print(y, "", end='')
    x,y=y,x+y
print("\nEnd brief Fibonacci code")

x = "salil"
y = "Ajay"
print (x +" "+ y)
x,y = y,x
print (x +" "+ y)


def factorial(n):
    return 1 if (n == 0) else n * factorial(n - 1)

result = factorial(5)
print(result)

seq_num=[]
def printer():
    counter = 100
    rslt_counter = 0
    while (counter):
        if ((counter%2) and (counter%5)):
            print(counter,end=' ')
            rslt_counter = rslt_counter + 1
            seq_num.append(counter)
        counter = counter - 1
    print("\nTotal values are",rslt_counter)

printer()
print(seq_num)

x=2
y=3
#x=int(input("Enter value of x"))
#y=int(input("Enter value of y"))

print("Sum is", x+y)


print(seq_num)

x=2
y=3
def prod_val(x,y):
    print("product is", x*y)

#x=int(input("Enter value of x"))
#y=int(input("Enter value of y"))

prod_val(x,y)

x=0
y=1
print(x, end= ' ')
print(y, end= ' ')
#print(x+y)
for i in range(0,15):
    #print(i)
    c=x+y
    x=y
    y=c
    print(c, end= ' ')

print("\n")


a=[5,1,4,3,2,20,10,16,98,95,5,11,84,32]
srt_list=a
print("Unsorted List",a)
for cntr1 in range(0,len(a)):
    for cntr2 in range(0,len(a)):
        if ( srt_list[cntr1] <= srt_list[cntr2]):
            #swapVal=srt_list[cntr2]
            #srt_list[cntr2]=srt_list[cntr1]
            #srt_list[cntr1]=swapVal
            srt_list[cntr1],srt_list[cntr2] = srt_list[cntr2],srt_list[cntr1]
print("Sorted List",srt_list)

#from collections import OrderedDict
#def occurences_count_words(n, words):
#    count_words = OrderedDict()
#    for word in words:
#        if word in count_words:
#            count_words[word] += 1
#        else:
#            count_words[word] = 1
#    distinct_count_words = len(count_words)
#    occurence_words_list = list(count_words.values())
#    print(distinct_count_words)
#    print(" ".join(map(str, occurence_words_list)))
#n = int(input("Enter No. of words: "))
#for i in range(0, n):
#    words = input("Enter String: ").split(" ")
#print("No. of words ", n,"Words are:", words)
#occurences_count_words(n,words)
