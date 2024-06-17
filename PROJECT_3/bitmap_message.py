import sys

bitmap = open("bit_map_world.txt", "r").readlines()

print(f'''
    Bitmap Message, by Al Sweigart al@inventwithpython.com
    Enter the message to display with the bitmap.

''')

message = input('>')
if message == '':
    sys.exit()

for line in bitmap:
    for i, bit in enumerate(line):
        if bit == ' ':
            print(" ", end='')
        else:
            print(message[i % len(message)], end='')
    print()
