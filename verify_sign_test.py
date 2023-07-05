# public libray
import base64
import hashlib

import ecdsa
from Crypto.Hash import SHA256
from bitarray.util import hex2ba
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from ecdsa.util import sigdecode_der
from hashlib import sha256
# project file :)
import der_decoder

# sample data
# pem formatted public key
publicKey = """-----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEAaiIUwqSeTdOtome9+b5ZvgrTnko
    SGdo5dcgm4+w
    0YNjHm3lJWxOqO0R1ZuL1NJCnSaweYYI9VF5g67H/9Cj7g==
    -----END PUBLIC KEY-----"""
pk = base64.b64decode("MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEl4y7uNyREELwW56XiEGdGsQuFpbqKGPQYb71T/H/67vIeuTz9mz+U/WkKPnt8loPqUE2hA2ea3e7eXSS7Ub2ng==")
hex_string_signature = "3044022058EFFBAB2BAA81BD35CA1D5C82E52770D9F0C66D85E2D776E4D2C582E8BBB6320220366A27E9FB17E81A5B4DDBF2BDB64A30155BB861D84E517FADC5D6C1EA54245A"


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
    print(verifier.verify(hashed_message, signature))

    # # new trial
    # signature = bytes.fromhex(hex_string_signature)
    # vk = ecdsa.VerifyingKey.from_string(pk, curve=ecdsa.NIST256p, hashfunc=sha256)
    # assert vk.verify(signature, hashed_message, hashlib.sha256, sigdecode=sigdecode_der)


