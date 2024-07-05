import qrcode as qr
code=qr.QRCode(
  border=4,
  box_size=10,
  version=5,
)
data=input("please enter the data")
code.add_data(data)
code.make(fit=True)
img=code.make_image(fill="black", back_color="white")
x=input("please enter the name of the code")
img.save(x+".png")
