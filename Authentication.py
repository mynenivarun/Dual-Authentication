from hashlib import sha512
import getpass
name = input("Enter Name: ")
pas = getpass.getpass('Enter the password: ')
s1=name+pas
newhash = sha512(s1 .encode()).hexdigest()
print('\n Hash Value \n',newhash,'\n')

name1 = 'admin'
name2 = 'varun'
pas1 = 'test'
pas2 ='varun'
s2=name1+pas1
deafulthash = sha512(s2 .encode()).hexdigest()
print('\n Default Hash Value \n',deafulthash,'\n')

if((name==name1 and pas == pas1) or (name==name2 and pas == pas2)):
    print('Regular Validation Successful \n')
    if(newhash == deafulthash):
        print('User Authentication Successful \n')
    else:
        print('!!User Authentication Failed!! \n')
else:
    print('!!Regular Validation Failed!! \n')
