#PROJECT EAS
import streamlit as st

st.title('SELAMAT DATANG DI WEB KAMI')
st.write("""
# PROJECT RUN FOR BAGINDA PAK ALMA
Dalam upaya pengendalian pencemaran udara, Kementerian Lingkungan Hidup dan
Kehutanan (KLHK) berkomitmen untuk memberikan informasi mutu udara yang tepat dan
akurat kepada masyarakat. Publik dapat mengetahui hasil pemantauan kualitas udara secara
real time di Indonesia melalui aplikasi berbasis android dan website ISPU Net. Selain kondisi
kualitas udara, data yang ditampilkan yaitu nilai kritis parameter, nilai kelembaban, nilai
tekanan udara, suhu, dan grafik parameter.
ISPU merupakan angka tanpa satuan, digunakan untuk menggambarkan kondisi mutu
udara ambien di lokasi tertentu dan didasarkan kepada dampak terhadap kesehatan manusia.
Perhitungan ISPU dilakukan berdasarkan nilai ISPU batas atas, ISPU batas bawah, ambient
batas atas, ambient batas bawah, dan konsentrasi ambient hasil pengukuran. Persamaan
matematika perhitungan ISPU sebagai berikut: """)

#PERHITUNGAN ISPU
st.write("""# YUK! CEK KONDISI UDARA MU!
Pastikan Input mu sesuai dengan data di Daerahmu ya...""")
Ia = st.number_input("ISPU Batas Atas ", 1)
Ib = st.number_input('ISPU Batas Bawah ', 1)
Xa = st.number_input(' Konsentrasi ambien batas atas (µg/m3)', 1)
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

#SIDEBAR
with st.sidebar:
    st.header('WELCOME TO OUR PAGE')
    st.write('A WEB PROJECT BY PL24 3C')

    #ABOUT US
    with st.expander(' **ABOUT US**'):
        st.info('SELAMAT DATANG DI WEB KAMI. Web ini dibuat untuk pemenuhan Tugas Akhir Mata Kuliah Pemrograman Dasar Semester 2 Studi Teknik Pengolahan Limbah. Web ini berisi mengenai Informasi serta Edukasi terhadap pencemaran udara. Harapan Besar kami dengan adanya Website ini dapat menambah wawasan serta kepekaan terhadap Pencermaran Udara. ')
