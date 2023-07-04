from Crypto.Hash import SHA256
from bitarray import bitarray
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

import der_decoder

# sample data
publicKey = """-----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEURKMmJOOSEmdZLzzETir9ghU6yh1
    6D3TITYPLCv2gRIkrtp9ym68VQJ3EndgcoOvppbuWpCG/gbnZkYqr3Jvlg==
    -----END PUBLIC KEY-----"""
hex_string_signature = "304502200231B8DDBCA2CF4CB445A16CC073031FEA889B32B81E8D92D0A3E90C2C8EEE2D022100CA7CF34598E1D" \
                       "BDA6B3D5BC83DB0DD4BF9F317535603CBF093B7EC8012C9DE7E"


if __name__ == "__main__":

    # import public key & generate verifier
    public_key = ECC.import_key(publicKey)
    verifier = DSS.new(public_key, 'fips-186-3')

    # 서명된 메시지
    message = bytes("I give my permission to order #4355", 'utf-8')
    hashed_message = SHA256.new(message)

    decoded_signature = der_decoder.der_decoder(hex_string_signature)
    signature = bytes.fromhex(decoded_signature)
    print(decoded_signature)
    print(signature)
    test = bitarray(endian='big')
    test.frombytes(signature)
    print(test)
    verifier.verify(hashed_message, signature)
