# Light ECDSA

Minimalist and lightweight implementation of ecdsa in python

## usage

```python
from ecdsa import sign, verify, PrivateKey

def main ():
    private_key = PrivateKey()
    public_key  = private_key.generate_public_key() 
    message = b"hello world"
    
    signature = sign(private_key, message)
    valid = verify(public_key, signature, message):
    print(valid)
    
if __name__ == "__main__":
    main()
```
