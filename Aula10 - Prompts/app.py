# app.py
import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os
from typing import List, Dict

# Configuração da página
st.set_page_config(
    page_title="Controle de Registros",
    page_icon="📝",
    layout="wide"
)

class GerenciadorRegistros:
    """Classe para gerenciar os registros"""
    
    def __init__(self):
        self.arquivo_dados = "registros.json"
        self.registros = self.carregar_registros()
    
    def carregar_registros(self) -> List[Dict]:
        """Carrega registros do arquivo JSON"""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def salvar_registros(self):
        """Salva registros no arquivo JSON"""
        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            json.dump(self.registros, f, ensure_ascii=False, indent=2)
    
    def adicionar_registro(self, nome: str, descricao: str, valor: float) -> bool:
        """Adiciona um novo registro"""
        if not nome or not descricao:
            st.error("Nome e descrição são obrigatórios!")
            return False
        
        if valor <= 0:
            st.error("Valor deve ser maior que zero!")
            return False
        
        registro = {
            "id": len(self.registros) + 1,
            "nome": nome.strip(),
            "descricao": descricao.strip(),
            "valor": round(valor, 2),
            "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "timestamp": datetime.now().isoformat()
        }
        
        self.registros.append(registro)
        self.salvar_registros()
        return True
    
    def listar_registros(self) -> pd.DataFrame:
        """Retorna registros como DataFrame"""
        if not self.registros:
            return pd.DataFrame()
        
        df = pd.DataFrame(self.registros)
        # Remove a coluna timestamp para exibição
        df_exibicao = df.drop(columns=['timestamp'], errors='ignore')
        return df_exibicao
    
    def remover_registro(self, registro_id: int) -> bool:
        """Remove um registro pelo ID"""
        for i, registro in enumerate(self.registros):
            if registro['id'] == registro_id:
                self.registros.pop(i)
                self.salvar_registros()
                return True
        return False
    
    def get_estatisticas(self) -> Dict:
        """Retorna estatísticas dos registros"""
        if not self.registros:
            return {
                "total": 0,
                "total_valor": 0,
                "media_valor": 0,
                "maior_valor": 0,
                "menor_valor": 0
            }
        
        valores = [r['valor'] for r in self.registros]
        return {
            "total": len(self.registros),
            "total_valor": sum(valores),
            "media_valor": sum(valores) / len(valores),
            "maior_valor": max(valores),
            "menor_valor": min(valores)
        }

def main():
    # Inicializa o gerenciador
    if 'gerenciador' not in st.session_state:
        st.session_state.gerenciador = GerenciadorRegistros()
    
    gerenciador = st.session_state.gerenciador
    
    # Título
    st.title("📝 Controle de Registros")
    st.markdown("---")
    
    # Layout com colunas
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("📌 Novo Registro")
        
        with st.form(key="registro_form"):
            nome = st.text_input("Nome *", placeholder="Digite o nome")
            descricao = st.text_area("Descrição *", placeholder="Digite a descrição")
            valor = st.number_input("Valor * (R$)", min_value=0.01, step=0.01, format="%.2f")
            
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                submitted = st.form_submit_button("✅ Registrar", width='stretch')  # Form submit button usa use_container_width
            with col_btn2:
                limpar = st.form_submit_button("🗑️ Limpar", width='stretch')  # Form submit button usa use_container_width
            
            if submitted:
                if gerenciador.adicionar_registro(nome, descricao, valor):
                    st.success("✅ Registro adicionado com sucesso!")
                    st.rerun()
    
    with col2:
        # Estatísticas
        st.subheader("📊 Estatísticas")
        stats = gerenciador.get_estatisticas()
        
        col_stats1, col_stats2, col_stats3 = st.columns(3)
        with col_stats1:
            st.metric("Total de Registros", stats['total'])
        with col_stats2:
            st.metric("Valor Total", f"R$ {stats['total_valor']:,.2f}")
        with col_stats3:
            st.metric("Valor Médio", f"R$ {stats['media_valor']:,.2f}")
        
        col_stats4, col_stats5 = st.columns(2)
        with col_stats4:
            st.metric("Maior Valor", f"R$ {stats['maior_valor']:,.2f}")
        with col_stats5:
            st.metric("Menor Valor", f"R$ {stats['menor_valor']:,.2f}")
    
    st.markdown("---")
    
    # Listagem de registros
    st.subheader("📋 Lista de Registros")
    
    df = gerenciador.listar_registros()
    
    if not df.empty:
        # Filtros
        col_filtro1, col_filtro2, col_filtro3 = st.columns(3)
        with col_filtro1:
            buscar = st.text_input("🔍 Buscar por nome", placeholder="Digite para filtrar...")
        with col_filtro2:
            ordenar = st.selectbox("Ordenar por", ["Data (mais recente)", "Data (mais antiga)", "Valor (maior)", "Valor (menor)", "Nome (A-Z)"])
        with col_filtro3:
            valor_min = st.number_input("Valor mínimo (R$)", min_value=0.0, value=0.0, step=0.01)
        
        # Aplicar filtros
        df_filtrado = df.copy()
        
        if buscar:
            df_filtrado = df_filtrado[df_filtrado['nome'].str.contains(buscar, case=False, na=False)]
        
        if valor_min > 0:
            df_filtrado = df_filtrado[df_filtrado['valor'] >= valor_min]
        
        # Aplicar ordenação
        if ordenar == "Data (mais recente)":
            df_filtrado = df_filtrado.sort_values('data_hora', ascending=False)
        elif ordenar == "Data (mais antiga)":
            df_filtrado = df_filtrado.sort_values('data_hora', ascending=True)
        elif ordenar == "Valor (maior)":
            df_filtrado = df_filtrado.sort_values('valor', ascending=False)
        elif ordenar == "Valor (menor)":
            df_filtrado = df_filtrado.sort_values('valor', ascending=True)
        elif ordenar == "Nome (A-Z)":
            df_filtrado = df_filtrado.sort_values('nome')
        
        # Exibir registros
        st.dataframe(
            df_filtrado,
            width='stretch',  # DataFrame também usa use_container_width
            hide_index=True,
            column_config={
                "id": "ID",
                "nome": "Nome",
                "descricao": "Descrição",
                "valor": st.column_config.NumberColumn("Valor (R$)", format="R$ %.2f"),
                "data_hora": "Data/Hora"
            }
        )
        
        # Botões de ação em massa
        col_acoes1, col_acoes2, col_acoes3 = st.columns(3)
        with col_acoes1:
            if st.button("🗑️ Limpar todos os registros", width='stretch'):  # Button usa use_container_width
                if st.session_state.get('confirmar_limpeza', False):
                    gerenciador.registros = []
                    gerenciador.salvar_registros()
                    st.success("Todos os registros foram removidos!")
                    st.session_state.confirmar_limpeza = False
                    st.rerun()
                else:
                    st.session_state.confirmar_limpeza = True
                    st.warning("⚠️ Clique novamente para confirmar a exclusão de todos os registros!")
        
        # Exportar dados
        with col_acoes2:
            csv = df.to_csv(index=False, encoding='utf-8-sig')
            st.download_button(
                label="📥 Exportar CSV",
                data=csv,
                file_name=f"registros_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                width='stretch'  # Download button usa use_container_width
            )
        
        # Exibir total de registros filtrados
        st.caption(f"📊 Mostrando {len(df_filtrado)} de {len(df)} registros")
        
    else:
        st.info("ℹ️ Nenhum registro encontrado. Adicione seu primeiro registro!")

if __name__ == "__main__":
    main()