# Weight : 170
# (K)g or (L)bs : l

# Weight in Kg: 76.5 

weight = int(input('Weight: '))
unit = input('(K)g or (L)bs: ')

if unit.upper() == 'K' :
    converted = weight/ 0.45
    print('Weight in Lbs: ' + str(converted))
else:
    converted = weight * 0.45
    print('Weight in Kgs: ' + str(converted))