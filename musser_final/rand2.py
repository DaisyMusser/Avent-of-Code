## this program makes random rotor configurations i used for all three rotors in enigma.py 
import math, random, os, sys

def seeder():
    random.seed( os.urandom( 128 ) )
    return

def alphaomelette():
    x = []
    min = 1
    max = 26.999999 
    for i in range( 26 ):
        rnd = int( math.floor( (min-max)*random.random()+min ) )
        while rnd in x:
            rnd = int( math.floor( (min-max)*random.random()+min ) )
        x.append( rnd )
    # I dont know why but all the numbers where negative so this fixes that        
    for i in range(len(x)):
        x[i] = abs(x[i])
    return x

# main program
seeder()    # outside loop
blah = alphaomelette()
print( blah )
