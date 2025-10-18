import qrcode  # type: ignore
import os

def generate_qr_code(url, filename='qr_code.png'):
    qr = qrcode.QRCode(  # type: ignore
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # type: ignore
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    img.save(filename)
    print(f"QR Code berhasil dibuat: {filename}")
    print(f"QR Code mengarah ke: {url}")
    
    return filename

if __name__ == '__main__':
    domain = os.environ.get('REPL_SLUG', 'samsat-kebumen')
    user = os.environ.get('REPL_OWNER', 'user')
    
    url = f"https://{domain}.{user}.repl.co"
    
    print("=== SAMSAT KEBUMEN QR CODE GENERATOR ===")
    print(f"URL Target: {url}")
    print("\nPilihan:")
    print("1. Gunakan URL otomatis dari environment")
    print("2. Masukkan URL custom")
    
    choice = input("\nPilih (1/2): ").strip()
    
    if choice == '2':
        custom_url = input("Masukkan URL custom: ").strip()
        if custom_url:
            url = custom_url
    
    filename = input("Nama file QR Code (tekan Enter untuk 'qr_code.png'): ").strip()
    if not filename:
        filename = 'qr_code.png'
    elif not filename.endswith('.png'):
        filename += '.png'
    
    generate_qr_code(url, filename)
    print(f"\n✅ Selesai! QR Code tersimpan di: {os.path.abspath(filename)}")
