import qrcode
import sqlite3

def generate_qr(student_id, name):
    qr = qrcode.make(student_id)
    qr.save(f"qr_{student_id}.png")

    print(f"✅ QR Code generated for {name} ({student_id})")

# Example: generate one manually
if __name__ == "__main__":
    student_id = "HIT2025CS001"
    name = "Christopher Bango"
    generate_qr(student_id, name)
