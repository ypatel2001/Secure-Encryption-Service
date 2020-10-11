
x=1
while x==1:
    print("Welcome to the CIA's Encryption and Decryption Software!")
    print("You are now connected to our secure server.")
    choice=input(        '''

What would you like to do:

1-Encrypt your own message
2-Decrypt a pre-loaded message left for you by your handler
3-Exit Secure Software 
''')
    if choice=="1":
        message=input("Please enter your message: ")
        shift=int(input("Your message will be encrypted using a Ceaser shift code.\nPlease enter the shift amount between (1-126) you want the Unicode to shift by: "))
        encryption=''
        for letter in message:
            x=ord(letter)+ shift
            encryption+= chr(x)
        print("Here is your encrypted message: "+encryption)

    if choice=="2":
        x1=(";<=*]om|o~*Myno*KLM")
        x2=("Mox~|kv*Zoov*]omyxnk|*]mryyv")
        x3=("^sxuvo*^sxuvo*Vs~~vo*]~k|")
        x4=("Tkwo}*Lyxn*::A")
        x5=("^rkxu*y*py|*nom|z~sxq*~rs}*}om|o~*wo}}kqo+")
        x11=('')
        x22=('')
        x33=('')
        x44=('')
        x55=('')

        print('''
Please select the number of the message that you wish to decrypt.
Here is a list of messages that can be decrypted for you:

1=(";<=*]om|o~*Myno*KLM")
2=("Mox~|kv*Zoov*]omyxnk|*]mryyv")
3=("^sxuvo*^sxuvo*Vs~~vo*]~k|")
4=("Tkwo}*Lyxn*::A")
5=("^rkxu*y*py|*nom|z~sxq*~rs}*}om|o~*wo}}kqo+")''')
        choice1= input("Please enter your selection: ")

        if choice1=="1":
                      for letter1 in x1:
                        xA=ord(letter1)- 10
                        x11+= chr(xA)
                        print("Here is your decrypted message: "+x11)
        if choice1=="2":
                      for letter2 in x2:
                        xB=ord(letter2)- 10
                        x22+= chr(xB)
                        print("Here is your decrypted message: "+x22)
        if choice1=="3":
                      for letter3 in x3:
                        xC=ord(letter3)- 10
                        x33+= chr(xC)
                        print("Here is your decrypted message: "+x33)
        if choice1=="4":
                      for letter4 in x4:
                        xD=ord(letter4)- 10
                        x44+= chr(xD)
                        print("Here is your decrypted message: "+x44)
        if choice1=="5":
                      for letter5 in x5:
                        xE=ord(letter5)- 10
                        x55+= chr(xE)
                        print("Here is your decrypted message: "+x55)

    if choice=="3":
        print("Thank You For Your Service Agent! \nGod Speed on your mission.")
        exit()
              
              







