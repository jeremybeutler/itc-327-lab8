# Initialize counter and data stream
# Loop for each bit in data stream
# Define next states for each bit
# Next Bit 1 = next bit of Data In
# Next Bit 2 = Present Bit 1
# Next Bit 3 = Present Bit 2 XOR
# present Bit 8
# Next Bit 4 = Present Bit 3 XOR
# present Bit 8
# Next Bit 5 = Present Bit 4 XOR
# present Bit 8
# Next Bit 6 = Present Bit 5
# Next Bit 7 = Present Bit 6
# Next Bit 8 = Present Bit 7
# Move next states into present states
# Present Bit 1 = Next Bit 1
# Present Bit 2 = Next Bit 2
# Present Bit 3 = Next Bit 3
# Present Bit 4 = Next Bit 4
# Present Bit 5 = Next Bit 5
# Present Bit 6 = Next Bit 6
# Present Bit 7 = Next Bit 7
# Present Bit 8 = Next Bit 8
# Output CRC encoder byte to screen
# End loop
# Output final CRC checksum byte

counter = 0
data_stream = "00001100"
pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8 = 0

for bit in data_stream:
    # Define next states for each bit
    nb1 = bit
    nb2 = pb1
    nb3 = pb2 ^ pb8
    nb4 = pb3 ^ pb8
    nb5 = pb4 ^ pb8
    nb6 = pb5
    nb7 = pb6
    nb8 = pb7
    # Move next states into present states
    pb1 = nb1
    pb2 = nb2
    pb3 = nb3
    pb4 = nb4
    pb5 = nb5
    pb6 = nb6
    pb7 = nb7
    pb8 = nb8


    counter += 1
