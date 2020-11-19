plainText=input("Enter Plain Text: ")
plainText=plainText.upper()


#############----------REMOVING SP.CHARS------------###########

pt=""
for i in plainText:
    if(i.isalpha()):
        pt+=i
print("Plain Text Without Sp.Chars: ",pt)
#print(len(pt))


#############----------KEY GENERATION------------###########

key=input("Enter Key: ")
key=key.upper()
#print(len(key))

if(len(key)>=len(pt)):
    key=key[0:len(pt)]
elif(len(key)<len(pt)):
    for i in range(len(pt)-len(key)):
            key+=key[i]

#print("Key Generated: ",key)
    
#############----------ENCRYPTION------------###########

key=list(key)
pt=list(pt)
pt2=list(plainText)
ct_list=[]
cipherText=""

for (a,b) in zip(pt,key):
    ct_list.append(chr(((ord(a)-65)+(ord(b)-65))%26+65))
#for i in ct_list:
#    ct+=i
#print("raw ct:",ct)

counter=0
for i in range(len(pt2)):
    if(pt2[i].isalpha()):
        pt2[i]=ct_list[counter]
        counter+=1
for i in pt2:
    cipherText+=i
print("Encrpted Text: ",cipherText)

#########----REMOVING SP.CHARS FROM CIPHER TEXT FOR DECRYPTION-------#########

ct=""
for i in cipherText:
    if(i.isalpha()):
        ct+=i
print("Cipher Text Without Sp.Chars: ",ct)

#############----------DECRYPTION------------###########

key=list(key)
ct=list(ct)
ct2=list(cipherText)
pt_list=[]
pt=""
plainText=""


for (a,b) in zip(ct,key):
    pt_list.append(chr(((ord(a)-65)-(ord(b)-65))%26+65))
#for i in ct_list:
#    ct+=i
#print("raw ct:",ct)

counter=0
for i in range(len(ct2)):
    if(ct2[i].isalpha()):
        ct2[i]=pt_list[counter]
        counter+=1
for i in ct2:
    plainText+=i
print("Decrypted Text: ",plainText)




