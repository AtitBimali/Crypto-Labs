S_BOX = [
    [0x1, 0x2, 0x3, 0x4],
    [0x5, 0x6, 0x7, 0x8],
    [0x9, 0xA, 0xB, 0xC],
    [0xD, 0xE, 0xF, 0x10]
]



def substitute(s_box, value):
    return s_box[value >> 2][value & 0x3]



def generate_key(input_key):
    key = [0] * 16  
    for i in range(16):
        key[i] = input_key[i % len(input_key)] ^ i
    return key



def main():
    input_matrix = [
        [0, 1, 5, 6],
        [0, 1, 5, 6],
        [0, 1, 5, 6],
        [0, 1, 5, 6]
    ]

    key = [0x12, 0x34, 0x56, 0x78]  
    expanded_key = generate_key(key)

    output_matrix = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            input_value = input_matrix[i][j]
            s_box_output = substitute(S_BOX, input_value)
            output_matrix[i][j] = s_box_output ^ expanded_key[i*4 + j]

    print("Input Matrix:")
    for row in input_matrix:
        print(row)

    print("\nS-box Output Matrix:")
    for row in output_matrix:
        print(row)

    print("\nExpanded Key:")
    print(expanded_key)


if __name__ == "__main__":
    main()
