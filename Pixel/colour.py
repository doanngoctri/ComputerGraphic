def hex_to_rgb_color(hex):
    hex = hex[1:]
    return [int(hex[i:i + 2], 16) for i in (0, 2, 4)]

#print(hex_to_rgb_color("#0fffff"))

def rgb_to_hex_color(rgb):
    return '#%02x%02x%02x' % rgb

def get_inverse_color(hex):
    tup = hex_to_rgb_color(hex)
    for i in range(0,len(tup)):
        tup[i] = 255 - tup[i]
    return rgb_to_hex_color(tuple(tup))