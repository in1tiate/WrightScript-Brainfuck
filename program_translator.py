import io

# Clear file
open('program.txt', 'w').close()

programbf = open('program.bf', 'r')
programtxt = open('program.txt','w')
index = 1
while 1:
    char = programbf.read(1)
    if not char:
        break
    line = "set chr" + str(index) + " " + char + "\n"
    programtxt.write(line)
    index = index + 1
programtxt.write("set chr" + str(index) + " END" + "\n")
programtxt.close()
programbf.close()

