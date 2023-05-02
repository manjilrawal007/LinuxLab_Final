import sys

def format_output(output):
    result_str = ''
    line_str = ''
    count_int = 0
    for letter in output:
        line_str += letter
        count_int += 1
        if count_int == 5:
            result_str += line_str + ' '
            line_str = ''
            count_int = 0
    if line_str:
        result_str += line_str + '\n'
    return result_str

def encode(text, shift):
    letters_lst = [char.upper() for char in text if char.isalpha()]
    encoded_lst = []
    for char in letters_lst:
        ascii_val = ord(char)
        new_val = ascii_val + shift
        if new_val > ord('Z'):
            final_val = (new_val - ord('Z')) % 26
            if final_val == 0:
                final_val = 26
            new_val = final_val + ord('A') - 1
        encoded_lst.append(chr(new_val))
    return format_output(''.join(encoded_lst))

args = sys.argv
if len(args) < 2:
    print("Please provide a shift value as a command line argument.")
    sys.exit(1)

shift_value = int(args[1])
for line_str in sys.stdin:
    encoded_text = encode(line_str.strip(), shift_value)
    sys.stdout.write(encoded_text)
