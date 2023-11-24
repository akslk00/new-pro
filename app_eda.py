import numpy as np
import streamlit as st
import pandas as pd

def run_eda_app():
    st.subheader('주택 가격데이터')
    df=pd.read_csv('./data/housing_price_dataset.csv')
    df=df.loc[df['Price']>0,]
    #df=df.sample(n=10000,random_state=1000)
    st.dataframe(df)

    square=df.loc[df['SquareFeet']==2999,]

    squaremin=df.loc[df['SquareFeet'] == 1000,]
    
    prmax=df.loc[df['Price']==492195.2599720151,]

    prmin=df.loc[df['Price']==154.77912007166017,]
    
    bdmax=df.loc[df['Bedrooms']==5,]

    bdmin=df.loc[df['Bedrooms']==2,]

    bsmax=df.loc[df['Bathrooms']==3,]

    bsmin=df.loc[df['Bathrooms']==1,]


    choice = ['평수가 가장 넓은집의 스펙모음','평수가 가장 좁은집의 스펙모음'
              ,'가장 금액이 높은 주택','금액이 가장싼 주택'
              ,'침실이 가장 많은 집 모음','침실이 가장 적은 집 모음'
              ,'화장실이 가장 많은 집 모음','화장실이 가장 적은 집 모음']
    my_choice = st.selectbox('원하는 조건을 선택하시오', choice)

    if my_choice == choice[0] :
        st.text('평수가 가장 넓은집의 스펙모음')
        st.dataframe(square)
    elif my_choice == choice[1] :
        st.text('평수가 가장 좁은집의 스펙모음')
        st.dataframe(squaremin)
    elif my_choice == choice[2]:
        st.text('가장 금액이 높은 주택')
        st.dataframe(prmax)
    elif my_choice == choice[3]:
        st.text('금액이 가장싼 주택')
        st.dataframe(prmin)
    elif my_choice == choice[4]:
        st.text('침실이 가장 많은 집 모음')
        st.dataframe(bdmax)
    elif my_choice == choice[5]:
        st.text('침실이 가장 적은 집 모음')
        st.dataframe(bdmin)
    elif my_choice == choice[6]:
        st.text('화장실이 가장 많은 집 모음')
        st.dataframe(bsmax)
    elif my_choice == choice[7]:
        st.text('화장실이 가장 적은 집 모음')
        st.dataframe(bsmin)




    st.text('조건에 적합한 집 검색')

    SF=st.slider('평방피트',1000, 2999, value=1000)
    Pr=st.slider('가격', 154, 492196,value=154)
    BD=st.slider('침실', 2, 5, value=2)
    BS=st.slider('화장실', 1, 3, value=1)
    sf=df['SquareFeet']<=SF
    pr=df['Price']<=Pr
    bd=df['Bedrooms']<=BD
    bs=df['Bathrooms']<=BS
    ALl=df.loc[((bd&bs)&(sf&pr)),]
    st.dataframe(ALl)
