
input_filename = input('Enter Your Input FileName:')
output_filename = input('Enter Your output FileName:')
i =0
my_list=[]

for x in input_filename:
    i=i+1
    if i == 8:
        my_list.append('x')
    
    my_list.append(x)


    
    for z in my_list:
        if z == 'a' or 'i' or 'e' or 'o' or 'u':   
            my_list.append(2)

        else:
            continue
            #if z == 'a' :
               # my_list.pop('a')
               
'''
my_string =''.join(my_list)
print(my_string)
            #i = 0   
        #  while len(input_filename) != 7:
        #      i = i+1

'''







