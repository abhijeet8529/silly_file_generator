import sys, random
print("Welcome to the Psych 'Sidekick Name Picker.'\n")
print("A name just like your friend would pick for friend:\n")

first = ('chotu','chetan','butt','fart','snakes','stinky','squirts',
         'lamba','shorty','skinny','bald','black')

last = ('Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'white hair')


while True:
    firstname= random.choice(first)
    lastname = random.choice(last)

    
    print("\n")
    print(firstname +' '+ lastname,file= sys.stderr)
    print('\n')
    
    tryagain = input("\nTry again or quit(press n to quit or Enter to continue)\n")
    if tryagain.lower()== 'n':
        break

input("\n press Enter to exit")