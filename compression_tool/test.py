
import sys
import json

json.loads
binary_string = '0101010100101'
print(binary_string)
print("size of binary string:" , sys.getsizeof(binary_string))
# Convert the binary string to an integer
integer_value = int(binary_string, 2)
print(integer_value)

# Calculate the number of bytes needed
num_bytes = (len(binary_string) + 7) // 8  # Round up to the nearest byte

# Convert the integer to bytes
byte_data = integer_value.to_bytes(num_bytes, byteorder='big')
print("compressed to: ", end = " ")
print(byte_data)
print("size of byte_data:" , sys.getsizeof(byte_data))


# Assume you have byte_data as the bytes you want to decode

# Convert the bytes to an integer
integer_value = int.from_bytes(byte_data, byteorder='big')

# Convert the integer to a binary string
binary_string = bin(integer_value)[2:]  # [2:] is used to remove the '0b' prefix
print("decompresed to: " , end = " ")
print(binary_string)
print("size of binary string:" , sys.getsizeof(binary_string))