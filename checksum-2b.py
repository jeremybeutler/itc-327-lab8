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