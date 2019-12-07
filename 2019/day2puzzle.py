import os

working_directory = os.path.dirname(__file__)
input_file_path = working_directory + '/day2input.txt'
with open(input_file_path) as fp:
    memory = eval("[" + fp.readline() +"]")
    for noun in range(0,99):
        program = memory[:]
        program[1] = noun # noun
        program[2] = 85 # verb
        i = 0
        while i < len(program):
            if  program[i] == 99:
                # print("0 : " + str(program[0]))
                break
            elif program[i] == 1:
                program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
            elif program[i] == 2:
                program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
            i+=4
        if program[0] == 19690720:
            print("noun = " + str(noun))
            break
            
