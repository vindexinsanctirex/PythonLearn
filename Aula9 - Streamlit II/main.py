# streamlit com columns e expander
import streamlit as st

st.title('Streamlit com Columns e Expander')

col1, col2, col3 = st.columns(3)

with col1:
    st.header('Coluna 1')
    st.write('Conteúdo da coluna 1')
    
with col2:
    st.header('Coluna 2')
    st.write('Conteúdo da coluna 2')
    
with col3:
    st.header('Coluna 3')
    st.write('Conteúdo da coluna 3')
    
with st.expander('Clique para expandir'):
    st.write('Conteúdo dentro do expander')
    st.write('Mais conteúdo dentro do expander')