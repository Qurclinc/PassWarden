from Services.Crypter import Crypter

crypter = Crypter()
key = "S0m3H4rdLin3"
# data = "Соси хуй чурка"
# res = crypter.encrypt(key, data)

encrypted_data = "KHAd0RvwidmZcxLF:03AI03B0dNyXaEL5JRKvPLAs5ADCB2SEIFmPBgJbXORPUvldurZoeRVCkGVPSlHs"

res = crypter.decrypt(key, encrypted_data)

print(res)