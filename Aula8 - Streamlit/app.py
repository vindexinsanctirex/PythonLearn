import streamlit as st

# Inicializar a lista de tarefas na sessão para persistir entre execuções
if 'tarefas' not in st.session_state:
    st.session_state.tarefas = []
if 'tarefas_concluidas' not in st.session_state:
    st.session_state.tarefas_concluidas = []

st.title("📝 Lista de Tarefas com Checkboxes")

# Entrada de nova tarefa
nova_tarefa = st.text_input("Digite uma nova tarefa", key="nova_tarefa_input")

# Botão para adicionar tarefa
if st.button("➕ Adicionar Tarefa"):
    if nova_tarefa.strip():  # Verifica se não está vazio ou só espaços
        st.session_state.tarefas.append(nova_tarefa.strip())
        st.success(f"✅ Tarefa '{nova_tarefa}' adicionada!")
        st.rerun()  # Recarrega a aplicação para limpar o input
    else:
        st.error("❌ Por favor, digite uma tarefa antes de adicionar.")

# Separador visual
st.divider()

# Exibir tarefas pendentes
st.subheader("📋 Tarefas Pendentes")
if st.session_state.tarefas:
    for i, tarefa in enumerate(st.session_state.tarefas):
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            # Checkbox para marcar como concluída
            if st.checkbox(" ", key=f"check_{i}"):
                st.session_state.tarefas_concluidas.append(tarefa)
                st.session_state.tarefas.pop(i)
                st.rerun()
        with col2:
            st.write(tarefa)
else:
    st.info("Nenhuma tarefa pendente no momento.")

# Separador visual
st.divider()

# Exibir tarefas concluídas
st.subheader("✅ Tarefas Concluídas")
if st.session_state.tarefas_concluidas:
    for i, tarefa in enumerate(st.session_state.tarefas_concluidas):
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        with col1:
            st.write("✓")
        with col2:
            st.write(f"~~{tarefa}~~")  # Texto riscado
        with col3:
            # Botão para reverter (mover de volta para pendentes)
            if st.button("↩️", key=f"reverter_{i}"):
                st.session_state.tarefas.append(tarefa)
                st.session_state.tarefas_concluidas.pop(i)
                st.rerun()
    
    # Botão para limpar todas as concluídas
    if st.button("🗑️ Limpar Concluídas"):
        st.session_state.tarefas_concluidas = []
        st.rerun()
else:
    st.info("Nenhuma tarefa concluída ainda.")

# Mostrar estatísticas
st.sidebar.header("📊 Estatísticas")
st.sidebar.metric("Total de Tarefas", 
                  len(st.session_state.tarefas) + len(st.session_state.tarefas_concluidas))
st.sidebar.metric("Pendentes", len(st.session_state.tarefas))
st.sidebar.metric("Concluídas", len(st.session_state.tarefas_concluidas))