min = int(input('hur många minuter ringer du per månad?'))
if min < 32:
    print ('Kontant')
elif min > 67:
    print ('plus')
else:
    print('Normal')


#det här fungerar också men är mer text och ser sämre ut, har även en högre risk för fail4mnmrrrrrrrrqwerqwerqwerqwerqwerqwer
#ring = input('Ringer du 33min,66min eller mer per månad?')
#if ring == '33min': 
 #   print('Då bör du välja Kontant')
#if ring == '66min':
 #   print('Då bör du välja Normal')
#if ring == 'mer':
 #   print('Då bör du välja Plus')
#else:
 #   print('Svara med "33min","66min" eller "mer" för att få fram vilket alternativ som passar dig')