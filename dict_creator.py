import itertools

path = "/home/user/Downloads/dict.txt"
list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0"
, "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def convertTuple(tup):
    str = ""
    for item in tup:
        str = str + item
    return str

with open(path, "w") as f:
    for length in range(len(list)+1):
        for x in itertools.combinations(list, length):
            x = convertTuple(x) + "\n"
            f.write(x)