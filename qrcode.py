import qrcode


#url = input("enter the url: ")
url = https://www.linkedin.com/in/nikhil-s-shetty-99432a324/

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=6,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("qr_code.png")


img.show()
