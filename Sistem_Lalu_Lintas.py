import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameter simulasi
waktu_simulasi = 200        # durasi waktu simulasi (dalam detik)
delta_t = 1                 # interval waktu (dalam detik)
panjang_antrian_maks = 20   # panjang maksimum antrian kendaraan di persimpangan
kecepatan_rata = 0.2        # kecepatan rata-rata kendaraan (per detik)
kedatangan_kendaraan = 0.3  # probabilitas kendaraan baru tiba setiap detik
waktu_hijau = 10            # durasi lampu hijau (dalam detik)
waktu_merah = 10            # durasi lampu merah (dalam detik)

# Variabel waktu dan antrian
waktu_lampu = waktu_hijau + waktu_merah
antrian = 0  # panjang antrian kendaraan saat ini
data_antrian = []  # untuk menyimpan data panjang antrian sepanjang waktu

def simulasi_lalu_lintas(t):
    global antrian
    fase_lampu = (t // waktu_lampu) % 2  # 0: hijau, 1: merah
    kendaraan_masuk = np.random.rand() < kedatangan_kendaraan

    # Tambah kendaraan ke antrian
    if kendaraan_masuk and antrian < panjang_antrian_maks:
        antrian += 1

    # Keluarkan kendaraan jika lampu hijau
    if fase_lampu == 0:  # lampu hijau
        antrian -= min(antrian, int(kecepatan_rata * delta_t))
        
    # Simpan data panjang antrian untuk visualisasi
    data_antrian.append(antrian)

# Simulasi
for t in range(waktu_simulasi):
    simulasi_lalu_lintas(t)

# Visualisasi hasil simulasi
fig, ax = plt.subplots()
ax.set_xlim(0, waktu_simulasi)
ax.set_ylim(0, panjang_antrian_maks + 1)
ax.set_title("Simulasi Dinamika Antrian Kendaraan di Persimpangan")
ax.set_xlabel("Waktu (detik)")
ax.set_ylabel("Panjang Antrian Kendaraan")

line, = ax.plot([], [], lw=2)

def update(frame):
    line.set_data(range(frame), data_antrian[:frame])
    return line,

ani = animation.FuncAnimation(fig, update, frames=waktu_simulasi, interval=100, blit=True)
plt.show()
