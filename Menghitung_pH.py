import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
from PIL import Image

with st.sidebar :
    navbar = option_menu(menu_title=None,
             options=['Home', 'Asam Kuat oleh Basa Kuat', 'Basa Lemah oleh Asam Kuat', 'Basa Kuat oleh Asam Kuat', 'Asam Lemah oleh Basa Kuat'])
if navbar == 'Home':
    st.title('Aplikasi penghitung Kadar pH :red[Titrasi Asam Basa]')
    st.write('dibuat oleh: **kelompok 3**')
    st.write('**Annisa Nabillah** (2219035)')
    st.write('**Aulia Falina Putri** (2219042)')
    st.write('**Muhammad Ramlan Agustian** (2219117)')
    st.write('**Reisya Putri Aprianti** (2219155)')
    
    st.header("Dasar :red[Teori :]")
    st.markdown("""pH merupakan ukuran atau derajat yang digunakan untuk menyatakan tingkat keasaman atau kebasaan yang dimiliki oleh suatu larutan. Ia didefinisikan sebagai algoritma aktivitas ion hidrogen yang terlarut. Rentang pH berkisar antara 0 hingga 14. Di mana jika suatu larutan mempunyai pH kurang dari 7, maka larutan tersebut bersifat asam, pH lebih dari 7 bersifat basa, dan pH sama dengan 7 bersifat netral.Skala pH menunjukkan konsentrasi ion hidrogen [H+] dalam larutan.Nilai pH larutan dihitung menggunakan nilai konsentrasi molar ion hidrogen yang larut dalam larutan.<br>
<br>	Suatu larutan bersifat asam jika terdapat ion H+ yang lebih banyak daripada ion OH–. Asam memiliki pH<7
<br>	Bersifat netral jika jumlah ion H+ dan OH– sama dalam larutan. Larutan netral memiliki pH=7
<br>	Larutan basa jika terdapat jumlah ion OH– lebih banyak dibanding H+. Basa memiliki pH>7

Dalam penerapan ilmu kimia,memahami pH adalah hal yang wajib dilakukan.Contohnya adalah pengukuran pH pada larutan bersifat asam, maupun basa seperti HCL,NaOH,CH3COOH.Untuk mengkategorikan suatu larutan bersifat asam atau basa dapat menggunakan alat berupa kertas lakmus,indikator pH,alat pH meter atau dapat dihitung menggunakan rumus persamaan dalam menghitung pH.yaitu:


                
Lingkup aplikasi web ini akan membahas mengenai :<br>
•	Menghitung pH dan pOH dari asam basa kuat,<br>
•	Menghitung pH dan pOH dari asam basa lemah,<br>
•	Menghitung pH dan pOH dari buffer atau larutan penyangga, dan<br>
•	Menghitung pH dari garam hidrolisis.<br>
<br>Pengukuran pH sangatlah penting dalam bidang yang terkait dengan kehidupan atau industri pengolahan kimia.Seperti kimia, biologi, kedokteran, pertanian, ilmu pangan, rekayasa (keteknikan), dan oseanografi. Tentu saja, pada bidang-bidang sains dan teknologi lainnya.""", unsafe_allow_html=True)

