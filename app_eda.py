import numpy as np
import streamlit as st
import pandas as pd

def run_eda_app():
    st.subheader('주택 가격데이터')
    df=pd.read_csv('./data/housing_price_dataset.csv')
    df=df.sample(n=10000,random_state=1000)
    df=df.loc[df['Price']>0,]
    st.dataframe(df)

    st.text('평수가 가장 넓은집의 스펙모음')
    square=df.loc[df['SquareFeet']==2999,'Bedrooms':'Price']
    st.dataframe(square)


    st.text('평수가 가장 좁은집의 스펙모음')
    squaremin=df.loc[df['SquareFeet']==1000,'Bedrooms':'Price']
    st.dataframe(squaremin)

    
    st.text('가장 금액이 높은 주택')
    prmax=df.loc[df['Price']==492195.2599720151,]
    st.dataframe(prmax)

    
    st.text('금액이 가장싼 주택')
    prmin=df.loc[df['Price']==154.77912007166017,]
    st.dataframe(prmin)

    
    st.text('침실이 가장 많은 집 모음')
    bdmax=df.loc[df['Bedrooms']==5,]
    st.dataframe(bdmax)

    
    st.text('침실이 가장 적은 집 모음')
    bdmin=df.loc[df['Bedrooms']==2,]
    st.dataframe(bdmin)

    st.text('화장실이 가장 많은 집 모음')
    bsmax=df.loc[df['Bathrooms']==3,]
    st.dataframe(bsmax)

    st.text('화장실이 가장 적은 집 모음')
    bsmin=df.loc[df['Bathrooms']==1,]
    st.dataframe(bsmin)

    st.text('조건에 적합한 집 검색')

    SF=st.slider('평방피트',1000, 2999, value=1000)
    Pr=st.slider('가격', 154, 492196,value=154)
    BD=st.slider('침실', 2, 5, value=2)
    BS=st.slider('화장실', 1, 3, value=1)
    sf=df.loc[df['SquareFeet']>=SF,]
    pr=df.loc[df['Price']>=Pr,]
    bd=df['Bedrooms']>=BD
    bs=df['Bathrooms']>=BS
    sfpr=df.loc[df[sf & pr],]
    
    st.dataframe(sfpr)
    
    
