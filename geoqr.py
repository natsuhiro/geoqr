import streamlit as st
from streamlit_geolocation import streamlit_geolocation
import qrcode
import io

location = streamlit_geolocation()

if location["latitude"]!=None:
    lat=location["latitude"]
    lon=location["longitude"]
    url = f"http://maps.google.com/maps?ll={lat},{lon}"

    img=qrcode.make(url)
    with io.BytesIO() as f:
        img.save(f,format="PNG")
        png = f.getvalue()
    st.write(url)
    st.image(png)
    st.download_button("Download",data=png,file_name="geoqr.png")
else:
    st.write("位置情報が取得できません")
