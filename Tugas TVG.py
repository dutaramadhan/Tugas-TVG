import numpy as np
import matplotlib.pyplot as plt

#membuat fungsi translasi
def translasi(objek):
    #meminta input dari user berupa besarnya translasi yang akan dilakukan
    tx=float(input("Objek akan ditranslasi terhadap sumbu-x sejauh: "))
    ty=float(input("Objek akan ditranslasi terhadap sumbu-y sejauh: "))
    #menentukan matriks translasi
    matriks_translasi=np.array([[1,0,tx],
                               [0,1,ty],
                               [0,0,1]])
    homogen = np.ones((len(objek), 1))
    objek_homogen = np.hstack((objek, homogen))

    # Melakukan translasi dengan mengalikan matriks transformasi dengan vektor homogen
    objek_translasi_homogen = np.dot(matriks_translasi, objek_homogen.T).T

    # Menghapus komponen homogen dari vektor hasil translasi
    objek_translasi = objek_translasi_homogen[:, :2]

    # Menampilkan objek setelah translasi
    fig, ax = plt.subplots()
    ax.plot(objek[:, 0], objek[:, 1], color='r')
    ax.plot(objek_translasi[:, 0], objek_translasi[:, 1], color='b')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')
    ax.grid(True)
    plt.title("Bangun datar setelah ditranslasi")
    plt.show()

#membuat fungai rotasi
def rotasi(objek):
    #meminta input dari user berupa sudut dan pusat rotasi
    sudut_derajat=float(input("Objek akan dirotasi sebesar(dalam derajat): "))
    sudut_radian=np.radians(sudut_derajat)
    tx=float(input("Pusat rotasi pada titik di sumbu-x: "))
    ty=float(input("Pusat rotasi pada titik di sumbu-y: "))
    #membuat komponen-komponen dari matrix rotasi
    matriks_translasi_pusat_koordinat=np.array([[1,0,-tx],
                                                [0,1,-ty],
                                                [0,0,1]])
    matriks_rotasi=np.array([[np.cos(sudut_radian),-np.sin(sudut_radian),0],
                             [np.sin(sudut_radian),np.cos(sudut_radian),0],
                             [0,0,1]])
    matriks_translasi_titik_awal=np.array([[1,0,tx],
                                          [0,1,ty],
                                          [0,0,1]])
    matriks_rotasi_gabungan =matriks_translasi_titik_awal @ matriks_rotasi @ matriks_translasi_pusat_koordinat
    #membuat vektor awal menjadi vektor homogen
    homogen = np.ones((len(objek), 1))
    objek_homogen = np.hstack((objek, homogen))
    # Melakukan rotasi dengan mengalikan matriks transformasi dengan vektor homogen
    objek_rotasi_homogen = np.dot(matriks_rotasi_gabungan, objek_homogen.T).T
     # Menghapus komponen homogen dari vektor hasil rotasi
    objek_rotasi = objek_rotasi_homogen[:, :2]
    #menampilkan objek setelah rotasi
    fig, ax = plt.subplots()
    ax.plot(objek[:, 0], objek[:, 1], color='r')
    ax.plot(objek_rotasi[:, 0], objek_rotasi[:, 1], color='b')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')
    ax.grid(True)
    plt.title("Bangun datar setelah dirotasi")
    plt.show()

#membuat fungsi scaling
def scaling(objek):
    #meminta input dari user berupa  seberapa besar scaling akan dilakukan
    sx=float(input("Objek akan di scale terhadap sumbu-x sebesar: "))
    sy=float(input("Objek akan di scale terhadap sumbu-y sebesar: "))
    #menentukan matriks scaling
    matriks_scaling=np.array([[sx,0,0],
                              [0,sy,0],
                              [0,0,1]])
     #membuat vektor awal menjadi vektor homogen
    homogen = np.ones((len(objek), 1))
    objek_homogen = np.hstack((objek, homogen))
    # Melakukan scaling dengan mengalikan matriks transformasi dengan vektor homogen
    objek_scaling_homogen = np.dot(matriks_scaling, objek_homogen.T).T
    # Menghapus komponen homogen dari vektor hasil scaling
    objek_scaling = objek_scaling_homogen[:, :2]
    #menampilkan objek setelah scaling
    fig, ax = plt.subplots()
    ax.plot(objek[:, 0], objek[:, 1], color='r')
    ax.plot(objek_scaling[:, 0], objek_scaling[:, 1], color='b')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')
    ax.grid(True)
    plt.title("Bangun datar setelah discaling")
    plt.show()

