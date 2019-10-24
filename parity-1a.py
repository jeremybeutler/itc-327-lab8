counter = 0
sent = "00001100"
parity_bit = ""

for bit in data:
    if bit == "1":
        counter += 1
even_calc = counter % 2
has_even_num_checked_bits = bool(even_calc == 1)
if (has_even_num_checked_bits):
    parity_bit = "1"
else:
    parity_bit = "0"

print("Original Data: " + data)
print("Parity Bit: " + parity_bit)
print("New Data:      " + data + parity_bit)


