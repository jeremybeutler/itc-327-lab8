sent        = "00001100"
recieved    = "000011001"
parity_bit = ""

def generate_even_parity_bit(bit_string):
    counter = 0
    for bit in bit_string:
        if bit == "1":
            counter += 1
    even_calc = counter % 2
    has_even_num_checked_bits = bool(even_calc == 1)
    if (has_even_num_checked_bits):
        return "1"
    else:
        return "0"

def was_error_detected(sent, recieved):
    counter = 0
    parity_sent = generate_even_parity_bit(sent)
    parity_recieved = recieved[len(recieved) - 1]
    i = 0
    for bit in recieved:
        if i < len(recieved) - 1:
            if bit == "1":
                counter += 1
        i += 1
    even_calc = counter % 2
    has_even_num_checked_bits = bool(even_calc == 1)
    if (has_even_num_checked_bits):
        parity_recieved_calc = "1"
    else:
        parity_recieved_calc = "0"
    

    if (parity_recieved_calc == parity_recieved):
        return "False"
    else:
        return "True"
    
print("Sent data:     " + sent + generate_even_parity_bit(sent))
print("Received data: " + recieved)
print("Error detected: " + was_error_detected(sent, recieved))
    

parity_bit = generate_even_parity_bit(sent)  



