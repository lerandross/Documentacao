import streamlit as st
import streamlit_authenticator as stauth
from content import documentacao

import yaml
from yaml.loader import SafeLoader

#hashed_passwords = stauth.Hasher(['azul#123', 'Q2+/-42!=15^`#|?']).generate()
#print(hashed_passwords)




with open('conf/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login('Login')

if st.session_state["authentication_status"]:
    #authenticator.logout('logout', location='sidebar')
    documentacao.main()
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')