from bitarray.util import hex2ba

hex_signature = '30450220203D56DC1D7C1EF988570F7B9D74DC96EA677D7FFDB94C09BED9C2CF5D967134022100AB8A49160B526F83D9FF4BDC58C1B4DA836E2A6741289562284D334292A970BA'


def der_decoder(signature):
    signature = signature[12:]  # remove heading
    hex_r = signature[:64]  # get number r
    ba_r = hex2ba(hex_r, endian='little')
    if ba_r[0] == 1:
        signature = signature[66:]
    else:
        signature = signature[64:]
    hex_s = signature[:64]
    signature = hex_r + hex_s
    return signature


if __name__ == "__main__":
    signature = der_decoder(hex_signature)
    print(signature)
    print(len(signature))

