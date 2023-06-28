import streamlit as st
from streamlit_folium import st_folium
import folium
import common

# 응급센터가 존재하는지 체크하는 함수
def check_option(row) :
    if row['응급의료지원센터여부'] == 'Y': return '<b>응급의료지원센터</b>'
    elif row['전문응급의료센터여부'] == 'Y': return '<b>전문응급의료센터</b>'
    elif row['전문응급센터전문분야'] == 'Y': return '<b>전문응급센터전문분야</b>'
    elif row['권역외상센터여부'] == 'Y': return '<b>권역외상센터</b>'
    elif row['지역외상센터여부'] == 'Y': return '<b>지역외상센터</b>'

common.page_config()

st.title("Map Visualization")
st.text("지역급 의료시설은 초록색하트마커로, 권역급 의료시설은 빨간색별마커로 표시")

df = common.get_data()
# 초기 맵
map_gyeonggi = folium.Map(location=[37.291887, 126.996340], zoom_start=10)


#업무 구분명이 지역센터나 기관일경우 녹색 하트마커, 그이외(광역) 빨강 스타마커
for index, row in df.iterrows():
    tip = check_option(row)
    if row['업무구분명'] == '지역센터' or row['업무구분명'] == '지역기관':
        if tip != '':
            folium.Marker(location=[row['위도'], row['경도']],
                          popup=row['병원명/센터명'],
                          tooltip=tip,
                          icon=folium.Icon(color='green', icon='heart')
                          ).add_to(map_gyeonggi)
        else:
            folium.Marker(location = [row['위도'], row['경도']],
                          popup=row['병원명/센터명'],
                          icon=folium.Icon(color='green',icon='heart')
                         ).add_to(map_gyeonggi)
    else:
        if tip != '':
            folium.Marker(location=[row['위도'], row['경도']],
                          popup=row['병원명/센터명'],
                          tooltip=tip,
                          icon=folium.Icon(color='yellow', icon='star')
                          ).add_to(map_gyeonggi)
        else :
            folium.Marker(location = [row['위도'], row['경도']],
                      popup=row['병원명/센터명'],
                    icon=folium.Icon(color='yellow',icon='star')
                     ).add_to(map_gyeonggi)

st_folium(map_gyeonggi)