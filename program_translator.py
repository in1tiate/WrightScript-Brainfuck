import io

# Clear files
open('program.txt', 'w').close()
open('input_formatted.txt', 'w').close()

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

inputtxt = open('input.txt', 'r')
inputfmt = open('input_formatted.txt', 'w')
index = 1
while 1:
    char = inputtxt.read(1)
    if not char:
        break
    line = "set chr" + str(index) + " " + char + "\n"
    inputfmt.write(line)
    index = index + 1
inputfmt.write("set chr" + str(index) + " END" + "\n")