if navbar == 'Asam Kuat oleh Basa Kuat' :
    st.title('Menghitung kadar pH titrasi :green[Asam Kuat oleh Basa Kuat]')
    st.header("Rumus yang digunakan : ")
    st.write('\n')
    st.image(Image.open("gambar_1.png"))
    st.image(Image.open("gambar_2.png"))
    st.image(Image.open("gambar_3.png"))
    st.image(Image.open("gambar_5.png"))
    st.image(Image.open("gambar_6.png"))
    st.write("---")
    
    st.selectbox("Silahkan pilih larutan titran :red[(basa)]",("NaOH","KOH","LiOH"))
    st.selectbox("Silahkan pilih larutan titrat :blue[(asam)]",("HCl","HNO3","HBr","HI"))
    
    st.write("---")
    M_titrat= st.number_input('masukkan :blue[Molaritas titrat]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titrat= st.number_input('masukkan :blue[mL titrat]',value = 25.00)
    M_titran= st.number_input('masukkan :red[Molaritas titran]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titran= st.number_input('masukkan :red[mL titran]',value = 25.00)

    mmol_titrat= M_titrat * V_titrat
    mmol_titran= M_titran * V_titran
    V_total= V_titrat + V_titran

    sisa_mol= abs(mmol_titran - mmol_titrat)
    Konsentrasi= sisa_mol/V_total

    pH = round(-(np.log10(Konsentrasi)),2)
    if st.button('tampilkan nilai ph') :
        if mmol_titran < mmol_titrat :
            st.success(f'nilai pH adalah : {pH}')
        elif mmol_titran == mmol_titrat :
            st.success(f'nilai pH adalah : 7' )
        else :
            st.success(f'nilai pH adalah : {14 - pH}')
    else :
        st.write('tekan tombol untuk memunculkan nilai')

if navbar == 'Basa Lemah oleh Asam Kuat':
    st.title('Menghitung kadar pH titrasi :green[Basa Lemah oleh Asam Kuat]')
    st.header("Rumus yang digunakan : ")
    st.write('\n')
    st.image(Image.open("gambar_1.png"))
    st.image(Image.open("gambar_2.png"))
    st.image(Image.open("gambar_4.png"),width = 200)
    st.image(Image.open("gambar_5.png"))
    st.image(Image.open("gambar_6.png"))
    st.image(Image.open("gambar_7.png"),width = 200)
    st.write("---")
    
    st.selectbox("Silahkan pilih larutan titran :blue[(asam)]",("HCl","HNO3","HBr","HI"))
    st.selectbox("Silahkan pilih larutan titrat :red[(basa lemah)]",("NH3","NH4OH","NaHCO3"))
    st.write("---")
    
    M_titran= st.number_input('masukkan :blue[Molaritas titran]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titran= st.number_input('masukkan :blue[mL titran]',value = 25.00)
    
    ka_titrat = st.number_input('masukkan :violet[Kb titrat (10^5)]',value = 1.8)
    kb = ka_titrat * 10**(-5)
    
    M_titrat= st.number_input('masukkan :red[Molaritas titrat]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titrat= st.number_input('masukkan :red[mL titrat]',value = 25.00)

    mmol_titrat= round((M_titrat * V_titrat),2)
    mmol_titran= round((M_titran * V_titran),2)
    V_total= V_titrat + V_titran

    sisa_mol= abs(mmol_titran - mmol_titrat)
      
    if st.button('tampilkan nilai pH') :
        
        # Garam Terhodirolisis
        if mmol_titran == mmol_titrat :
            Cg = round((mmol_titran/V_total),3)
            konsentrasi = np.sqrt((10**(-14)/kb)*Cg)
            pH = round(-(np.log10(konsentrasi)),2)
            st.success(f'Nilai pH adalah  {pH} :green[Garam Terhidrolisis]')
         # Asam   
        elif mmol_titran > mmol_titrat  :
            konsentrasi = (sisa_mol/V_total)
            pH = round(-(np.log10(konsentrasi)),2)
            st.success(f'Nilai pH adalah {pH} :green[Asam]')
        #Buffer    
        else :
            Cg = mmol_titran
            konsentrasi = ((mmol_titrat-Cg)/Cg) *kb
            ph = round(-(np.log10(konsentrasi)),2)
            st.success(f'Nilai pH adalah {14 - ph} :green[[Buffer]]')
    else :
        st.write('Tekan tombol untuk memunculukan nilah pH')
    
if navbar ==  'Basa Kuat oleh Asam Kuat':
    st.title('Menghitung kadar pH titrasi :green[Basa Kuat oleh Asam Kuat]')
    st.header("Rumus yang digunakan : ")
    st.write('\n')
    
    st.image(Image.open("gambar_1.png"))
    st.image(Image.open("gambar_2.png"))
    st.image(Image.open("gambar_3.png"))
    st.image(Image.open("gambar_5.png"))
    st.image(Image.open("gambar_6.png"))
    st.write("---")
    
    st.selectbox("Silahkan pilih larutan titrat :blue[(basa)]",("NaOH","KOH","LiOH"))
    st.selectbox("Silahkan pilih larutan titran :red[(asam)]",("HCl","HNO3","HBr","HI"))
    st.write("---")
    
    M_titrat= st.number_input('masukkan :blue[Molaritas titrat]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titrat= st.number_input('masukkan :blue[mL titrat]',value = 25.00)
    M_titran= st.number_input('masukkan :red[Molaritas titran]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titran= st.number_input('masukkan :red[mL titran]',value = 25.00)

    mmol_titrat= M_titrat * V_titrat
    mmol_titran= M_titran * V_titran
    V_total= V_titrat + V_titran

    sisa_mol= abs(mmol_titran - mmol_titrat)
    Konsentrasi= sisa_mol/V_total

    pH = round(-(np.log10(Konsentrasi)),2)
    if st.button('tampilkan nilai ph') :
        if mmol_titran > mmol_titrat :
            st.success(f'nilai pH adalah : {14 - pH}')
        elif mmol_titran == mmol_titrat :
            st.success('nilai pH adalah :  7')
        else :
            st.success(f'nilai pH adalah : {pH}')
    else :
        st.write('tekan tombol untuk memunculkan nilai')
        
if navbar == 'Asam Lemah oleh Basa Kuat':
    st.title('Menghitung kadar pH titrasi :green[Asam Lemah oleh Basa Kuat]')
    st.write('\n')
    
    st.image(Image.open("gambar_5.png"))
    st.image(Image.open("gambar_3.png"))
    st.image(Image.open("gambar_8.png"),width = 200)
    st.image(Image.open("gambar_1.png"))
    st.image(Image.open("gambar_6.png"))
    st.image(Image.open("gambar_9.png"),width = 200)
    st.write("---")
    
    st.selectbox("Silahkan pilih larutan titrat :red[(asam lemah)]",("CH3COOH","H2C2O4","HF","HClO"))
    st.selectbox("Silahkan pilih larutan titran :blue[(basa)]",("NaOH","LiOH","KOH"))
    st.write("---")
    
    M_titran= st.number_input('masukkan :blue[Molaritas titran]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titran= st.number_input('masukkan :blue[mL titran]',value = 25.00)
    ka_titrat = st.number_input('masukkan :violet[Ka titrat (10^-5)]', value = 1.8)
    
    ka = ka_titrat * 10**(-5)
    M_titrat= st.number_input('masukkan :red[Molaritas titrat]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titrat= st.number_input('masukkan :red[mL titrat]',value = 25.00)

    mmol_titrat= round((M_titrat * V_titrat),2)
    mmol_titran= round((M_titran * V_titran),2)
    V_total= V_titrat + V_titran
    
    sisa_mol= abs(mmol_titran - mmol_titrat)
    
    if st.button('tampilkan nilai pH') :
        
        # Garam Terhodirolisis
        if mmol_titran == mmol_titrat :
            Cg = round((mmol_titran/V_total),3)
            konsentrasi = np.sqrt((10**(-14)/ka)*Cg)
            pH = round(-(np.log10(konsentrasi)),2)
            st.success(f'Nilai pH adalah  {round((14 - pH),2)} :green[[Garam Terhidrolisis]]')
        # Basa    
        elif mmol_titran > mmol_titrat  :
            konsentrasi = (sisa_mol/V_total)
            pH = round(-(np.log10(konsentrasi)),2)
            st.success(f'Nilai pH adalah {round((14 - pH),2)} :green[[Basa]]')
        # Buffer
        else :
            Cg = mmol_titran
            konsentrasi = ((mmol_titrat-Cg)/Cg) * ka
            ph = round(-(np.log10(konsentrasi)),2)
            st.success(f'Nilai pH adalah {round((ph),2)}  :green[[Buffer]]')
    else :
        st.write('Tekan tombol untuk memunculukan nilah pH')

        
    