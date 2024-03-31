import qrcode as qr

qr_code = qr.make(input("Enter your text: "))
qr_code.save("my_qr_code.png")