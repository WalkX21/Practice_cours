
# def chaos(): #definit la fonction chaos
#     print("This program illustrates a chaotic function ")
#     x = float(input("Enter a number between 0 and 1")) #demande un nombre entre 0 et 1 et le converti si possible en float
#     for i in range(10): 
#         x = 3,9 * x * (1-x) # formule du nombre du chaos
#         print(x) #affiche le resultat  

# chaos()

#--------------------------------
x = 0.7678
def twofois():
    print("Ce program multipli les nombres par deux")
    x = float(input("enter a number between 2 and 9"))
    for i in range(10):
        x = x * 2
        print(x)
    
twofois()
print(type(x))
