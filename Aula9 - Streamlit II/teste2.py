# streamlit usando sidebar.radio e selectbox para criar um sistema academico

import streamlit as st

st.title('Sistema Acadêmico')

option = st.sidebar.radio('Escolha uma opção:', ['Início', 'Cadastro', 'Relatório'])

if option == 'Início':
    st.header('Bem-vindo ao Sistema Acadêmico')
    st.write('Selecione uma opção no menu lateral para começar.')
    
elif option == 'Cadastro': # deve mostrar informações dos alunos e ter uma selectbox chamada "selecione curso" com opções GTI ADS, Redes e Ciencia da Computação, que apareça uma mensagem mostrando qual curso foi escolhido.
    st.header('Cadastro de Alunos')
    st.write('Preencha as informações dos alunos abaixo.')
    
    nome = st.text_input('Nome do Aluno')
    
    curso = st.selectbox('Selecione o curso:', ['GTI', 'ADS', 'Redes', 'Ciência da Computação'])
    
    if st.button('Cadastrar'):
        st.success(f'Aluno {nome} cadastrado com sucesso no curso {curso}!')
elif option == 'Relatório':
    st.header('Relatório de Alunos')
    st.write('Aqui você pode visualizar o relatório dos alunos cadastrados.')
    # Aqui você pode adicionar código para mostrar o relatório dos alunos cadastrados, por exemplo, usando uma tabela ou gráfico.