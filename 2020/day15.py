# data = [0,3,6]
data = [14,1,17,0,3,20]

numbers = {}
current_turn = 0

# Add starting numbers to the dict.
while current_turn < len(data):
    numbers[data[current_turn]] = [current_turn]
    current_turn += 1

last_number = data[len(data)-1]

# Calculate subsequent numbers after starting numbers.
while current_turn < 30000000: 

    # If last number was spoken for the first time.
    if len(numbers[last_number]) == 1:
        last_number = 0

    # If last number had been spoken before.
    else:
        # If spoken twice in a row.
        if numbers[last_number][1] - numbers[last_number][0] == 1:
            last_number = numbers[last_number][1] - numbers[last_number][0]

        # If not spoken twice in a row.
        else: 
            last_number = numbers[last_number][1] - numbers[last_number][0]

    # Add number to numbers if necessary and append current turn.
    if last_number in numbers:
        numbers[last_number].append(current_turn)
    else:
        numbers[last_number] = [current_turn]

    # Keep only last two turns any numbers was said.
    if len(numbers[last_number]) == 3:
        del(numbers[last_number][0])
        
    current_turn += 1

print(last_number)
