def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()

    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan harus C, F, atau K."

    if dari == "k" and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif."
    if dari in ["c", "f"] and nilai < -273.15:
        return "Error: Suhu tidak boleh lebih rendah dari -273.15°C."

    if dari == ke:
        return nilai

    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5/9
    elif dari == "k":
        c = nilai - 273.15

    if ke == "c":
        return c
    elif ke == "f":
        return c * 9/5 + 32
    elif ke == "k":
        return c + 273.15
