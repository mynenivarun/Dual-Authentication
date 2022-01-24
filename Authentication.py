from hashlib import sha512
print('enter name')
name = input()
print('enter password')
pas = input()
s1=name+pas
newhash = sha512(s1 .encode()).hexdigest()
print(newhash)

name1 = 'admin'
pas1 = 'test'
s2=name1+pas1
deafulthash = sha512(s2 .encode()).hexdigest()
print(deafulthash)

if(name==name1 and pas == pas1):
    print('Regular Validation Successful')
    if(newhash == deafulthash):
        print('user authentication Successful')
    else:
        print('user authentication unSuccessful')
else:
    print('Regular Validation Failed')
