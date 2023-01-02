## Light ECDSA

Minimalist and lightweight implementation of ecdsa in python

### Installation
Run this command in the terminal:
```bash
pip install light-ecdsa
```

### Code Examples

Basic private and public key generation and sign a message

```python
from ecdsa import sign, verify, PrivateKey

def main ():
    private_key = PrivateKey()
    public_key  = private_key.generate_public_key() 
    message = b"hello world"
    
    signature = sign(private_key, message)
    is_valid = verify(public_key, message, signature)
    print(is_valid) # True   
    
if __name__ == "__main__":
    main()
```
