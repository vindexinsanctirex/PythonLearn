import streamlit as st
import pandas as pd

# Inicializar a lista de usuários na sessão do Streamlit
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = []

# Título principal
st.title("Sistema de Cadastro de Usuários")

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, email):
    usuario = {"nome": nome, "email": email}
    st.session_state.usuarios.append(usuario)

# Seção de cadastro
st.header("📝 Cadastrar Novo Usuário")
with st.form("form_cadastro"):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    
    submitted = st.form_submit_button("Cadastrar")
    if submitted:
        if nome and email:
            cadastrar_usuario(nome, email)
            st.success("✅ Usuário cadastrado com sucesso!")
            st.rerun()  # Atualiza a página para mostrar o novo usuário
        else:
            st.error("❌ Por favor, preencha todos os campos.")

# Seção de lista de usuários
st.header("👥 Lista de Usuários")

# Verifica se há usuários cadastrados
if st.session_state.usuarios:
    # Converte a lista de usuários em um DataFrame
    df_usuarios = pd.DataFrame(st.session_state.usuarios)
    
    # Exibe o DataFrame na tela com formatação melhorada
    st.dataframe(
        df_usuarios,
        use_container_width=True,
        hide_index=True,
        column_config={
            "nome": "Nome",
            "email": "E-mail"
        }
    )
    
    # Mostra estatísticas
    st.info(f"Total de usuários cadastrados: {len(st.session_state.usuarios)}")
    
    # Opção para limpar a lista (opcional)
    if st.button("🗑️ Limpar Lista"):
        st.session_state.usuarios = []
        st.rerun()
        
else:
    st.warning("⚠️ Nenhum usuário cadastrado ainda.")
    st.info("👆 Utilize o formulário acima para cadastrar novos usuários.")

# Rodapé (opcional)
st.markdown("---")
st.caption("Sistema de CRUD simples desenvolvido com Streamlit")