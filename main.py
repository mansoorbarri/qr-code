import qrcode
import requests

print("""
        __  __ ____  
        |  \/  |  _ \ 
        | \  / | |_) |
        | |\/| |  _ < 
        | |  | | |_) |
        |_|  |_|____/ 

======= Mansoor Barri =======
    https://mansoorbarri.com
""")

def generate_qr_code(url, fill_color, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=None)
    img.save(output_file)

def main():
    fill_color = input("Enter the color reference number (e.g., #ffffff) for the fill color: ")

    while True:
        url = input("Enter the URL: ").strip()
        try:
            response = requests.head(url)
            if response.status_code == 200:
                break
            else:
                print("Error: URL is not accessible. Please enter a valid URL.")
        except Exception as e:
            print(f"Error: {e}")

    output_file = input("Enter the destination file name (with .png extension): ")

    generate_qr_code(url, fill_color, output_file)

if __name__ == "__main__":
    main()
