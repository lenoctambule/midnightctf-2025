with open("frozen.txt") as f :
    data = f.read().replace("\t", " ")
    logs = data.split("Audit ")
    for e in logs :
        if  "Result Code:  0x0" not in e :
            print(e)
            print("#" * 30)

# MCTF{trooper:asreproasting}
