#import secrets
pt=input("Enter PlainText: ") 
ct_list=[]                                      # Created an empty array to append positions of alphabets
ct=""
pt=pt.upper()
l=len(pt)
pt=list(pt)

key=""

#for i in range(len(pt)):
#    key+=secrets.choice('abcdefghijklmnopqrstuvwxyz')
#print("Key: ",key)


sp_pos={}                                       # Created an empty dictionary to store positions of special characters
ref=[]

for i in pt:  
    if((ord(i)<65 or ord(i)>90)and ord(i)!=32): # Special Characters range from (32 to 64), (91 to 96) & (123 to 127)
        sp_pos.update({i:pt.index(i)})          # Adding special characters to dictionary with value as their position in string
        pt.remove(i)                            # Removing special characters  from plaintext
print(pt)

while(len(key)!=len(pt)):                       # Mandates key to be equal to plaintext excluding sp.chars
    print("KEY SHOULD BE EQUAL TO PLAINTEXT")
    key=input("Enter Key: ")
    
key=key.upper()
key=list(key)
#print(sp_pos)

        

#########---------------ENCRYPTION-----------------##########


for(a,b)in zip(pt,key):                         # Appending positions of cipher alphabets to ct_list
    if(ord(a)>=65 and ord(a)<=90):
        ct_list.append((ord(a)-65)+(ord(b)-65))
    else:
        ct_list.append(a)

#print("raw: ",ct_list)
for i in range(len(ct_list)):
    if(ct_list[i]!=" "):                        # Done to maintain space in between words of cipher text same as plain text
        ct_list[i]=chr((ct_list[i])%26+65)      # Replaces each position with its respective character
    else:
        ct_list[i]=" "


for i,j in sp_pos.items():                  
    if(j>=len(ct_list)):
        ct_list.insert(j+1,i)
    else:
        ct_list.insert(j,i)                     # Inserts Special chars at required positions( value in dict) in list    
    print(ct_list)    

for i in ct_list:                               # Iterates over ct_list to add alphabets to empty string
    ct+=i

print("ENCRYPTION: ",ct)                        # Prints encrypted text ct

#########---------------DECRYPTION-----------------##########

pt=""
sp_pos={}
ct=list(ct)

for i in ct:
    if((ord(i)<65 or ord(i)>90)and ord(i)!=32): #Special Characters range from (32 to 64), (91 to 96) & (123 to 127)
        sp_pos.update({i:ct.index(i)})          # Adding special characters to dictionary
        ct.remove(i)                            # Removing special characters  from plaintext
#print(sp_pos)
        
ct_list=[]                                      # Re-Initiated an empty array
for (a,b) in zip(ct,key):
    if(ord(a)>=65 and ord(a)<=90):
        ct_list.append((ord(a)-65)-(ord(b)-65))
    else:
        ct_list.append(a)
for i in range(len(ct_list)):
    if(ct_list[i]!=" "):                        # Done to maintain space in between words of plain text same as cipher text
        ct_list[i]=chr((ct_list[i])%26+65)      # Replaces each position with its respective character
    else:
        ct_list[i]=" "

for i,j in sp_pos.items():
    if(j>=len(ct_list)):
        ct_list.append(i)
    else:
        ct_list.insert(j,i)                         # Inserts Special chars at required positions( value in dict) in list    

for i in ct_list:                               # Iterates over ct_list to add alphabets to empty string
    pt+=i
print("DECRYPTION: ",pt)                        # Prints plain text same as input
