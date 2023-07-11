def der_decoder(signature):
    len_r = int(signature[6:8], 16)
    if len_r == 32:
        hex_r = signature[8:72]
    else:
        hex_r = signature[10:74]
    hex_s = signature[-64:]
    return hex_r+hex_s



