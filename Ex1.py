#Q1
l=[17,38,10,25,72,45,14]
for p in l: 
    p=p+1
    print(p)
#Q2
l.append(13)
l.append(12)
print(l)
#Q3
z=l.index(72)
print(z)

#Q4
paire, impaire=[],[]
for nombre in l:
    if nombre%2:
        impaire.append(nombre)
    else:
        paire.append(nombre)
print ("nombres impaires: %s" % ", ".join([str(nb) for nb in impaire]))
print ("nombres paires: %s" % ", ".join([str(nb) for nb in paire]))
#for nombre in l:
    #if nombre%2==0:
        #print("impaires",nombre)
    #else:
        #print("paires", nombre)    
#Q5
l.insert(4,30)
print(l)
#Q6
l.remove(30)
print(l)
#Q7
l.reverse()
print(l)
#Q8
a=input("donner un nombre ")
if a==l:
    print("ce nombre est existe",l)
    
else:
    print("ce nombre n'existe pas ")

#Q9-10
a=l[2:4]
print("2 eme element au 3 eme element",a)
b=l[:3]
print("debut au 2 eme", b)
#Q11
print("la position du dernier element avec l'indice inverse",l[-1])

    

   



     
        
