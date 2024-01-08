### Make a Simple encoding and decoding ###
# By: Sina Ghorbani
# The whole process is like: 'text ---> encoded(text) ---> decoded(text) ---> 'text

# enc_formula = (ord(inp) + 2) * 4
# dec_formula = chr((ord(inp) // 4) - 2)


while True:
    print("Please choose your strategy:\n\t1) Encrypt\n\t2) Decrypt\n\t3) Exit")

    inp = input("Enter your Choice: ")

    if inp == "1":
        enc_text_str = ''
        raw_text = [x for x in input("Please enter your text: ")] # input: aexe --> output: ['a', 'e', 'x', 'e']
        encoded_text = [(ord(i) + 2) * 4 for i in raw_text]  # input:['a', 'e', 'x', 'e'] --> output:['ƌ', 'Ɯ', 'Ǩ', 'Ɯ']
        enc_text_str = enc_text_str.join([chr(i) for i in encoded_text]) # ƌƜǨƜ
        print(f'The encoded text is: {enc_text_str}')
        print("*" * 40)

        break
    elif inp == "2":
        dec_text_str = ''
        enc_text = [x for x in input("Please enter your encrypted text: ")] # input:ƌƜǨƜ --> output:['ƌ', 'Ɯ', 'Ǩ', 'Ɯ']
        decoded_text_ordered = [chr((ord(x) // 4) - 2) for x in enc_text] # input:['ƌ', 'Ɯ', 'Ǩ', 'Ɯ'] --> output:['a', 'e', 'x', 'e']
        enc_text_str = dec_text_str.join([str(i) for i in decoded_text_ordered]) # aexe
        print(f'The decoded text is: {enc_text_str}')
        print("*" * 40)

        break

    elif inp == '3':
        print("You are going to exit the program")

        break
    else:
        print("*" * 40)
        print('Wrong choice')
        print("*" * 40)

        continue
