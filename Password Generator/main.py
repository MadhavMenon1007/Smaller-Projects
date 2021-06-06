import random

list_upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

list_lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

list_num=[0,1,2,3,4,5,6,7,8,9]

list_symbols=["~","!","@","#","$","%","^","&","*", ",","-","+","=","_","|",":",";","<",">","?"]


num1=random.randint(0,(len(list_upper)-1))
num2=random.randint(0,(len(list_lower)-1))
num3=random.randint(1,(len(list_num))-1)
num4=random.randint(1,(len(list_symbols))-1)


num5=random.randint(0,(len(list_upper)-1))
num6=random.randint(0,(len(list_lower)-1))
num7=random.randint(1,(len(list_num))-1)
num8=random.randint(1,(len(list_symbols))-1)


num9=random.randint(0,(len(list_upper)-1))
num10=random.randint(0,(len(list_lower)-1))
num11=random.randint(1,(len(list_num))-1)
num12=random.randint(1,(len(list_symbols))-1)


num13=random.randint(0,(len(list_upper)-1))
num14=random.randint(0,(len(list_lower)-1))
num15=random.randint(1,(len(list_num))-1)
num16=random.randint(1,(len(list_symbols))-1)


def create_password():
    password=""
    password=(list_upper[num1]+list_lower[num2]+str(list_num[num3])+list_symbols[num4])
    password+=(list_lower[num6]+list_symbols[num8]+str(list_num[num7])+list_upper[num5])
    password+=(list_upper[num9]+str(list_num[num11])+list_lower[num10]+list_symbols[num12])
    password+=(str(list_num[num15])+list_upper[num9]+list_symbols[num16]+list_lower[num14])
    return password



print(create_password())
