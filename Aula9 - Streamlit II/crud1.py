import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Sistema CRUD de Usuários",
    page_icon="👥",
    layout="wide"
)

# Título principal
st.title("👥 Sistema CRUD de Usuários com Streamlit")

# Inicializar a lista de usuários na sessão do Streamlit
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = []
if 'proximo_id' not in st.session_state:
    st.session_state.proximo_id = 1

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, email, cidade, telefone):
    usuario = {
        "id": st.session_state.proximo_id,
        "nome": nome, 
        "email": email,
        "cidade": cidade,
        "telefone": telefone
    }
    st.session_state.usuarios.append(usuario)
    st.session_state.proximo_id += 1

# Função para atualizar um usuário
def atualizar_usuario(id, nome, email, cidade, telefone):
    for i, usuario in enumerate(st.session_state.usuarios):
        if usuario['id'] == id:
            st.session_state.usuarios[i] = {
                "id": id,
                "nome": nome,
                "email": email,
                "cidade": cidade,
                "telefone": telefone
            }
            break

# Função para deletar um usuário
def deletar_usuario(id):
    for i, usuario in enumerate(st.session_state.usuarios):
        if usuario['id'] == id:
            st.session_state.usuarios.pop(i)
            break

# Função para buscar usuário por ID
def buscar_usuario_por_id(id):
    for usuario in st.session_state.usuarios:
        if usuario['id'] == id:
            return usuario
    return None

# Criando abas para organizar as funcionalidades
tab1, tab2, tab3 = st.tabs(["📝 Cadastrar", "📋 Listar/Editar", "📊 Estatísticas"])

