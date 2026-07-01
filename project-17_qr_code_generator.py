import qrcode
from PIL import Image
user_input = input("Enter url or number to generate QR code: ")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(user_input)
qr.make(fit=True)
image = qr.make_image(fill_color="black", back_color="white")
image.save("qr_code.png")
print("QR code generated successfully")