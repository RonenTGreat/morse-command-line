import morse_talk as mtalk


print("Hello Welcome!")
print("Do you want to Encode or Decode")
choose = input()

if(choose.lower() == "encode"):
    message = input("Enter the message you want to encode: ")
    print(mtalk.encode(message))
elif(choose.lower() == "decode"):
    message = input("Enter the message you want to encode: ")
    print(mtalk.decode(message))
else:
    print("You have entered an invalid input.")
