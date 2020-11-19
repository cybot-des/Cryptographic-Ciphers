import secrets
import random

plainText=input("Enter Plain Text: ")
plainText=plainText.upper()

################------------REMOVE SP. CHARS----------################
pt=""
for i in plainText:
    if(ord(i)>=65 and ord(i)<=90):
        pt+=i

print("Removing sp. chrs: ",pt)
################------------KEY GENERATION----------################

prefix=""
suffix=""

for i in range(len(pt)//2):
    prefix+=secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print("Prefix is: ",prefix)


rand_pt=random.sample(str(pt),(len(pt)-len(prefix)))

for i in rand_pt:
    suffix+=i
print("Suffix is: ",suffix)


Autokey=prefix+suffix
print("Autokey Generated: ",Autokey)

################------------ENCRYPTION-----------################

pt=list(pt)
ak=list(Autokey)
ct_list=[]
#pt2=list(plainText)
#pt2=plainText[::-1]
ct=""
#print(pt2)

for (a,b) in zip(pt,ak):
    if(ord(a)>=65 and ord(a)<=90):
        ct_list.append(chr(((ord(a)-65)+(ord(b)-65))%26+65))
    else:
        ct_list.append(a)
print(ct_list)

#['@','p','o','o','j','a','','d','e','s']

for i in ct_list:
    ct+=i
print("Encrypted Text: ",ct)
################------------DECRYPTION-----------################

ct=list(ct)
ak=list(Autokey)
ct_list=[]
#pt2=list(plainText)
#pt2=plainText[::-1]
pt=""
#print(pt2)

for (a,b) in zip(ct,ak):
    if(ord(a)>=65 and ord(a)<=90):
        ct_list.append(chr(((ord(a)-65)-(ord(b)-65))%26+65))
    else:
        ct_list.append(a)
print(ct_list)

#['@','p','o','o','j','a','','d','e','s']

for i in ct_list:
    pt+=i
print("Decrypted Text: ",pt)






