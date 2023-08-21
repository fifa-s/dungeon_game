import base64

def int_to_base64(number):
    number_bytes = number.to_bytes((number.bit_length() + 7) // 8, 'big')
    base64_encoded = base64.b64encode(number_bytes)
    base64_string = base64_encoded.decode('utf-8')
    return base64_string

def base64_to_int(base64_string):
    base64_bytes = base64_string.encode('utf-8')
    number_bytes = base64.b64decode(base64_bytes)
    number = int.from_bytes(number_bytes, 'big')
    return number

