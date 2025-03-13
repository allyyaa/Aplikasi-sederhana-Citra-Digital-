import cv2

def main():
    # Meminta pengguna untuk memasukkan path file gambar di drive D
    file_path = input("Masukkan path file gambar: ")

    # Membaca citra menggunakan OpenCV
    image = cv2.imread(file_path)

    # Memeriksa apakah gambar berhasil dibaca
    if image is None:
        print("Gambar tidak ditemukan. Pastikan path yang dimasukkan benar.")
        return

    # Mengubah citra dari BGR ke RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Mengakses 10 nilai piksel pertama
    print("10 nilai piksel pertama (RGB):")
    for i in range(10):
        # Mengambil koordinat piksel (i, 0) untuk mendapatkan 10 piksel pertama di baris pertama
        if i < image.shape[0]:  # Memastikan tidak melebihi jumlah baris
            pixel_value = image_rgb[i, 0]
            print(f"Piksel {i + 1}: R={pixel_value[0]}, G={pixel_value[1]}, B={pixel_value[2]}")
        else:
            print(f"Piksel {i + 1}: Tidak ada data (melebihi ukuran gambar)")

if __name__ == "__main__":
    main()