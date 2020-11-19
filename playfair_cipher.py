import numpy as np

############---------GENERATION OF EMPTY 5x5 MATRIX---------###########

mat=np.zeros((5,5),dtype=str)
print("Empty Matrix: ")
print(mat)

############---------TAKING PLAINTEXT INPUT & REMOVING SP.CHARS---------###########

plainText=input("Enter PlainText: ")
plainText=plainText.upper()
pt=""
for i in plainText:
    if(i.isalpha()==True):
        pt+=i
pt=pt.replace("J","I")   #replacing all j with i in plaintext
print("Plain Text without Sp.chars: ",pt)

############---------TAKING KEY INPUT & REPLACING ALL J WITH I---------###########

KEY=input("Enter Key: ")
KEY=KEY.upper()
key=''
for i in KEY:
    if(i.isalpha()==True):
        key+=i

key=key.replace('J','I')

############---------REMOVING DUPLICATE LETTERS FROM KEY---------###########

key2=key
key2=list(key2)
key2=list(dict.fromkeys(key2))

print("Key without duplicates: ",key2)
print("\n")

############---------PUTTNG ALPHABETS INTO PLAYFAIR MATRIX---------###########
#pt2=pt2.reverse()
alpha=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P',
          'Q','R','S','T','U','V','W','X','Y','Z']
alpha2=[]
for i in alpha:
    if(i not in key2):
        alpha2.append(i)        
print("Alphabets apart from key \n",alpha2) # List of alphabets excuding key alphabets


counter=len(key2)           # Filling the empty matrix with alphabets
cnt=0
cnt2=0
for i in range(5):
    for j in range(5):
        if(counter>0):
            mat[i][j]=key2[cnt]
            cnt+=1
            counter-=1
        else:
            mat[i][j]=alpha2[cnt2]
            cnt2+=1
print("\n Playfair Matrix: ")
print(mat)

############---------BREAKING OF PLAINTEXT INTO PAIRS OF 2---------###########

if(len(pt)%2!=0):           # To pair up single letter with X
    pt+='X'
else:
    pt=pt

pt2=list(pt)
cnt=0                       # To replace duplicate letter with X
while(cnt<len(pt2)):
    if(pt2[cnt]==pt2[cnt+1]):
        pt2[cnt+1]="X"
    cnt+=2

print("Plain Text before pairing: ",pt2)

pair_mat=pt2                # Only to show pair formation
#print(pair_mat)
pair_mat=np.array(pair_mat).reshape(int(len(pair_mat)/2),2)
print("\n Breaking of Plain Text into pairs:")
print(pair_mat)

############---------ENCRYPTION---------###########
#cipher=dict()
cipher=[]
#pt2=list(pt)

#print("\n ",pt2)
ct=""
cnt=0
def char_pos(mat,pt2):      #for finding positions of plaintext alphabets in key matrix
    x,y=0,0
    for i in range(5):
        for j in range(5):
            if(mat[i][j] in pt2):
                #print(pt2[cnt])
                x=i
                y=j
                #print(mat[i][j],":",(x,y))
    return x,y
            #cipher.update({mat[i][j]:(x,y)}) (not to refer)
            
counter=0
while(counter<len(pt2)):
    p1,q1=char_pos(mat,pt2[counter])
    p2,q2=char_pos(mat,pt2[counter+1])
    
    #print((p1,q1),' ',(p2,q2))
    if(p1==p2):                 # Same row case
        if(q1==4):              # If column position is 4
            q1=-1               # Bring to -1(last) so to form a circular list
        if(q2==4):              # Same
            q2=-1               # Same
        cipher.append(mat[p1][q1+1])
        cipher.append(mat[p2][q2+1])
    elif(q1==q2):               # Same column case
        if(p1==4):              # If row position is 4
            p1=-1               # Bring to -1(last) so to form a circular list
        if(p2==4):              # Same
            p2=-1               # Same
        cipher.append(mat[p1+1][q1])
        cipher.append(mat[p2+1][q2])
    else:
        cipher.append(mat[p1][q2]) # Rectangular opposite case
        cipher.append(mat[p2][q1]) 
    counter+=2
for i in cipher:
    ct+="".join(i)
print("\nENCRYPTED TEXT: ",ct)
#print(cipher)
    
############---------DECRYPTION---------###########
ct2=list(ct)
plaintext=[]
ptext=""
counter=0

while(counter<len(ct2)):
    p1,q1=char_pos(mat,ct2[counter])
    p2,q2=char_pos(mat,ct2[counter+1])
    
    #print((p1,q1),' ',(p2,q2))
    if(p1==p2):                 # Same row case
        if(q1==4):              # If column position is 4
            q1=-1               # Bring to -1(last) so to form a circular list
        if(q2==4):              # Same
            q2=-1               # Same
        plaintext.append(mat[p1][q1-1])
        plaintext.append(mat[p2][q2-1])
    elif(q1==q2):               # Same column case
        if(p1==4):              # If row position is 4
            p1=-1               # Bring to -1(last) so to form a circular list
        if(p2==4):              # Same
            p2=-1               # Same
        plaintext.append(mat[p1-1][q1])
        plaintext.append(mat[p2-1][q2])
    else:
        plaintext.append(mat[p1][q2]) # Rectangular opposite case
        plaintext.append(mat[p2][q1]) 
    counter+=2


for i in plaintext:
    ptext+="".join(i)
print("DECRYPTED TEXT: ",ptext)
            