#membuat fungsi refleksi
def refleksi(objek):
    #meminta input dari user berupa terhadap sumbu apa refleksi akan dilakukan
    jenis_refleksi=int(input("Objek akan direfleksikan terhadap sumbu x atau y(1. X, 2. y): "))
    #membuat vektor awal menjadi vektor homogen
    homogen = np.ones((len(objek), 1))
    objek_homogen = np.hstack((objek, homogen))
    if jenis_refleksi==1:
        #menentukan matriks refleksi terhadap sumbu-x
        matriks_refleksi_x=np.array([[1,0,0],
                                     [0,-1,0],
                                     [0,0,1]])
        # Melakukan refleksi terhadap sumbu x dengan mengalikan matriks transformasi dengan vektor homogen
        objek_refleksi_homogen = np.dot(matriks_refleksi_x, objek_homogen.T).T
    elif jenis_refleksi==2:
        #menentukan matriks refleksi terhadap sumbu-y
        matriks_refleksi_y=np.array([[-1,0,0],
                                     [0,1,0],
                                     [0,0,1]])
        # Melakukan refleksi terhadap sumbu y dengan mengalikan matriks transformasi dengan vektor homogen
        objek_refleksi_homogen = np.dot(matriks_refleksi_y, objek_homogen.T).T
     # Menghapus komponen homogen dari vektor hasil refleksi
    objek_refleksi = objek_refleksi_homogen[:, :2]
    #menampilkan objek setelah scaling
    fig, ax = plt.subplots()
    ax.plot(objek[:, 0], objek[:, 1], color='r')
    ax.plot(objek_refleksi[:, 0], objek_refleksi[:, 1], color='b')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')
    ax.grid(True)
    plt.title("Bangun datar setelah direfleksi")
    plt.show()

#membuat fungsi shear
def shear(objek):
    #meminta input dari user berupa seberapa besar shear akan dilakukan
    shx=float(input("Objek akan dilakukan transformasi shear horizontal(terhadap sumbu-x) sebesar: "))
    shy=float(input("Objek akan dilakukan transformasi shear vertikal(terhadap sumbu-y) sebesar: "))
    #menentukan matriks shear
    matriks_shear=np.array([[1,shx,0],
                            [shy,1,0],
                            [0,0,1]])
    #membuat vektor awal menjadi vektor homogen
    homogen = np.ones((len(objek), 1))
    objek_homogen = np.hstack((objek, homogen))
    # Melakukan shear dengan mengalikan matriks transformasi dengan vektor homogen
    objek_shear_homogen = np.dot(matriks_shear, objek_homogen.T).T
    # Menghapus komponen homogen dari vektor hasil shear
    objek_shear = objek_shear_homogen[:, :2]
    #menampilkan objek setelah scaling
    fig, ax = plt.subplots()
    ax.plot(objek[:, 0], objek[:, 1], color='r')
    ax.plot(objek_shear[:, 0], objek_shear[:, 1], color='b')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')
    ax.grid(True)
    plt.title("Bangun datar setelah dishear")
    plt.show()


#meminta input dari user bangun data yang ingin ditransformasi
bangun_datar=int(input("Masukan bangun datar yang ingin anda transformasikan(1. Kotak, 2. Segitiga, 3. Lingkaran): "))

if bangun_datar==1:
    # Meminta input untuk titik 1
    x1 = float(input("Masukkan nilai koordinat x untuk titik 1: "))
    y1 = float(input("Masukkan nilai koordinat y untuk titik 1: "))

    # Meminta input untuk titik 2
    x2 = float(input("Masukkan nilai koordinat x untuk titik 2: "))
    y2 = float(input("Masukkan nilai koordinat y untuk titik 2: "))

    # Meminta input untuk titik 3
    x3 = float(input("Masukkan nilai koordinat x untuk titik 3: "))
    y3 = float(input("Masukkan nilai koordinat y untuk titik 3: "))

    # Meminta input untuk titik 4
    x4 = float(input("Masukkan nilai koordinat x untuk titik 4: "))
    y4 = float(input("Masukkan nilai koordinat y untuk titik 4: "))

    # Membuat array dari input pengguna
    pts = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4],[x1, y1]])
    #menampilkan objek sebelum dilakukan transformasi geometri
    fig, ax = plt.subplots()
    ax.plot(pts[:, 0], pts[:, 1], color='r')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')
    ax.grid(True)
    plt.title("Bangun datar sebelum ditransformasi")
    plt.show()
    #meminta pengguna untuk menginput jenis transformasi manakah yang ingin mereka lakukan
    jenis_transformasi=int(input("Masukan jenis transformasi yang ingin anda lakukan(1. Translasi, 2. Rotasi, 3. Scaling, 4. Refleksi, 5.Shear): "))
    if jenis_transformasi==1:
        translasi(pts)
    elif jenis_transformasi==2:
        rotasi(pts)
    elif jenis_transformasi==3:
        scaling(pts)
    elif jenis_transformasi==4:
        refleksi(pts)
    elif jenis_transformasi==5:
        shear(pts)
elif bangun_datar==2:
    # Meminta input untuk titik 1
    x1 = float(input("Masukkan nilai koordinat x untuk titik 1: "))
    y1 = float(input("Masukkan nilai koordinat y untuk titik 1: "))

    # Meminta input untuk titik 2
    x2 = float(input("Masukkan nilai koordinat x untuk titik 2: "))
    y2 = float(input("Masukkan nilai koordinat y untuk titik 2: "))

    # Meminta input untuk titik 3
    x3 = float(input("Masukkan nilai koordinat x untuk titik 3: "))
    y3 = float(input("Masukkan nilai koordinat y untuk titik 3: "))
    # Membuat array dari input pengguna
    pts = np.array([[x1, y1], [x2, y2], [x3, y3],[x1, y1]])
    #menampilkan objek sebelum dilakukan transformasi geometri
    fig, ax = plt.subplots()
    ax.plot(pts[:, 0], pts[:, 1], color='r')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')
    ax.grid(True)
    plt.title("Bangun datar sebelum ditransformasi")
    plt.show()

