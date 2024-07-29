import qrcode

def generate_qr_code(website):
    data = f"url:{website}\n"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    return img


if __name__ == "__main__":
    website = input("Введите адрес сайта: ")

    qr_code = generate_qr_code(website)
    qr_code.save("qr_code.png")

    print("QR-код сохранен в файл 'qr_code.png'")
