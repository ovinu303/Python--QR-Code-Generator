import qrcode
import os

data = input('Enter the data you want to encode in the QR code: ')
output_path = os.path.join(os.path.expanduser("~"), "Downloads") #to get path to user's Downloads folder

qr = qrcode.QRCode(version=1, box_size=25, border=10)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')
img.save(os.path.join(output_path, 'PythonQR.png'))

print('Check your Downloads folder for your QR Code.')

