import pandas as pd
import streamlit as st

def main():
    st.title('항공편 가격을 예측해보자')
    df=pd.read_csv('./data/Data_Train.csv')
    st.dataframe(df)

if __name__ == '__main__':
    main()