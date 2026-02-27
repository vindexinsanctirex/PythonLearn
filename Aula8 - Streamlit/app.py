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
    if nova_tarefa.strip():
        st.session_state.tarefas.append({"nome": nova_tarefa.strip(), "id": len(st.session_state.tarefas) + len(st.session_state.tarefas_concluidas)})
        st.success(f"✅ Tarefa '{nova_tarefa}' adicionada!")
        st.rerun()
    else:
        st.error("❌ Por favor, digite uma tarefa antes de adicionar.")

st.divider()

# Exibir tarefas pendentes
st.subheader("📋 Tarefas Pendentes")
if st.session_state.tarefas:
    # Criar uma lista para armazenar tarefas a serem removidas
    tarefas_para_concluir = []
    
    for i, tarefa in enumerate(st.session_state.tarefas):
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            # Usar um ID único baseado no índice e no nome
            checkbox_key = f"pendente_{i}_{tarefa['nome']}"
            if st.checkbox(" ", key=checkbox_key):
                tarefas_para_concluir.append(i)
        with col2:
            st.write(tarefa['nome'])
    
    # Processar tarefas marcadas para conclusão (fora do loop)
    if tarefas_para_concluir:
        for i in reversed(tarefas_para_concluir):  # Reverso para não afetar índices
            tarefa_concluida = st.session_state.tarefas.pop(i)
            st.session_state.tarefas_concluidas.append(tarefa_concluida)
        st.rerun()
else:
    st.info("Nenhuma tarefa pendente no momento.")

st.divider()

# Exibir tarefas concluídas
st.subheader("✅ Tarefas Concluídas")
if st.session_state.tarefas_concluidas:
    # Criar uma lista para armazenar tarefas a serem revertidas
    tarefas_para_reverter = []
    
    for i, tarefa in enumerate(st.session_state.tarefas_concluidas):
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        with col1:
            st.write("✓")
        with col2:
            st.write(f"~~{tarefa['nome']}~~")
        with col3:
            # Botão único para reverter cada tarefa
            if st.button("↩️", key=f"reverter_{i}_{tarefa['nome']}"):
                tarefas_para_reverter.append(i)
    
    # Processar tarefas marcadas para reverter (fora do loop)
    if tarefas_para_reverter:
        for i in reversed(tarefas_para_reverter):
            tarefa_revertida = st.session_state.tarefas_concluidas.pop(i)
            st.session_state.tarefas.append(tarefa_revertida)
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

# Instruções
st.sidebar.divider()
st.sidebar.info(
    "✅ **Como usar:**\n"
    "1. Digite uma tarefa\n"
    "2. Clique em 'Adicionar Tarefa'\n"
    "3. Marque o checkbox para concluir\n"
    "4. Use ↩️ para reverter tarefas concluídas"
)