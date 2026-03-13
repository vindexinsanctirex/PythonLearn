import streamlit as st

st.title('📋 CRUD de Usuários com Streamlit')

# Inicializa a lista de usuários no session_state
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = []

# Cria um formulário para os campos de entrada
with st.form(key='form_usuario', clear_on_submit=True):
    st.subheader("➕ Adicionar Novo Usário")
    
    nome = st.text_input('Nome')
    email = st.text_input('Email')
    cidade = st.text_input('Cidade')
    telefone = st.text_input('Telefone')
    
    # Botão de submit dentro do formulário
    submitted = st.form_submit_button('Adicionar Usuário')
    
    # Processa quando o botão for clicado
    if submitted:
        if nome and email and cidade and telefone:  # Verifica se todos os campos foram preenchidos
            usuario = {
                'nome': nome,
                'email': email,
                'cidade': cidade,
                'telefone': telefone
            }
            st.session_state.usuarios.append(usuario)
            st.success(f'✅ Usuário {nome} adicionado com sucesso!')
            # Os campos serão automaticamente limpos graças ao clear_on_submit=True
        else:
            st.error('❌ Por favor, preencha todos os campos para adicionar um usuário.')

# Seção para exibir a lista de usuários
if st.session_state.usuarios:
    st.divider()
    st.header('📋 Lista de Usuários Cadastrados')
    
    # Exibe os usuários em uma tabela mais organizada
    for i, usuario in enumerate(st.session_state.usuarios, 1):
        with st.container():
            # CORREÇÃO: Agora temos 5 colunas para 5 proporções [1, 2, 2, 2, 2]
            col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 2])
            with col1:
                st.write(f"**#{i}**")
            with col2:
                st.write(f"**Nome:** {usuario['nome']}")
            with col3:
                st.write(f"**Email:** {usuario['email']}")
            with col4:
                st.write(f"**Cidade:** {usuario['cidade']}")
            with col5:
                st.write(f"**Telefone:** {usuario['telefone']}")
            st.divider()
else:
    st.info('📭 Nenhum usuário cadastrado ainda. Adicione um usuário acima!')