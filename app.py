import pandas as pd
import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app

def main():
    st.title('주택 가격을 예측해보자')

    menu = ['Home','주택 가격비교','ML']

    choice=st.sidebar.selectbox('메뉴',menu)
    
    if choice == menu[0]:
        run_home_app()
            
    elif choice == menu[1]:
        run_eda_app()
        
    elif choice == menu[2]:
        pass
 

if __name__ == '__main__':
    main()