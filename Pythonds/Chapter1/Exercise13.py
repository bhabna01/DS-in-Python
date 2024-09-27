# Define the half adder
def half_adder(bit1, bit2):
    # XOR for sum
    sum_bit = bit1 ^ bit2
    # AND for carry
    carry_bit = bit1 & bit2
    return sum_bit, carry_bit

# Define the full adder
def full_adder(bit1, bit2, carry_in):
    # Use two half adders and combine their results
    sum1, carry1 = half_adder(bit1, bit2)
    sum2, carry2 = half_adder(sum1, carry_in)
    carry_out = carry1 | carry2
    return sum2, carry_out

# 8-bit full adder function
def add_8bit(bin1, bin2):
    # Convert inputs to lists of bits (least significant bit first)
    a_bits = [int(bit) for bit in bin1[::-1]]
    b_bits = [int(bit) for bit in bin2[::-1]]

    # Initialize variables
    carry_in = 0
    result_bits = []

    # Loop through each bit position (0 to 7 for 8 bits)
    for i in range(8):
        bit_a = a_bits[i] if i < len(a_bits) else 0
        bit_b = b_bits[i] if i < len(b_bits) else 0
        
        # Perform full addition for each bit
        sum_bit, carry_out = full_adder(bit_a, bit_b, carry_in)
        
        # Append the sum bit to the result
        result_bits.append(sum_bit)
        
        # Update carry for the next position
        carry_in = carry_out
    
    # Convert result to string and reverse to get MSB to LSB order
    result = ''.join(str(bit) for bit in result_bits[::-1])
    return result, carry_in

# Input two 8-bit binary numbers as strings
bin1 = input("Enter 8-bit binary number A: ")
bin2 = input("Enter 8-bit binary number B: ")

# Ensure inputs are 8-bit numbers
if len(bin1) != 8 or len(bin2) != 8:
    print("Please enter valid 8-bit binary numbers!")
else:
    # Add the numbers
    sum_result, carry_out = add_8bit(bin1, bin2)
    
    # Display the result
    print(f"Sum: {sum_result}")
    print(f"Carry Out: {carry_out}")
