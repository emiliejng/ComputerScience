import sys
#mode = None
if (sys.argv[1] == "cypher"):
    mode = "cypher"
elif (sys.argv[1] == "decypher"):
    mode = "decypher"
else:
    print(f"commande non supportee: {sys.argv[1]}")
    sys.exit(0)
key = sys.argv[2]
msg = sys.argv[3]

first_char = msg[0]
i=0
msg_ord=[]
for i in range(len(msg)):
    if(mode=="cypher"):
        msg_ord.append(ord(msg[i])+int(key))
    #print(msg[i])
    elif(mode=="decypher"):
        msg_ord.append(ord(msg[i])-int(key))
    i=i+1

print(msg_ord)

j=0
new_msg=""
for j in range(len(msg_ord)):
    new_msg=new_msg + chr(msg_ord[j])
    j=j+1

print(new_msg)

#print(ord(first_char))