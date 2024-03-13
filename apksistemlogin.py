# Data Dictionary Username & Password (Contoh)
data_mahasiswa = {
    '07352311175': 'password1',
    '07352311176': 'password2',
    '07352311177': 'password3',
    '07352311178': 'password4',
    '07352311179': 'password5',
    '07352311180': 'password6',
    '07352311181': 'password7',
    '07352311182': 'password8',
    '07352311183': 'password9',
    '07352311184': 'password10',
}

# Aplikasi Sistem Login
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Mengecek keberadaan username dalam data dictionary
    if username in data_mahasiswa:
        # Mengecek kecocokan password
        if data_mahasiswa[username] == password:
            print("Selamat datang,", username + "!")
        else:
            print("Data yang dimasukkan salah, Silahkan coba lagi.")
    else:
        print("Data yang dimasukkan salah, Silahkan coba lagi.")

# Memanggil fungsi login
login()