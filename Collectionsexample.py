from collections import defaultdict

#different from the dict , you don't have to check the key

colors = (('Yasoob','Yellow'),('Ali','Blue'),('Arma','Pink'),('Ali','Green'),('Yasoob','Red'),('Arma','Yellow'))

favourite_colours = defaultdict(list)

for name,color in colors:
    favourite_colours[name].append(color)

print(favourite_colours)