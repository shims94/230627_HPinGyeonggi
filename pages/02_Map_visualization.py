import streamlit as st
from streamlit_folium import st_folium
import folium
import common

st.title("Map Visualization")
common.page_config()

df = common.get_dataset()
# 초기 맵
map_gyeonggi = folium.Map(location=[37.291887, 126.996340], zoom_start=10)
st_folium(map_gyeonggi)

# 업무 구분명이 지역센터나 기관일경우 녹색 하트마커, 그이외(광역) 빨강 스타마커
# for index, row in df.iterrows():
#     if row['업무구분명'] == '지역센터' or row['업무구분명'] == '지역기관':
#         folium.Marker(location = [row['위도'], row['경도']],
#                       popup=row['병원또는센터명'],
#                       icon=folium.Icon(color='green',icon='heart')
#                      ).add_to(map_gyeonggi)
#     else:
#         folium.Marker(location = [row['위도'], row['경도']],
#                       popup=row['병원또는센터명'],
#                     icon=folium.Icon(color='yellow',icon='star')
#                      ).add_to(map_gyeonggi)
