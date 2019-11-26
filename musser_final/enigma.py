# README this program attempts to encrypt and decrypt messages following the same general principles of the german
# military version of the enigma machine (for details on the historical machine, find sources in README file included in
# this directory). The encrypt and decrypt modules are not working for some reason I cannot figure out, so ultimately
# this program doesn't really do anything useful

# WORKS the plug board was the first unit the message passed through, it let you connect two letters
# effectively swapping them. i didn't have time to make the plug setting adjustable by the user,
# so right now it's just a random (details below) default setting
def plugbrd(alpha, swp):
    x = 0
    y = 1
    # rand was made with the file rand.py file which seeds from urandom
    rand = [21, 13, 25, 20, 9, 15, 23, 5, 24, 1, 11, 12, 0, 4, 10, 7, 14, 22, 16, 2, 6, 3, 18, 8, 19, 17]
    for i in range(13):
        alpha = swp(alpha, rand[x], rand[y])
        x += 2
        y += 2
    return alpha


# WORKS the rotors are the next three units the message would pass through. different rotors had different
# wire configurations, and they could be swapped out from a box of five rotors (there is no equivalent
# of this in the code right now, but it would be a cool thing to add). in the code the wire
# configurations are random (details below)
def rotor1(alpha, rot, direction, setting):
    outAZ = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
    # this wire configuration was made by the rand.py file
    wires = [13, 17, 6, 16, 14, 22, 10, 4, 11, 15, 2, 18, 7, 5, 23, 8, 19, 21, 25, 0, 1, 12, 24, 3, 20, 9]
    for i in range(setting):
        wires = rot(wires)
    if direction == "forward":
        for i in range(26):
            outAZ[i] = alpha[wires[i]]
        return outAZ
    if direction == "backward":
        for i in range(26):
            outAZ[wires[i]] = alpha[i]
        return outAZ


# WORKS the same as rotor1 but with different wiring
def rotor2(alpha, rot, direction, setting):
    outAZ = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
    # this wire configuration was made by the rand.py file
    wires = [25, 12, 24, 1, 21, 22, 5, 6, 23, 13, 17, 19, 15, 7, 8, 3, 20, 10, 2, 4, 14, 18, 16, 0, 11, 9]
    for i in range(setting):
        wires = rot(wires)
    if direction == "forward":
        for i in range(26):
            outAZ[i] = alpha[wires[i]]
        return outAZ
    if direction == "backward":
        for i in range(26):
            outAZ[wires[i]] = alpha[i]
        return outAZ


# WORKS the same as rotor1 and 2 but with different wiring
def rotor3(alpha, rot, direction, setting):
    outAZ = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
    # this wire configuration was made by the rand.py file
    wires = [13, 10, 20, 0, 21, 22, 6, 16, 3, 8, 19, 17, 11, 2, 4, 12, 5, 9, 14, 15, 7, 18, 25, 24, 1, 23]
    for i in range(setting):
        wires = rot(wires)
    if direction == "forward":
        for i in range(26):
            outAZ[i] = alpha[wires[i]]
        return outAZ
    if direction == "backward":
        for i in range(26):
            outAZ[wires[i]] = alpha[i]
        return outAZ


# WORKS the reflector modifies the message before sending it backwards though the rotors and plugboard
# again. without this step all the encrypting done to the message would be undone when the message
# was sent backwards through the rotors and plugboard
def reflector(alpha, swp):
    # i couldn't find details on how the reflector actually modified the message, so i decided to
    # flip everything over the middle of the alphabet
    for i in range(13):
        alpha = swp(alpha, i, 25-i)
    return alpha


# WORKS pushes items in list up one and puts last item at start of list
def rotation(x):
    dupe = []
    for i in range(26):
        if i < 25:
            dupe.append(x[i+1])
        if i == 25:
            dupe.append(x[0])
    return dupe


# WORKS swaps the values at to locations on a list
def swap(x, a1, a2):
    hold = x[a1]
    x[a1] = x[a2]
    x[a2] = hold
    return x


# WORKS takes settings from the user
def settings():
    r1 = int(input("Set rotor1 [1-26]: "))
    r2 = int(input("Set rotor2 [1-26]: "))
    r3 = int(input("Set rotor3 [1-26]: "))
    return r1, r2, r3


# BROKEN should take a message and encrypt each letter with a uniquely scrambled alphabet. while it apears to be doing
# this the coded message it returns is not being successfully decrypted by the decryption mod, meaning one or both of
# the mods must be broken
def encrypt(plugbrd, rotor1, rotor2, rotor3, settings, swap, rotation):
    set1, set2, set3 = settings()
    click = 0
    mess = input("Message [no spaces]: ")
    mess = mess.upper()
    text = []
    for i in range(len(mess)):
        text.append(mess[i])
    for i in range(len(mess)):
        set1 += 1
        click += 1
        if 26 % click:
            set2 += 1
        if (26*26) % click:
            set3 += 1
        az = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        caz = plugbrd(az, swap)
        caz = rotor1(caz, rotation, "forward", set1)
        caz = rotor2(caz, rotation, "forward", set2)
        caz = rotor3(caz, rotation, "forward", set3)
        caz = reflector(caz, swap)
        caz = rotor3(caz, rotation, "backward", set3)
        caz = rotor2(caz, rotation, "backward", set2)
        caz = rotor1(caz, rotation, "backward", set1)
        caz = plugbrd(caz, swap)
        x = az.index(text[i])
        text[i] = caz[x]
    return text


# BROKEN should decrypt the coded message given if the same settings are used, but it doesn't work for some reason
# I can't figure out
def decrypt(plugbrd, rotor1, rotor2, rotor3, settings, swap, rotation):
    set1, set2, set3 = settings()
    click = 0
    message = input("Code [no spaces]: ")
    message = message.upper()
    text = []
    for i in range(len(message)):
        text.append(message[i])
    for i in range(len(message)):
        set1 += 1
        click += 1
        if 26 % click:
            set2 += 1
        if (26*26) % click:
            set3 += 1
        az = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        cAZ = plugbrd(az, swap)
        cAZ = rotor1(cAZ, rotation, "backward", set1)
        cAZ = rotor2(cAZ, rotation, "backward", set2)
        cAZ = rotor3(cAZ, rotation, "backward", set3)
        cAZ = reflector(cAZ, swap)
        cAZ = rotor3(cAZ, rotation, "forward", set3)
        cAZ = rotor2(cAZ, rotation, "forward", set2)
        cAZ = rotor1(cAZ, rotation, "forward", set1)
        cAZ = plugbrd(cAZ, swap)
        x = az.index(text[i])
        text[i] = cAZ[x]
    return text


#
# main program
#
x = input("Encrypt message? [y/n]: ")
if x == "y":
    code = encrypt(plugbrd, rotor1, rotor2, rotor3, settings, swap, rotation)
    print(code)
x = input("Decrypt code? [y/n]: ")
if x == "y":
    message = decrypt(plugbrd, rotor1, rotor2, rotor3, settings, swap, rotation)
    print(message)



