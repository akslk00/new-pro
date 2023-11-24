import math
import numpy as np
import streamlit as st
import joblib
from sklearn.linear_model import LinearRegression

def run_ml_app():
    st.subheader('견적 보기')
    regressor = joblib.load('./model/Aregressor.pkl')
    SquareFeet = st.number_input('면적 입력',1000,2999)
    Bedrooms=st.number_input('침실수 입력',2,5)
    Bathrooms=st.number_input('화장실수 입력',1,3)
    YearBuil=st.number_input('연식 입력',1950,2021)

    if st.button('구매 예산금액'):
        new_data =np.array([SquareFeet,Bedrooms,Bathrooms,YearBuil])
        new_data = new_data.reshape(1,4)
        y_pred=regressor.predict(new_data)
        price=y_pred[0]
        if price<=154:
            st.text('자동차를 구매하기 어렵습니다')
        else:
            st.text('이 고객은 {}금액정도면 구매 가능 합니다'.format(math.ceil(price)))
        st.text(y_pred)

    else:
        st.text('')