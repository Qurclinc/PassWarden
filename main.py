from Crypto.Cipher import AES
import base64

key = "XUELlx8+ZgVXU5VI"
cipher = AES.new(key.encode("utf-8"), AES.MODE_EAX)

nonce = cipher.nonce

data = "соси хуй чурка"

ciphertext, tag = cipher.encrypt_and_digest(data.encode("utf-8"))
text = base64.b64encode(ciphertext)
print(text)