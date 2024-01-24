def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    number_word = {}

    for line in lines:
        parts = line.split()
        number = int(parts[0])
        word = ' '.join(parts[1:])
        number_word[number] = word

    max_number = max(number_word.keys())

    decoded_message = []
    current_number = 1
    i = 1
    while current_number <= max_number:
        decoded_message.append(number_word[current_number])
        i += 1
        current_number += i

    return ' '.join(decoded_message)

decode('/Users/Admin/Downloads/coding_qual_input.txt')

# Example usage: decode('message_file.txt')
# Replace 'message_file.txt' with your file path
