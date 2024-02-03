# generate a random pw with a combination of %, ',' and parentheses
# lower-case, upper-case alphabets and numbers.
import string
import random
pw_length = int(input('Enter password length: '))
#asking for length of the pw.
print('''Choose character set for pw from these: 
1. Letters
2. Digits
3. Special characters
4. Exit when done choosing''')

character_list = ''

#getting the character set
while True:
    choice = int(input('Enter a number from the character set above: : '))
    if choice == 1:
        character_list += string.ascii_letters #adding letters
    elif choice == 2:
        character_list += string.digits #adding digits
    elif choice == 3:
        character_list += string.punctuation #adding special characters
    elif choice == 4:
        break
    else:
        print('Invalid selection. Pick another one!')
pw = []

for i in range(pw_length):
    random_char = random.choice(character_list) #creating random characters
    pw.append(random_char) #adding random character to the pw

print('The random pw is:' + "".join(pw))