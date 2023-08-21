"""convertion between string and int representation of IPv4"""

def ipv4_to_int(ipv4_str: str) -> int:
    parts = ipv4_str.split('.')
    
    # Ensure there are four parts and each part is within valid range (0-255)
    if len(parts) != 4 or any(not 0 <= int(part) <= 255 for part in parts):
        raise ValueError("Invalid IPv4 address format")
    
    # Convert each part to an integer and calculate the 32-bit integer representation
    ipv4_int = (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])
    return ipv4_int

def int_to_ipv4(ipv4_int: int) -> str:
    # Ensure the input is a valid 32-bit unsigned integer
    if not 0 <= ipv4_int <= 0xffff_ffff:
        raise ValueError("Invalid 32-bit integer representation of IPv4 address")
    
    # Calculate each part of the IPv4 address from the integer
    part1 = (ipv4_int >> 24) & 255
    part2 = (ipv4_int >> 16) & 255
    part3 = (ipv4_int >> 8) & 255
    part4 = ipv4_int & 255
    
    ipv4_str = f"{part1}.{part2}.{part3}.{part4}"
    return ipv4_str


