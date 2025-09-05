from utils import konversi_suhu

print("=== KONVERSI SUHU ===")

try:
    nilai = float(input("Masukkan nilai suhu: "))
    dari = input("Dari satuan (C/F/K): ").strip()
    ke = input("Ke satuan (C/F/K): ").strip()

    hasil = konversi_suhu(nilai, dari, ke)

    if isinstance(hasil, str):
        print(hasil)
    else:
        print(f"Hasil: {nilai}{dari.upper()} = {round(hasil, 2)}{ke.upper()}")
except ValueError:
    print("Error: Input nilai suhu harus berupa angka!")
