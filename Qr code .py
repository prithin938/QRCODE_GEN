import qrcode
Name=input("Enter your Name:")
Age=int(input("Enter your Age:"))
Gender=input("Enter your Gender:")
Phonenumber=int(input("Enter your Phonenumber:"))
Email=input("Enter your Email:")
ID_number=int(input("Enter your ID_number:"))
professionality=input("Enter your professionality: ")
data=f"Name:{Name}\n Age:{Age}\nGender:{Gender}\n Phonenumber:{Phonenumber}\n Email:{Email}\n ID_number:{ID_number}\n professionality:{professionality}"
image=qrcode.make (data)
image.show()
image.save("Desktop")
print(image)
