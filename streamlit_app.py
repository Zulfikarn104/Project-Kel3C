#PROJECT EAS
import streamlit as st

st.title('SELAMAT DATANG')
st.write("""
# LATAR BELAKANG
Dalam upaya pengendalian pencemaran udara, Kementerian Lingkungan Hidup dan
Kehutanan (KLHK) berkomitmen untuk memberikan informasi mutu udara yang tepat dan
akurat kepada masyarakat. Publik dapat mengetahui hasil pemantauan kualitas udara secara
real time di Indonesia melalui aplikasi berbasis android dan website ISPU Net. Selain kondisi
kualitas udara, data yang ditampilkan yaitu nilai kritis parameter, nilai kelembaban, nilai
tekanan udara, suhu, dan grafik parameter.
ISPU merupakan angka tanpa satuan, digunakan untuk menggambarkan kondisi mutu
udara ambien di lokasi tertentu dan didasarkan kepada dampak terhadap kesehatan manusia.
Perhitungan ISPU dilakukan berdasarkan nilai ISPU batas atas, ISPU batas bawah, ambient
batas atas, ambient batas bawah, dan konsentrasi ambient hasil pengukuran. Untuk mengecek kondisi udaramu bisa dibawah ini yaa..""")


#PERHITUNGAN ISPU
st.write("""# YUK! CEK KONDISI UDARA MU!
Pastikan Input mu sesuai dengan data di Daerahmu ya...""")
Ia = st.number_input("ISPU Batas Atas ", 0)
Ib = st.number_input('ISPU Batas Bawah ', 1)
Xa = st.number_input(' Konsentrasi ambien batas atas (µg/m3)', 0)
Xb = st.number_input('Konsentrasi ambien batas bawah (µg/m3)', 1)
Xx = st.number_input('Konsentrasi ambien nyata hasil pengukuran (µg/m3)', 1)
Submit = st.button('SUBMIT!')

Hasil = (Ia-Ib)/(Xa-Xb)*(Xx-Xb) + Ib

if Submit:
    st.write(f"HASIL PERHITUNGAN = {Hasil}")
    if Hasil >= 1 and Hasil <=50:
        st.success(f"WAHH Indeks Udara sekitarmu tergolong 'BAIK!!' ")
    elif Hasil >= 51 and Hasil <= 100:
        st.info(f"JAGA KESEHATAN YA... Indeks Udara sekitarmu tergolong 'SEDANG'")
    elif Hasil >= 101 and Hasil <= 200:
        st.warning(f"WASPADA! Indeks Udara sekitarmu tergolong 'TIDAK SEHAT!'")
    elif Hasil >= 201 and Hasil <= 300:
        st.error(f"GAWAT!! INDEKS UDARA SEKITAR MU 'SANGAT TIDAK SEHAT!'")
    elif Hasil >= 301:
        st.error(f"BAHAYA!!! INDEKS UDARA SEKITAR MU 'BERBAHAYA!'")
    elif ZeroDivisionError:
        st.info(' ***Masukkan Nomor Input*** ')

with st.expander('***MORE INFORMATION***'):
    st.caption('KATEGORI ISPU (Indeks Standar Pencemar Udara)')
    st.info('1-50 Baik; 51-100 Sedang; 101-200 Tidak Sehat; 201-300 Sangat Tidak Sehat')

#ARTIKEL
st.write("""
         # PENGERTIAN DAN JENIS LIMBAH GAS
Limbah gas merupakan hasil buangan yang menggunakan udara sebagai medianya dan udara secara alami  mengandung unsur-unsur kimia seperti O2, N2, NO2, CO2, dan H2.

Zat pencemar udara dibagi menjadi dua bagian: partikel dan gas, berikut :

**A. Partikel** : partikel kecil dan dapat dilihat dengan mata telanjang.
 Contoh: uap air, debu, asap, kabut, kabut.

**B. Gas** : hanya dapat dirasakan melalui baunya (gas tertentu) atau akibat langsungnya.
 	
**Materi Partikulat** : Limbah gas yang dilepaskan ke udara biasanya mengandung partikel bahan padat atau cair yang  sangat kecil dan ringan yang tersuspensi dalam gas. Contoh : gas yang dihasilkan dari pabrik berupa asap, partikel, dan debu.
""")
st.write("""
         # PENYEBAB PENCEMARAN UDARA""")
