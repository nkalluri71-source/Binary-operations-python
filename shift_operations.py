def left_shift(binary, positions):
    print("Original binary number:", binary)
    result = int(binary, 2)

    for i in range(positions):
        result = (result << 1) & 0xFF
        print("After left shift", i + 1, ":", format(result, '08b'))

    print("Final 8-bit result:", format(result, '08b'))
    print()


def right_shift(binary, positions):
    print("Original binary number:", binary)
    result = int(binary, 2)

    for i in range(positions):
        result = result >> 1
        print("After right shift", i + 1, ":", format(result, '08b'))

    print("Final 8-bit result:", format(result, '08b'))
    print()


print("LOGICAL SHIFT OPERATIONS ON 8-BIT NUMBERS")
print("=" * 45)

print("\na) Logical left shift of 10110110 by 2 positions")
left_shift("10110110", 2)

print("b) Logical right shift of 11010100 by 2 positions")
right_shift("11010100", 2)