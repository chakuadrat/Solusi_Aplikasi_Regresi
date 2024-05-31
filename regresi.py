import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit

def get_user_input():
    while True:
        print("Masukkan data Jumlah Latihan Soal (dipisahkan dengan koma):")
        NL = np.array([float(x) for x in input().split(',')])
        print("Masukkan data Nilai Ujian Siswa (dipisahkan dengan koma):")
        NT = np.array([float(x) for x in input().split(',')])
        
        if len(NL) != len(NT):
            print("\nJUMLAH ELEMEN JUMLAH LATIHAN SOAL DAN NILAI UJIAN SISWA HARUS SAMA!\n \n")
        else:
            break
    return NL, NT

def plot_data(NL, NT):
    plt.scatter(NL, NT, color='blue', label='Data Points')
    plt.xlabel('Jumlah Latihan Soal (NL)')
    plt.ylabel('Nilai Ujian Siswa (NT)')
    plt.title('Grafik Titik Data NL vs NT')
    plt.legend()
    plt.grid(True)
    plt.show()

def linear_regression(NL, NT):
    NL_reshaped = NL.reshape(-1, 1)
    linear_model = LinearRegression()
    linear_model.fit(NL_reshaped, NT)
    NT_pred_linear = linear_model.predict(NL_reshaped)
    RMS_linear = np.sqrt(np.mean((NT - NT_pred_linear) ** 2))
    
    plt.scatter(NL, NT, color='blue', label='Data Points')
    plt.plot(NL, NT_pred_linear, color='red', label='Linear Regression')
    plt.xlabel('Jumlah Latihan Soal (NL)')
    plt.ylabel('Nilai Ujian Siswa (NT)')
    plt.title('Regresi Linear NL vs NT')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return RMS_linear

def power_regression(NL, NT):
    def power_model(x, a, b):
        return a * np.power(x, b)
    
    params, _ = curve_fit(power_model, NL, NT)
    a, b = params
    NT_pred_power = power_model(NL, a, b)
    RMS_power = np.sqrt(np.mean((NT - NT_pred_power) ** 2))
    
    plt.scatter(NL, NT, color='blue', label='Data Points')
    NL_sorted = np.sort(NL)
    plt.plot(NL_sorted, power_model(NL_sorted, a, b), color='green', label='Power Regression')
    plt.xlabel('Jumlah Latihan Soal (NL)')
    plt.ylabel('Nilai Ujian Siswa (NT)')
    plt.title('Regresi Pangkat Sederhana NL vs NT')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return RMS_power

def growth_rate_regression(NL, NT):
    def growth_rate_model(x, a, b, c):
        return a * x / (b + x) + c
    
    params, _ = curve_fit(growth_rate_model, NL, NT, maxfev=10000)
    a, b, c = params
    NT_pred_growth = growth_rate_model(NL, a, b, c)
    RMS_growth = np.sqrt(np.mean((NT - NT_pred_growth) ** 2))
    
    plt.scatter(NL, NT, color='blue', label='Data Points')
    NL_sorted = np.sort(NL)
    plt.plot(NL_sorted, growth_rate_model(NL_sorted, a, b, c), color='purple', label='Growth Rate Regression')
    plt.xlabel('Jumlah Latihan Soal (NL)')
    plt.ylabel('Nilai Ujian Siswa (NT)')
    plt.title('Regresi Laju Pertumbuhan Jenuh NL vs NT')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return RMS_growth

def main():
    """Fungsi utama untuk menjalankan program."""
    print("\nNisrina Azka Salsabila")
    print("21120122130057")
    print("Metode Numerik - Kelas C")
    print("Teknik Komputer")
    
    while True:
        print("\nAplikasi Regresi")
        print("\nSelamat datang! Silahkan pilih penyelesaian yang anda inginkan pada menu dibawah ini:")
        print("1. Model Linear")
        print("2. Model Pangkat Sederhana")
        print("3. Model Laju Pertumbuhan Jenuh")
        print("4. Keluar")

        pilihan = int(input("Masukkan pilihan Anda (1-4): "))

        if pilihan == 1:
            NL, NT = get_user_input()
            plot_data(NL, NT)
            RMS_linear = linear_regression(NL, NT)
            print("RMS Error for Linear Regression:", RMS_linear)
        elif pilihan == 2:
            NL, NT = get_user_input()
            plot_data(NL, NT)
            RMS_power = power_regression(NL, NT)
            print("RMS Error for Power Regression:", RMS_power)
        elif pilihan == 3:
            NL, NT = get_user_input()
            plot_data(NL, NT)
            RMS_growth = growth_rate_regression(NL, NT)
            print("RMS Error for Growth Rate Regression:", RMS_growth)
        elif pilihan == 4:
            print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
