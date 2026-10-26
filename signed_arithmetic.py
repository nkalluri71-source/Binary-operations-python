def to_8bit_binary(num):
    return format(num & 0xFF, '08b')


def signed_value(binary_value):
    if binary_value & 0x80:
        return binary_value - 256
    return binary_value


def add_8bit(a, b):
    # Convert operands to 8-bit 2's complement
    a_bin = a & 0xFF
    b_bin = b & 0xFF

    # Perform 8-bit addition
    result = (a_bin + b_bin) & 0xFF

    # Signed overflow occurs when the operands have
    # the same sign but the result has a different sign
    overflow = ((~(a_bin ^ b_bin) & (a_bin ^ result)) & 0x80) != 0

    print("First operand :", to_8bit_binary(a), "=", a)
    print("Second operand:", to_8bit_binary(b), "=", b)
    print("Binary result :", to_8bit_binary(result))
    print("Decimal result:", signed_value(result))
    print("Overflow      :", "Yes" if overflow else "No")
    print("-" * 40)


print("8-BIT 2'S COMPLEMENT SIGNED ADDITION")
print("=" * 40)

print("\na) (+25) + (+18)")
add_8bit(25, 18)

print("\nb) (-25) + (-18)")
add_8bit(-25, -18)