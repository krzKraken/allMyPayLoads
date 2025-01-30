#!/usr/bin/env python3



hex_data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# Convert hex string to bytes
ciphertext = bytes.fromhex(hex_data)

# We know the flag starts with "crypto{", use it to extract the key
known_plaintext = b"crypto{"

# Determine the repeating key length using XOR on known plaintext
key = bytes([ciphertext[i] ^ known_plaintext[i] for i in range(len(known_plaintext))])

# Print the extracted partial key
key_str = key.decode()
print(f"Extracted partial key: {key_str}")

# Since the key repeats, we extend it over the full ciphertext length
full_key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]

# Decrypt the full ciphertext using the full key
decrypted_message = bytes([ciphertext[i] ^ full_key[i] for i in range(len(ciphertext))])

# Output the properly decoded flag
print(decrypted_message.decode())