with tab1:
    # Seção de cadastro
    st.header("📝 Cadastrar Novo Usuário")
    
    with st.form("form_cadastro", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            nome = st.text_input("Nome completo")
            email = st.text_input("E-mail")
        
        with col2:
            cidade = st.text_input("Cidade")
            telefone = st.text_input("Telefone")
        
        submitted = st.form_submit_button("✅ Cadastrar Usuário", use_container_width=True)
        
        if submitted:
            if nome and email and cidade and telefone:
                cadastrar_usuario(nome, email, cidade, telefone)
                st.success(f"✅ Usuário {nome} cadastrado com sucesso! (ID: {st.session_state.proximo_id - 1})")
            else:
                st.error("❌ Por favor, preencha todos os campos.")

with tab2:
    st.header("📋 Lista de Usuários")
    
    # Verifica se há usuários cadastrados
    if st.session_state.usuarios:
        # Barra de busca por ID
        with st.expander("🔍 Buscar Usuário por ID", expanded=False):
            col_busca1, col_busca2 = st.columns([3, 1])
            with col_busca1:
                id_busca = st.number_input("Digite o ID do usuário", min_value=1, step=1)
            with col_busca2:
                buscar_click = st.button("🔍 Buscar", use_container_width=True)
            
            if buscar_click:
                usuario_encontrado = buscar_usuario_por_id(id_busca)
                if usuario_encontrado:
                    st.success(f"✅ Usuário encontrado!")
                    with st.container(border=True):
                        st.markdown(f"### {usuario_encontrado['nome']}")
                        st.markdown(f"**🆔 ID:** {usuario_encontrado['id']}")
                        st.markdown(f"**📧 Email:** {usuario_encontrado['email']}")
                        st.markdown(f"**🏙️ Cidade:** {usuario_encontrado['cidade']}")
                        st.markdown(f"**📞 Telefone:** {usuario_encontrado['telefone']}")
                else:
                    st.error(f"❌ Nenhum usuário encontrado com o ID {id_busca}")
        
        st.divider()
        
        # Opção para limpar a lista
        col1, col2, col3 = st.columns([3, 1, 1])
        with col3:
            if st.button("🗑️ Limpar Lista", use_container_width=True):
                st.session_state.usuarios = []
                st.session_state.proximo_id = 1
                st.rerun()
        
        # Converte a lista de usuários em um DataFrame
        df_usuarios = pd.DataFrame(st.session_state.usuarios)
        
        # Reordena as colunas para colocar o ID primeiro
        df_usuarios = df_usuarios[['id', 'nome', 'email', 'cidade', 'telefone']]
        
        # Exibe o DataFrame na tela com formatação melhorada
        st.dataframe(
            df_usuarios,
            use_container_width=True,
            hide_index=True,
            column_config={
                "id": "ID",
                "nome": "Nome",
                "email": "E-mail",
                "cidade": "Cidade",
                "telefone": "Telefone"
            }
        )
        
        # Mostra estatísticas
        st.info(f"📊 Total de usuários cadastrados: {len(st.session_state.usuarios)}")
        
        st.divider()
        st.subheader("✏️ Editar ou Excluir Usuários")
        
        # Selecionar usuário para edição/exclusão por ID
        ids_usuarios = [usuario['id'] for usuario in st.session_state.usuarios]
        nomes_usuarios = [f"ID {usuario['id']} - {usuario['nome']}" for usuario in st.session_state.usuarios]
        
        usuario_selecionado = st.selectbox(
            "Selecione um usuário para editar/excluir:",
            options=ids_usuarios,
            format_func=lambda x: f"ID {x} - {buscar_usuario_por_id(x)['nome']}"
        )
        
        if usuario_selecionado:
            usuario = buscar_usuario_por_id(usuario_selecionado)
            
            if usuario:
                # Formulário de edição
                with st.form("form_edicao"):
                    st.write(f"**Editando:** {usuario['nome']} (ID: {usuario['id']})")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        novo_nome = st.text_input("Nome", value=usuario['nome'])
                        novo_email = st.text_input("E-mail", value=usuario['email'])
                    
                    with col2:
                        nova_cidade = st.text_input("Cidade", value=usuario['cidade'])
                        novo_telefone = st.text_input("Telefone", value=usuario['telefone'])
                    
                    col_edit, col_delete = st.columns(2)
                    
                    with col_edit:
                        edit_submitted = st.form_submit_button("💾 Atualizar Usuário", use_container_width=True)
                    
                    with col_delete:
                        delete_submitted = st.form_submit_button("🗑️ Excluir Usuário", use_container_width=True)
                    
                    if edit_submitted:
                        if novo_nome and novo_email and nova_cidade and novo_telefone:
                            atualizar_usuario(usuario['id'], novo_nome, novo_email, nova_cidade, novo_telefone)
                            st.success(f"✅ Usuário atualizado com sucesso!")
                            st.rerun()
                        else:
                            st.error("❌ Por favor, preencha todos os campos.")
                    
                    if delete_submitted:
                        deletar_usuario(usuario['id'])
                        st.success(f"✅ Usuário excluído com sucesso!")
                        st.rerun()
        
        # Visualização alternativa em cards
        with st.expander("👁️ Visualização em Cards"):
            st.subheader("Cards de Usuários")
            
            # Criar linhas com 3 cards cada
            cols = st.columns(3)
            for i, usuario in enumerate(st.session_state.usuarios):
                with cols[i % 3]:
                    with st.container(border=True):
                        st.markdown(f"### {usuario['nome']}")
                        st.markdown(f"**🆔 ID:** {usuario['id']}")
                        st.markdown(f"**📧 Email:** {usuario['email']}")
                        st.markdown(f"**🏙️ Cidade:** {usuario['cidade']}")
                        st.markdown(f"**📞 Telefone:** {usuario['telefone']}")
                        
                        # Botão para deletar diretamente do card
                        if st.button(f"🗑️ Excluir", key=f"del_card_{usuario['id']}"):
                            deletar_usuario(usuario['id'])
                            st.rerun()
    else:
        st.warning("⚠️ Nenhum usuário cadastrado ainda.")
        st.info("👆 Utilize a aba 'Cadastrar' para adicionar novos usuários.")

with tab3:
    st.header("📊 Estatísticas do Sistema")
    
    if st.session_state.usuarios:
        df_stats = pd.DataFrame(st.session_state.usuarios)
        
        # Métricas principais
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total de Usuários", len(df_stats))
        with col2:
            st.metric("Cidades Únicas", df_stats['cidade'].nunique())
        with col3:
            st.metric("Emails Únicos", df_stats['email'].nunique())
        with col4:
            st.metric("Último ID", df_stats['id'].max())
        
        st.divider()
        
        # Distribuição por cidade
        st.subheader("🏙️ Distribuição por Cidade")
        cidade_counts = df_stats['cidade'].value_counts().reset_index()
        cidade_counts.columns = ['Cidade', 'Quantidade']
        st.bar_chart(cidade_counts.set_index('Cidade'))
        
        # Tabela de distribuição
        with st.expander("📋 Ver tabela de distribuição"):
            st.dataframe(cidade_counts, use_container_width=True, hide_index=True)
        
        st.divider()
        
        # Lista completa em formato de tabela
        st.subheader("📋 Dados Completos")
        st.dataframe(
            df_stats[['id', 'nome', 'email', 'cidade', 'telefone']],
            use_container_width=True,
            hide_index=True
        )
        
        # Download dos dados
        csv = df_stats.to_csv(index=False)
        st.download_button(
            label="📥 Download dos Dados (CSV)",
            data=csv,
            file_name="usuarios.csv",
            mime="text/csv",
            use_container_width=True
        )
    else:
        st.warning("⚠️ Nenhum usuário cadastrado ainda.")
        st.info("👆 Cadastre usuários na aba 'Cadastrar' para ver as estatísticas!")
        
        # Gráfico ilustrativo vazio
        st.subheader("🏙️ Distribuição por Cidade")
        st.info("📊 Gráfico aparecerá quando houver usuários cadastrados")
        
        st.divider()
        
        st.subheader("📋 Dados Completos")
        st.info("📋 Tabela aparecerá quando houver usuários cadastrados")

# Rodapé
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col2:
    st.caption("📱 Sistema CRUD completo com busca por ID - Desenvolvido com Streamlit")