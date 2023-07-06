# public libray
from ecdsa import VerifyingKey
from hashlib import sha256
# project file :)
import der_decoder

# sample data
# pem formatted public key
publicKey = """-----BEGIN PUBLIC KEY-----
    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE+nvGkuBUIxiFR8i84EgOZeU5r4Ho
    yzajuY/9WDNK
    9Qlfg3klUKqdRdIafQC0Uiz7XpViN217VUJjKJWN3vwn0g==
    -----END PUBLIC KEY-----"""
hex_string_signature = "304402207790BB0D4E57535FD1943EABCF9AF3C2B6D78E4362972F7933913013F90C9C2A02200CB52AC933E0E6D43" \
                       "6219A5DF9F80967CB7D7D0DD10391644CD7DDA1F9C5DBFC"
message = "1234567890"

if __name__ == "__main__":
    vk = VerifyingKey.from_pem(publicKey)
    print(vk)
    decoded_signature = der_decoder.der_decoder(hex_string_signature)
    result = vk.verify(bytes.fromhex(decoded_signature), bytes(message, "ascii"), sha256)
