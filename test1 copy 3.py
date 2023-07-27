print('SOmething #')


#create a list
ages = [1,2,3]
alpha = ['a','b','c']
odd = []
hieghst = ages[0]
#cretaing variables
x = 45
y = 2
ans = x + y
#a function that returns the largest element in an array 
#ages.count()

for i in ages:
    if i > hieghst:
        hieghst = i
    else:
        print(hieghst)        
#Write a function that reverses a list (Array)
ages.reverse()

#Write a function that checks whether an element occurs in a list.
print(2 in ages)

#Write a function that returns the elements on odd positions in a list.
i = odd #create an empty array as a placeholder for odd numbers
for i in ages:
    if i % 2 != 0:
        odd.append(i)
print(odd)


#Write 2 functions that compute the sum of the numbers in a list: using a for-loop and a while-loop
for item in ages:
    print(sum(ages))

count = 0
while ages == count:
    print(sum(ages))
    count =+ 1
#Write a function that concatenates two lists. For example [a, b, c], [1, 2, 3] becomes – [a, b,c, 1, 2, 3]
print((ages + alpha))

#Write a function that combines two lists by alternatingly taking elements, e.g. [a, b, c], [1, 2,3] becomes – [a, 1, b, 2, c, 3].
# hit = ((ages + alpha))
# hit [0] = 'a'
# hit [1] = '7'
# hit [2] = 'b'
# hit [3] = '6'
# hit [4] = 'c'
# hit [5] = '5'
# hit [6] = '4'
# hit [7] = '3'
# hit [8] = '2
# hit [9] = '1'
# print(hit)
hit = []
for i in range(len(ages)):
    hit.append(ages[i])  #we use the [] to access an item in a list/array
    hit.append(alpha[i])    #we use the [] to access an item in a list/array
print(hit)
#Write a function that sorts a list of numbers in ascending order.
ages.sort()

print(ages)



print(4567)