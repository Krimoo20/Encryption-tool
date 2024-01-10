import secrets

import functions


#data="hello world"
#key="1e321daeb96017ab59526ec8e66a6235"
#data = ''.join(format(ord(char), '08b') for char in data)
#key=''.join(format(ord(char), '08b') for char in key)





def main():
    key = secrets.token_bytes(16)
    args = functions.argument_parser()
    if args.enc is not None:
     cipher=functions.enc(key,args.enc[0].encode('utf-8'))
     print("your encrepted message is: ",cipher)
     print("the encreption key used is: ",key)
    if args.dec is not None:
     key=args.dec[1]
     key=key.encode('utf-8').decode('unicode_escape').encode('latin-1')[1:]
     data=args.dec[0]
     data=data.encode('utf-8').decode('unicode_escape').encode('latin-1')[1:]

     plain_text=functions.dec(key,data)
     print('your plain text is: ', plain_text)
if __name__ == "__main__":
    main()
