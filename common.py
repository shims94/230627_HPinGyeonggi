import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def get_dataset():
    data = pd.read_csv("응급의료기관및응급의료지원센터현황.csv")
    df = df.rename(columns={'병원명/센터명': '병원또는센터명'})

    # 응급의료지원센터여부	전문응급의료센터여부
    # 전문응급센터전문분야	권역외상센터여부	지역외상센터여부의 NaN을 fillna()함수로 0으로 채워줌
    df['응급의료지원센터여부'] = df['응급의료지원센터여부'].fillna('0')
    df['전문응급의료센터여부'] = df['전문응급의료센터여부'].fillna('0')
    df['전문응급센터전문분야'] = df['전문응급센터전문분야'].fillna('0')
    df['권역외상센터여부'] = df['권역외상센터여부'].fillna('0')
    df['지역외상센터여부'] = df['지역외상센터여부'].fillna('0')
    return data

def page_config():
    st.set_page_config(
        page_title="HealthPoint Locator in Gyeonggi",
        page_icon="🏥",
    )