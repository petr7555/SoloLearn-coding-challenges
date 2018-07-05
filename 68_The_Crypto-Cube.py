import math, random

text = "Programming in Python is awesome!"
while len(text)%8 != 0:
    text = text + " "
num_cubes = len(text)//8
cubes = [[text[j+i*8] for j in range(8)] for i in range(num_cubes)]
print("Number of cubes: {}".format(num_cubes))
for i in range(num_cubes):
    print("Cube n. {}: {}".format(i+1, cubes[i]))

def left(cube):
    shifted_cube = []
    seq = [3,2,6,7,0,1,5,4]
    for i in range(8):
        shifted_cube.append(cube[seq[i]])
    return shifted_cube

def right(cube):
    shifted_cube = []
    seq = [4,5,1,0,7,6,2,3]
    for i in range(8):
        shifted_cube.append(cube[seq[i]])
    return shifted_cube

def up(cube):
    shifted_cube = []
    seq = [4,0,3,7,5,1,2,6]
    for i in range(8):
        shifted_cube.append(cube[seq[i]])
    return shifted_cube

def down(cube):
    shifted_cube = []
    seq = [1,5,6,2,0,4,7,3]
    for i in range(8):
        shifted_cube.append(cube[seq[i]])
    return shifted_cube
    
#5-10 random moves for each cube
possible_rotations = ["L","R","U","D"]
all_cubes_moves = [[random.choice(possible_rotations) for j in range(random.randint(5,10))] for i in range(num_cubes)]
for i in range(num_cubes):
    print("Moves for cube n. {}: {}".format(i+1, all_cubes_moves[i]))


encrypt_dic = {"L":left, "R":right, "U":up, "D":down}
decrypt_dic = {"L":right, "R":left, "U":down, "D":up}
def encrypt(cubes, all_cubes_moves):
    for i in range(len(all_cubes_moves)):
        for move in all_cubes_moves[i]:
            cubes[i] = encrypt_dic[move](cubes[i])
    return cubes
def decrypt(cubes, all_cubes_moves):
    for i in range(len(all_cubes_moves)):
        for j in range(len(all_cubes_moves[i])):
            cubes[i] = decrypt_dic[all_cubes_moves[i][-j-1]](cubes[i])
    return cubes
def read(cubes):
    text = ""
    for cube in cubes:
        text = text + "".join(cube)
        #or: text = text + "".join("".join(cube).split())       
    return text

print("Original text: {}".format(read(cubes)))
cubes = encrypt(cubes,all_cubes_moves)
print("Encrypted text: {}".format(read(cubes)))
cubes = decrypt(cubes,all_cubes_moves)
print("Decrypted text: {}".format(read(cubes)))
