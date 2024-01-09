import functions


data="hello world"
key="1e321daeb96017ab59526ec8e66a6235"
#data = ''.join(format(ord(char), '08b') for char in data)
#key=''.join(format(ord(char), '08b') for char in key)

if __name__ == '__main__':
    enc=functions.enc(key.encode('utf-8'),data.encode('utf-8'))
    print("your encrepted message is ",enc)
    dec=functions.dec(key.encode('utf-8'),enc)
    print('your decrepted message is',dec)
