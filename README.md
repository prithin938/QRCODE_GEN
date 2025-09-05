# QR Code Generator

A simple Python script that collects user details (Name, Age, Gender, Phone, Email, ID number, Profession) and generates a QR code image.

---

## Requirements
- Python 3.8+
- pip
- Install dependency:
```bash
pip install "qrcode[pil]"
Usage
Sample Input / Output

Input (Terminal prompts):
Enter your name: Alice
Enter your age: 25
Enter your gender: Female
Enter your phonenumber: 9876543210
Enter your Email: alice@example.com
Enter your ID_number: 12345
Enter your professionality: Engineer


Generated QR Content (scanned result):
Name: Alice
Age: 25
Gender: Female
Phonenumber: 9876543210
Email: alice@example.com
ID_number: 12345
professionality: Engineer


Clone repo:

git clone <your-repo-url>
cd <your-repo-folder>


(Optional) Create virtual environment:

python -m venv .venv
# Windows:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate


Run script:

python "Qr code .py"
# or, if renamed:
python qr_code.py


Enter details when prompted.
The QR code will preview and save to a file.

Save to PNG

In the script, replace:

image.save("Desktop")


with:

image.save("qr.png")

Example QR Content
Name: Alice
Age: 25
Gender: Female
Phonenumber: 9876543210
Email: alice@example.com
ID_number: 12345
professionality: Engineer

Troubleshooting

Module not found: pip install "qrcode[pil]"

No preview: Save with .png and open manually.

Phone loses leading zeros: Treat phone as string in script.
