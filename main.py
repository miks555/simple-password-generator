import string
import random
def gen_pass(length_1, characters_1, seed_1):
	if seed_1 is None:
		return ''.join(random.SystemRandom().choice(characters_1) for _ in range(length_1))
	else:
		random.seed(seed_1)
		return ''.join(random.choice(characters_1) for _ in range(length_1))
ascii_printable_with_space = ""
for char in range(32, 127):
	ascii_printable_with_space += chr(char)
easy = '!#%+23456789:=?@ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
visually_aggressive = '!"#$%&\'()*+,-./23456789:;<=>?@ABCDEFGHJKLMNOPRSTUVWXYZ[\]^_abcdefghijkmnopqrstuvwxyz{|}~'
characters_0=easy
length_0=100
seed_0 = None
print("Select characters set:")
print("1 (easy) = ")
print(easy)
print("2 (visually_aggressive) = ")
print(visually_aggressive)
print("3 (ascii_printable_with_space) = ")
print(ascii_printable_with_space)
print("If you are generating random passwords, it's a good idea to avoid characters that can be confused for others (easy or visually_aggressive):")
flag_0=int(input())
if(flag_0==1):
	characters_0=easy
if(flag_0==2):
	characters_0=visually_aggressive
if(flag_0==3):
	characters_0=ascii_printable_with_space
print("Type characters to remove, enter to skip:")
characters_0 = characters_0.replace(input(), "")
print("Selected characters:")
print(characters_0)
print("Type password length:")
length_0 = int(input())
print("If a seed is provided, the password can be replicated. Otherwise, the system uses entropy, such as mouse movement or fan speed variation, depending on the system's implementation:")
print("1 (type seeds)")
print("2 (no seeds)")
flag_1=int(input())
print("Number of passwords to generate:")
for i in range(int(input())):
	if(flag_1==1):
		print("Type seed ranging <-2147483648;2147483647>:")
		seed_0 = input()
		print("password "+str(i+1)+' =')
		print(gen_pass(length_0,characters_0,seed_0))
	else:
		print("password "+str(i+1)+' =')
		print(gen_pass(length_0,characters_0,seed_0))
