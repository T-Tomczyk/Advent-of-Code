import re

with open('day08.txt') as file:
    my_input = file.read()

my_input = re.split(r'\n', my_input)
my_input = my_input[:-1]

for i in range(len(my_input)):
    my_input[i] = str(i) + ' ' + my_input[i]
    my_input[i] =  my_input[i].split()
    my_input[i][0] = int(my_input[i][0])
    my_input[i][2] = int(my_input[i][2])

# returns [terminated?, accumulator], e.g.:
# [False, 1475]
def program_runner(instructions_list):
    # Trying to execute this line means the program should terminate.
    instructions_list.append(0)

    accumulator = 0
    program_terminated = False

    instructions_run = []
    instruction_index = 0

    while instruction_index not in instructions_run:
        if instructions_list[instruction_index] == 0:
            program_terminated = True
            break

        instructions_run.append(instruction_index)
        if instructions_list[instruction_index][1] == 'acc':
            accumulator += instructions_list[instruction_index][2]
            instruction_index += 1
        elif instructions_list[instruction_index][1] == 'jmp':
            instruction_index += instructions_list[instruction_index][2]
        elif instructions_list[instruction_index][1] == 'nop':
            instruction_index += 1

    return [program_terminated, accumulator]

for i in range(len(my_input)):
    if my_input[i][1] == 'jmp':
        my_input[i][1] = 'nop'
        if program_runner(my_input)[0] == True:
            print(program_runner(my_input)[1])
            break
        else:
            my_input[i][1] = 'jmp'

    elif my_input[i][1] == 'nop':
        my_input[i][1] = 'jmp'
        if program_runner(my_input)[0] == True:
            print(program_runner(my_input)[1])
            break
        else:
            my_input[i][1] = 'nop'
