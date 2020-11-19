import numpy as np
pt=input("Enter Text: ")
pt=pt.upper()
pt=pt.replace(" ","")
l=len(pt)
print("No. of Rails: ",end="")
rails=int(input())


########-----REMOVING SP.CHARS-----#########

pt2=""
for i in pt:
    if(i.isalpha()==True):
        pt2+=i
print(pt2)
########-----GENERATING EMPTY MATRIX & INITIALIZING VARS-----#########
mat=np.zeros((rails,len(pt2)),dtype=str)
print(mat)
row=0
col=0
change_dir=0
ct=""
########-----ENCRYPTION-----#########

for i in range(len(pt2)):
    mat[row][i]=pt2[i]
    if(row==(rails-1)):
        change_dir=1
        
    elif(row==0):
        change_dir=0
        
    if(change_dir==1):
        row-=1
        
    elif(change_dir==0):
        row+=1
print("\n")        
print(mat,end="\n")

for i in range(rails):
    ct=ct+"".join(mat[i])

print("ENCRYPTION: ",ct)

########-----DECRYPTION-----#########

#ct="RUAOITTLEAL"
#print(ct)
#rails=int(input("Rails: "))

mat=np.zeros((rails,len(ct)),dtype=str)
print("Empty Matrix: ")
print(mat)
print("\n")

row=0
change_dir=None

for i in range(len(ct)):
    mat[row][i]="$"
    if(row==0):
        change_dir=True
        
    elif(row==(rails-1)):
        change_dir=False
        
    if(change_dir==True):
        row+=1

    elif(change_dir==False):
        row-=1
print("Marked Matrix: ")
print(mat)

ct2=list(ct[::-1])
print(ct2)
print("\n")
for i in range(rails):
    for j in range(len(ct)):
        if(mat[i][j]=="$"):
            mat[i][j]=ct2.pop()
print(mat)

pt=""
for i in range(len(ct)):
    for j in range(rails):
        if(mat[j][i].isalpha()):
            pt+=mat[j][i]
print("DECRYPTION: ",pt)






    
        
