import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

## lire un fichier de données
f = open("parabole.csv")
sep=";" #caractère séparateur du csv -peut être une virgule, un point-virgule ou une tabulation noté \t 
data=f.readlines() #on lit toutes les lignes et on met ça dans une liste -un élément par ligne-
f.close() #on referme le fichier

data=data[3:] #on supprime les lignes d'en-tête qui ne nous intéressent pas, le 3 peut être modifié en fonction des besoins

#on construit les listes de valeurs utiles
t=[]
x=[]
y=[]
for ligne in data:
    ligne=ligne.replace(",",".") #change les virgules en point => format numérique différent sur excel et sur python
    ligne=ligne.strip().split(sep) #on sépare les différents élément en utilisant le caractère séparateur défini
    ligne=list(map(float,ligne)) #on converti chaque élément en flottant
    t.append(ligne[0]) #on rentre les valeurs dans les lites adaptées
    x.append(ligne[1])
    y.append(ligne[2])

## Modelisation


def affine(x,a,b):
    return a*x+b

def lineaire(x,a):
    return a*x

def parabole(x,a,b): #on impose c = 0 sinon il faut utiliser l'autre
    return a*x**2 + b*x

#def parabole(x,a,b,c):
#   return a*x**2 + b*x + c

params1=curve_fit(affine,x,y)
#params3=curve_fit(lineaire,x,y)
params2=curve_fit(parabole,x,y)

m1=[]
m2=[]
#m3=[]
for val in x:
    m1.append(affine(val,params1[0][0],params1[0][1]))
    m2.append(parabole(val,params2[0][0],params2[0][1]))
    #m3.append(lineaire(val,params3[0][0]))

plt.plot(x,y,"+",label="trajectoire Y = f(X)")
plt.plot(x,m1,label="modele1 Y = {:.3f} X + {:.3f}".format(params1[0][0],params1[0][1]))
plt.plot(x,m2,label="modele2 Y = {:.3f} X\u00B2 + {:.3f} X".format(params2[0][0],params2[0][1]))
#plt.plot(t,m3)
plt.legend()
plt.title("modélisation de la trajectoire d'une balle")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.show()
##
