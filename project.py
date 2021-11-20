import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
char = ['@','#','$','%','&','!','+']
num =[ '0','1','2','3','4','5','6','7','8','9']
passlen=0
charno=0
passlist = []

print("Hello!! Welcome to the passward generator")
input(print("press enter to get start"))

passlen = int(input("How many digits of passward do you want to create"))

intno = int(input("How many numbers do you want to add ?"))

a = input("do you want to add special charactor. Enter Y/N")
if a == 'N' or a == 'n':
  charno == 0
elif a == 'Y' or a == 'y':
  charno = int(input("How many special charactors do you want to add"))
else :
  print("you have entered a wrong key")

for i in range(0,charno):
    passlist.append(random.choice(char))
    # print(passward)
for i in range(0, intno):
    passlist.append(random.choice(num))
    # print(passward)
for i in range(0,passlen-intno-charno):
    passlist.append(random.choice(letters))
print(passlist)
random.shuffle(passlist)
passward =""
for char in passlist:
    passward+=char
print(f"your passward is: {passward}")
