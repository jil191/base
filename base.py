#Binary into Decimal 
fh = open('base.txt','w')
binary_number = input('Enter a number to convert into Decimal: ') 
n = int(binary_number , 2) 
fh.write(str(n)) 
fh.write('\n')
 
#Decimal into Binary 
n = int(input('Enter a number to convert into Binary: ')) 
abc = bin(n) 
fh.write(str(abc[2:]))
fh.close()