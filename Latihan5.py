import streamlit as st
from PIL import Image
def tampilkan_gambar(link) :
    img=Image.open(link)
    img=img.resize((300,300))
    st.image(img)

st.set_page_config(layout="wide")
st.title('REKOMENDASI')
st.divider()
with st.container ():
    col1, col2, col3, col4, col5, col6=st.columns([1,1,1,1,1,1])
    with col1 :
        st.image('https://www.lunss.com/uploads/product/1/Y/1Y446/beaded-wine-lace-long-prom-dress-with-overskirt-1.webp')
        st.header('Gaun pengantin')  
        st.write('Rp. 1.000.000') 
    with col2 :   
        st.image('https://www.lunss.com/uploads/product/1/Y/1Y446/beaded-wine-lace-long-prom-dress-with-overskirt-1.webp')
        st.header('Gaun pengantin')  
        st.write('Rp. 1.500.000') 
    with col3 :
        st.image('https://www.lunss.com/uploads/product/1/Y/1Y446/beaded-wine-lace-long-prom-dress-with-overskirt-1.webp')
        st.header('Gaun pengantin')  
        st.write('Rp. 1.000.000') 
    with col4 :
        st.image('https://www.lunss.com/uploads/product/1/Y/1Y446/beaded-wine-lace-long-prom-dress-with-overskirt-1.webp')
        st.header('Gaun pengantin')  
        st.write('Rp. 1.000.000') 
    with col5 :
        st.image('https://www.lunss.com/uploads/product/1/Y/1Y446/beaded-wine-lace-long-prom-dress-with-overskirt-1.webp')
        st.header('Gaun pengantin')  
        st.write('Rp. 1.000.000') 
    with col6 :
        st.image('https://www.lunss.com/uploads/product/1/Y/1Y446/beaded-wine-lace-long-prom-dress-with-overskirt-1.webp')
        st.header('Gaun pengantin')  
        st.write('Rp. 1.700.000') 

with st.container():
    col1,col2,col3,col4,col5= st.columns([1,1,1,1,1])
    with col1 :
        tampilkan_gambar('C:\KODING\gambar\gbr 1.jfif')
        st.header('Alat Dapur Kita')
        st.write('Rp 1.250.000')
    with col2 :
        tampilkan_gambar('C:\KODING\gambar\gbr 2.jfif')
        st.header('Pisau Serba Guna')
        st.write('Rp 500.000')
    with col3 :
        tampilkan_gambar('C:\KODING\gambar\gbr 3.jfif')
        st.header('Set Alat Masak')
        st.write('Rp 250.000')
    with col4 :
        tampilkan_gambar('C:\KODING\gambar\gbr 4.jfif')
        st.header('Alat masak silikon')
        st.write('Rp. 350.000')
    with col5 :
        tampilkan_gambar('C:\KODING\gambar\gbr 4.jfif')
        st.header('storege kayu')
        st.write('Rp 200.000')
                

