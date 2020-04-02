def occurence(arg: str) -> dict:
    xyz = {}
    word = arg
    for x in word:
        if x in xyz:
            xyz[x] +=1
        else: 
            xyz[x] = 1
    print(xyz)
