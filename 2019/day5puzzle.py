import os

working_directory = os.path.dirname(__file__)
input_file_path = working_directory + '/day5input.txt'
with open(input_file_path) as fp:
    memory = eval("[" + fp.readline() +"]")
    # for noun in range(0,99):
    program = memory[:]
    # program[1] = 12 # noun
    # program[2] = 2 # verb
    i = 0
    while i < len(program):
        opcode = program[i] % 100
        if  opcode == 99:
            # print("0 : " + str(program[0]))
            break
        elif opcode == 1:
            x = 0
            y = 0
            opcodestr = str(program[i])
            if len(opcodestr) > 2 and opcodestr[-3] == "1":
                x = program[i+1]
            else:
                x = program[program[i+1]]
            if len(opcodestr) > 3 and opcodestr[-4] == "1":
                y = program[i+2]
            else:
                y = program[program[i+2]]
            program[program[i+3]] = int(x) + int(y)
            i+=4
        elif opcode == 2:
            x = 0
            y = 0
            opcodestr = str(program[i])
            if len(opcodestr) > 2 and opcodestr[-3] == "1":
                x = program[i+1]
            else:
                x = program[program[i+1]]
            if len(opcodestr) > 3 and opcodestr[-4] == "1":
                y = program[i+2]
            else:
                y = program[program[i+2]]
            program[program[i+3]] = int(x) * int(y)
            i+=4
        elif opcode == 3:
            program[program[i+1]] = int(input())
            print("Diagnostic outputs:\n\n")
            i+=2
        elif opcode == 4:
            opcodestr = str(program[i])
            if len(opcodestr) > 2 and opcodestr[-3] == "1":
                x = program[i+1]
            else:
                x = program[program[i+1]]
            print(x)
            i+=2
        elif opcode == 5:
            x = 0
            y = 0
            opcodestr = str(program[i])
            if len(opcodestr) > 2 and opcodestr[-3] == "1":
                x = program[i+1]
            else:
                x = program[program[i+1]]
            if len(opcodestr) > 3 and opcodestr[-4] == "1":
                y = program[i+2]
            else:
                y = program[program[i+2]]
            if x != 0:
                i = y
            else:
                i += 3
        elif opcode == 6:
            x = 0
            y = 0
            opcodestr = str(program[i])
            if len(opcodestr) > 2 and opcodestr[-3] == "1":
                x = program[i+1]
            else:
                x = program[program[i+1]]
            if len(opcodestr) > 3 and opcodestr[-4] == "1":
                y = program[i+2]
            else:
                y = program[program[i+2]]
            if x == 0:
                i = y
            else:
                i += 3
        elif opcode == 7:
            x = 0
            y = 0
            opcodestr = str(program[i])
            if len(opcodestr) > 2 and opcodestr[-3] == "1":
                x = program[i+1]
            else:
                x = program[program[i+1]]
            if len(opcodestr) > 3 and opcodestr[-4] == "1":
                y = program[i+2]
            else:
                y = program[program[i+2]]
            if x < y:
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
            i+=4
        elif opcode == 8:
            x = 0
            y = 0
            opcodestr = str(program[i])
            if len(opcodestr) > 2 and opcodestr[-3] == "1":
                x = program[i+1]
            else:
                x = program[program[i+1]]
            if len(opcodestr) > 3 and opcodestr[-4] == "1":
                y = program[i+2]
            else:
                y = program[program[i+2]]
            if x == y:
                program[program[i+3]] = 1
            else:
                program[program[i+3]] = 0
            i+=4
    

            
