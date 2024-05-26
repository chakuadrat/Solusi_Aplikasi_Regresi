import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit

def get_user_input():
    while True:
        print("Masukkan data Durasi Waktu Belajar (dipisahkan dengan koma):")
        TB = np.array([float(x) for x in input().split(',')])
        print("Masukkan data Nilai Ujian Siswa (dipisahkan dengan koma):")
        NT = np.array([float(x) for x in input().split(',')])
        
        if len(TB) != len(NT):
            print("\nJUMLAH ELEMEN DURASI WAKTU BELAJAR DAN NILAI UJIAN SISWA HARUS SAMA!\n \n")
        else:
            break
    return TB, NT

def plot_data(TB, NT):
    plt.scatter(TB, NT, color='blue', label='Data Points')
    plt.xlabel('Durasi Waktu Belajar (TB)')
    plt.ylabel('Nilai Ujian Siswa (NT)')
    plt.title('Grafik Titik Data TB vs NT')
    plt.legend()
    plt.grid(True)
    plt.show()

def linear_regression(TB, NT):
    TB_reshaped = TB.reshape(-1, 1)
    linear_model = LinearRegression()
    linear_model.fit(TB_reshaped, NT)
    NT_pred_linear = linear_model.predict(TB_reshaped)
    RMS_linear = np.sqrt(np.mean((NT - NT_pred_linear) ** 2))
    
    plt.scatter(TB, NT, color='blue', label='Data Points')
    plt.plot(TB, NT_pred_linear, color='red', label='Linear Regression')
    plt.xlabel('Durasi Waktu Belajar (TB)')
    plt.ylabel('Nilai Ujian Siswa (NT)')
    plt.title('Regresi Linear TB vs NT')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return RMS_linear

def power_regression(TB, NT):
    def power_model(x, a, b):
        return a * np.power(x, b)
    
    params, _ = curve_fit(power_model, TB, NT)
    a, b = params
    NT_pred_power = power_model(TB, a, b)
    RMS_power = np.sqrt(np.mean((NT - NT_pred_power) ** 2))
    
    plt.scatter(TB, NT, color='blue', label='Data Points')
    TB_sorted = np.sort(TB)
    plt.plot(TB_sorted, power_model(TB_sorted, a, b), color='green', label='Power Regression')
    plt.xlabel('Durasi Waktu Belajar (TB)')
    plt.ylabel('Nilai Ujian Siswa (NT)')
    plt.title('Regresi Pangkat Sederhana TB vs NT')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return RMS_power

def growth_rate_regression(TB, NT):
    def growth_rate_model(x, a, b, c):
        return a * x / (b + x) + c
    
    params, _ = curve_fit(growth_rate_model, TB, NT, maxfev=10000)
    a, b, c = params
    NT_pred_growth = growth_rate_model(TB, a, b, c)
    RMS_growth = np.sqrt(np.mean((NT - NT_pred_growth) ** 2))
    
    plt.scatter(TB, NT, color='blue', label='Data Points')
    TB_sorted = np.sort(TB)
    plt.plot(TB_sorted, growth_rate_model(TB_sorted, a, b, c), color='purple', label='Growth Rate Regression')
    plt.xlabel('Durasi Waktu Belajar (TB)')
    plt.ylabel('Nilai Ujian Siswa (NT)')
    plt.title('Regresi Laju Pertumbuhan Jenuh TB vs NT')
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
            TB, NT = get_user_input()
            plot_data(TB, NT)
            RMS_linear = linear_regression(TB, NT)
            print("RMS Error for Linear Regression:", RMS_linear)
        elif pilihan == 2:
            TB, NT = get_user_input()
            plot_data(TB, NT)
            RMS_power = power_regression(TB, NT)
            print("RMS Error for Power Regression:", RMS_power)
        elif pilihan == 3:
            TB, NT = get_user_input()
            plot_data(TB, NT)
            RMS_growth = growth_rate_regression(TB, NT)
            print("RMS Error for Growth Rate Regression:", RMS_growth)
        elif pilihan == 4:
            print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
