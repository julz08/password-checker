from hashlib import shake_128


test = 'James'
first_char = test[0]

print(first_char.isupper())

# islower()

test.find('a')
print(test.find('a'))
# returns index if it finds it

# step 1: 
r1 = False
r2 = False
r3 = False
password = input('give me a password ')

if 'z' in password: # finds z
    r1 = True
    print('Password contains z.')
else:
    print("Your password DOES NOT contain a 'z'!")

if password[-1] == "!": # checks if ends with !
    r2 = True
    print('Password ends with an exclamation mark')
else:
    print("Your password DOES NOT end with an exclamation mark!")
    
fc_pass = password[0]
if fc_pass.isupper() == True: # checks if stars with uppercase letter
    r3 = True
    print('Password starts with an uppercase.')
else:
    print("Your password DOES NOT start with an uppercase!")

if r1 == True and r2 == True and r3 == True:
    print('Accepted password!')
else:
    print('Rejected password.')
    
# step 2:
s1 = False
s2 = False
s3 = False
s4 = False
s5 = False
pro_pass = input('give me an proper password! ')
if len(pro_pass) > 7 and len(pro_pass) < 16:
    print('Password has more than 7 letters and less than 16 characters')
    s1 = True
else:
    print('Your password is NOT more than 7 letters and less than 16 letters.')

specialchar = '!@#$%^&*(){}?/_+-=[]><~`;:\|'
for i in pro_pass:
    if i.islower() == True: # checks for a lowercase character
        s2 = True
    if i.isupper() == True: # checks for an uppercase character
        s3 = True
    if i.isdigit() == True: # checks for a number
        s4 = True
    if i in specialchar: # checks for a symbol
        s5 = True
        
if s2 == True: #feedback to user's password
    print('Password includes a lowercase character')
else:
    print('Your password DOES NOT include a lowercase character')
if s3 == True:
    print('Password includes a uppercase character')
else:
    print('Your password DOES NOT include a uppercase character')
if s4 == True:
    print('Password includes a number')
else:
    print('Your password DOES NOT include a number')
if s5 == True:
    print('Password includes a symbol')
else:
    print('Your password DOES NOT include a symbol')
    
    
if s1 == True and s2 == True and s3 == True and s4 == True and s5 == True:
    print('Accepted password!')
else:
    print('Rejected password.')

    


