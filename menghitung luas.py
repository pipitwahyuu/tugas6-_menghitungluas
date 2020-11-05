import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Membuat fungsi utk menentukan layout window
# Memecah fungsi menjadi beberapa bagian, TopLayout merupakan fungsi untuk tampilan bagian atas

def topLayout(window):
    # Membuat Judul Dibagian Atas
    label = QLabel("Aplikasi Menghitung Luas Bangun Ruang")
    # Mensetting Align nya agar berada Ditengah
    label.setAlignment(Qt.AlignCenter)
    # Membuat Vertical Layout Dan Menambahkan Widget Nya
    layout1 = QVBoxLayout()
    layout1.addWidget(label)
    # Mereturn/mengembalikan nilai layout nya karena kita butuh layoutnya untuk ditambahkan ke gridLayout nya
    return layout1

def hitungJajarGenjang(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Menghitung Luas Jajar Genjang", window)
    # Membuat Widget Label
    labelRusuk = QLabel("Panjang Alas: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global rusuk
    labelTall = QLabel("Panjang Tinggi: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global tall
    # Membuat Widget Inputan
    rusuk = QLineEdit()
    tall = QLineEdit()
    # Membuat Button/ tombol
    btn = QPushButton("Hitung")
    # Mengirim Data Saat kita Mengklik button nya
    btn.clicked.connect(jajargenjang)
    # Membuat Form Layout Dan Menambahkan widget
    layout = QVBoxLayout()
    layout1 = QGridLayout()
    layout1.addWidget(labelRusuk)
    layout1.addWidget(rusuk)
    layout2 = QGridLayout()
    layout2.addWidget(labelTall)
    layout2.addWidget(tall)
    layout.addLayout(layout1)
    layout.addLayout(layout2)
    layout.addWidget(btn)
    groupbox.setLayout(layout)
    return groupbox

def jajargenjang():
    try:
        vRusuk = rusuk.text()
        vTall = tall.text()
        hKubus = int(vRusuk) * int(vTall)
        hasilKubus.setText(str(hKubus))
        rusuk.setText("")
        tall.setText("")
    except ValueError:
        pass
    
# Rumus Perhitungan
def hitungBalok(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Menghitung Luas Balok", window)
    # Membuat Widget Label
    labelPanjang = QLabel("Panjang: ")
    labelLebar = QLabel("Lebar: ")
    labelTinggi = QLabel("Tinggi: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global panjang, lebar,tinggi
    # Membuat Widget Inputan
    panjang = QLineEdit()
    lebar = QLineEdit()
    tinggi = QLineEdit()
    # Membuat Button/ tombol
    btn = QPushButton("Hitung")
    # Mengirim Data Saat kita Mengklik button nya
    btn.clicked.connect(balok)
    # Membuat Form Layout Dan Menambahkan widget
    layout1 = QGridLayout()
    layout1.addWidget(labelPanjang,0,0)
    layout1.addWidget(panjang,0,1)
    layout1.addWidget(labelLebar,1,0)
    layout1.addWidget(lebar,1,1)
    layout1.addWidget(labelTinggi,2,0)
    layout1.addWidget(tinggi,2,1)
    layout1.addWidget(btn,3,0,1,0)
    groupbox.setLayout(layout1)
    return groupbox

def balok():
    try:
        vPanjang = panjang.text()
        vLebar = lebar.text()
        vTinggi = tinggi.text()
        hBalok = (2 * int(vPanjang) * int(vLebar)) + (2 *
        int(vPanjang) * int(vTinggi)) + (2 * int(vLebar) * int(vTinggi))
        hasilBalok.setText(str(hBalok))
        panjang.setText("")
        lebar.setText("")
        tinggi.setText("")
    except ValueError:
        pass
    
def Tampil(window):
    # Membuat Grupbox
    groupbox = QGroupBox("Hasil Operasi", window)
    # Membuat Widget Label
    labelKubus = QLabel("Luas Jajar Genjang: ")
    labeBalok = QLabel("Luas Balok: ")
    # Mendefinisikan agar variabel suhu bisa diakses fungsi lain/membuat variabel suhu tidak menjadi lokal lagi
    global hasilKubus,hasilBalok
    # Membuat Widget Inputan
    hasilKubus = QLineEdit()
    hasilKubus.setReadOnly(True)
    hasilBalok = QLineEdit()
    hasilBalok.setReadOnly(True)
    # Membuat Form Layout Dan Menambahkan widget
    layout1 = QFormLayout()
    layout1.addRow(labelKubus,hasilKubus)
    layout1.addRow(labeBalok,hasilBalok)
    groupbox.setLayout(layout1)
    return groupbox

def window_go():
    #inisialisasi pyqt
    app = QApplication(sys.argv)
    window = QWidget()
    # Menginisiasi GridLayout
    GLayout = QGridLayout()
    # Menambahkan Widget GroupBox Ke gridLayout
    GLayout.addLayout(topLayout(window),0,0,1 ,2)
    GLayout.addWidget(hitungJajarGenjang(window), 2, 0,1,0)
    GLayout.addWidget(hitungBalok(window), 3, 0,1,0)
    GLayout.addWidget(Tampil(window), 4, 0,1,0)
    # Menset agar jarak tidak terlalu renggang
    GLayout.setRowStretch(2,1)
    GLayout.setRowStretch(3,1)
    # Menset Layout Utama Ke GridLayout
    window.setLayout(GLayout)
    # Mensetting Ukuran Aplikasinya
    window.setGeometry(100,100,500,500)
    # Menset Judul Aplikasi
    window.setWindowTitle("Menghitung Bangun Datar")
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    window_go()