a = '''**1. Aktivitas Pertambangan :**
aktivitas pertambangan dapat menghasilkan debu dan bahan kimia lainnya yang akhirnya dilepaskan ke udara. hal tersebut dilakukan untuk mengekstraksi mineral yang ada di bawah bumi menggunakan alat besar yang menggunakan bahan bakar untuk menggerakkannya.

**2. aktivitas pertanian :** 
para petani sering menggunakan pupuk kimia yang dapat mempengaruhi proses panen mereka dan ketika melakukan kegiatan pembakaran lahan maka gas ataupun asap yang dikeluarkan akan lebih berbahaya dan menimbulkan pencemaran udara.

**3. penggunaan listrik yang berlebihan :**
hal ini dikarenakan dalam membuat listrik di indonesia masih mengandalkan bahan bakar batu bara. oleh sebab itu, semakin banyaknya penggunaan listrik maka limbah batu bara yang akan dibuang ke udara akan semakin banyak dan menimbulkan pencemaran udara.

**4. asap yang dihasilkan pabrik :**
pada sebuah pabrik biasanya asap tersebut dibuang melalui cerobong asap besar dalam jumlah yang besar. asap yang dikeluarkan industri pabrik merupakan salah satu penyumbang terbesar gas karbon yang ada di udara. namun bukan hanya mencemari udara tetapi juga menimbulkan terjadinya pemanasan global.

**5.limbah yang dihasilkan rumah tangga :**
kegiatan rumah tangga seringkali menghasilkan sampah. sampah tersebut kemudian dibuang dan dibakar sehingga menghasilkan asap yang membuat munculnya pencemaran udara. 
'''
st.markdown(a)

st.write(''' # JADI.. SOLUSINYA APA??
Untuk menangani hal tersebut kamu bisa loh dengan mengganti kebiasaan mu... Seperti,
###### 1. Jalan kaki dan megendarai sepeda
###### 2. Bercocok tanam 
###### 3. Tidak membakar sampah
###### 4. Menghemat penggunaan listrik 
tapi masih banyak lagi lohh.. hal yang bisa kamu lakuin untuk mengurangi pencemaran ini. ''')

st.write(""" # KESIMPULAN
limbah gas merupakan isu lingkungan yang signifikan yang perlu diperhatikan dengan serius. limbah gas industri, transportasi, dan pertanian memiliki dampak negatif terhadap kualitas udara, tanah, air, dan ekosistem. manajemen limbah gas adalah tanggung jawab bersama untuk generasi saat ini dan masa depan kita. """)

#SIDEBAR
with st.sidebar:
    st.header('WELCOME TO OUR PAGE')
    st.write('A WEB PROJECT BY PL23 C3')

    #ABOUT US
    with st.expander(' **ABOUT US**'):
        st.info('SELAMAT DATANG DI WEB KAMI. Web ini dibuat untuk pemenuhan Tugas Akhir Mata Kuliah Pemrograman Dasar Semester 2 Studi Teknik Pengolahan Limbah. Web ini berisi mengenai Informasi serta Edukasi terhadap pencemaran udara. Harapan Besar kami dengan adanya Website ini dapat menambah wawasan serta kepekaan terhadap Pencermaran Udara. ')

    with st.expander('**FITUR**'):
        st.warning('Dalam Web ini anda dapat mengetahui info seputar Pencemaran Udara serta Dapat Menghitung secara otomatis Indeks Udara ISPU dengan parameternya.')

    with st.expander('**DAFTAR ISI**'):
        st.success('''1. Latar Belakang
2. Perhitungan ISPU
3. Pengertian dan Jenis Limbah Gas
4. Penyebab Pencemaran Udara
5. Solusi Pencemaran Udara
6. Kesimpulan 
                   ''')
    st.caption('*Develop by* **MOCH ZULFIKAR NAIM**')
    st.caption('*Support by* **SHOFWATUL QOLBIA & ERLINA MUSTAFA**')

