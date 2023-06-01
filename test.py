import qrcode

data = "Leandro dos Santos Araújo\n01/06/2023\n05/06/2023"

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
import os
os.startfile('qrcode.png')
