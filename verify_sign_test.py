# public libray
from Crypto.Hash import SHA256
from bitarray.util import hex2ba
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
import hashlib
# project file :)
import der_decoder

# sample data
publicKey = """-----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEqzkre/No20HVUUoBinG2SUmwdXMA
    4kiXUbZtpKSa
    B3UYCbZG2fVne/T4Sb81a1LwQ9HXBS/7YCJG8JRdR9T2Ew==
    
    -----END PUBLIC KEY-----"""
hex_string_signature = "30460221008061585A59CBA8A722DCF03C004D38C26BDD369B6B09D68E94A25A7B31315F790221008286DFD7202192D167B406DC39A2879DFF204F32BEB1388843C184C077B5F8F0"


if __name__ == "__main__":

    # import public key & generate verifier
    public_key = ECC.import_key(publicKey)
    verifier = DSS.new(public_key, 'fips-186-3')

    # 서명된 메시지
    message = bytes("random text", 'ascii')
    hashed_message = SHA256.new(message)

    decoded_signature = der_decoder.der_decoder(hex_string_signature)
    ba_signature = hex2ba(decoded_signature)
    signature = bytes.fromhex(decoded_signature)

    print("result of verfier :", verifier.verify(hashed_message, signature))
