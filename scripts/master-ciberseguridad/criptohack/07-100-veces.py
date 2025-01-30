
from pwn import remote
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes

# Connect to the server
r = remote('socket.cryptohack.org', 13377)

# Function to receive JSON data
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

# Function to send JSON data
def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

# Function to decode the given encoded text
def decode_message(encoding_type, encoded_value):
    if encoding_type == "base64":
        return base64.b64decode(encoded_value).decode()
    elif encoding_type == "hex":
        return bytes.fromhex(encoded_value).decode()
    elif encoding_type == "rot13":
        return codecs.decode(encoded_value, 'rot_13')
    elif encoding_type == "bigint":
        return long_to_bytes(int(encoded_value, 16)).decode()
    elif encoding_type == "utf-8":
        return "".join(chr(i) for i in encoded_value)
    else:
        raise ValueError(f"Unknown encoding type: {encoding_type}")

# Start the challenge loop
intento = 0
while True:
    intento +=1
    print('intento: ', intento)
    received = json_recv()

    # Check if we got the flag
    if "flag" in received:
        print(f"Flag: {received['flag']}")
        break

    encoding_type = received["type"]
    encoded_value = received["encoded"]

    # Decode the message
    decoded_message = decode_message(encoding_type, encoded_value)
    print(decoded_message)
    # Send the decoded message back
    to_send = {"decoded": decoded_message}
    json_send(to_send)
