

#create a list
#cretaing variables

def get_highest_number(arr):
    highest = -1000000000000000
    for i in arr:
        if i > highest:
            highest = i

    return highest    
         
ages = [97 ,  14 ,  65 ,  63 ,  88 ,  53 ,  59 ,  98 ,  31 ,  74 ]

h = get_highest_number(ages)
print(h)        
#Write a function that reverses a list (Array)
