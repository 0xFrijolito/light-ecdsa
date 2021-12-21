from ecdsa import PrivateKey, sign, verify

private_key = PrivateKey
public_key = private_key.generate_public_key()

message = b"hello world"

signature = sign(private_key, message)
valid_sign = verify(public_key, signature, message)

print(valid_sign)
