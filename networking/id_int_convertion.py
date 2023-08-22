ID_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def int_to_id(n):
    base = len(ID_CHARS)
    
    if n == 0:
        return ID_CHARS[0]
    
    result = ""
    while n > 0:
        digit = n % base
        result = ID_CHARS[digit] + result
        n //= base
    
    return result

def id_to_int(custom_b64_str):
    base = len(ID_CHARS)
    result = 0
    power = 0
    
    for char in reversed(custom_b64_str):
        digit = ID_CHARS.index(char)
        result += digit * (base ** power)
        power += 1
    
    return result



if __name__ == '__main__':
    _input = ""
    while _input != "q":
        _input = input("int: ")
        try:
            num = int(_input)
        except:
            continue
        base64_n = int_to_id(num)
        print(f"custom_base64: {base64_n}")
        print(f"back: {id_to_int(base64_n)}")
