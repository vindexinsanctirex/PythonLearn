# teste.py
import sys
from app import GerenciadorRegistros

def testar_sistema():
    """Testa as funcionalidades do sistema"""
    print("=" * 50)
    print("TESTE DO SISTEMA DE CONTROLE DE REGISTROS")
    print("=" * 50)
    
    # Inicializa o gerenciador
    gerenciador = GerenciadorRegistros()
    
    # Limpa registros existentes para teste
    gerenciador.registros = []
    
    print("\n✅ Teste 1: Adicionando registros...")
    
    # Adiciona registros de teste
    registros_teste = [
        ("Notebook Dell", "Notebook para desenvolvimento", 3500.00),
        ("Mouse Logitech", "Mouse sem fio", 150.50),
        ("Teclado Mecânico", "Teclado RGB", 299.90),
        ("Monitor 27\"", "Monitor 4K", 1800.00),
        ("Cadeira Gamer", "Cadeira ergonômica", 1200.00)
    ]
    
    for nome, desc, valor in registros_teste:
        sucesso = gerenciador.adicionar_registro(nome, desc, valor)
        if sucesso:
            print(f"  ✓ Registro adicionado: {nome} - R$ {valor:.2f}")
        else:
            print(f"  ✗ Erro ao adicionar: {nome}")
    
    print("\n✅ Teste 2: Listando registros...")
    df = gerenciador.listar_registros()
    
    if not df.empty:
        print(f"\nTotal de registros: {len(df)}")
        print("\nLista de registros:")
        print("-" * 80)
        
        for idx, row in df.iterrows():
            print(f"ID: {row['id']} | Nome: {row['nome']} | Valor: R$ {row['valor']:.2f} | Data: {row['data_hora']}")
            print(f"     Descrição: {row['descricao']}")
            print("-" * 80)
    else:
        print("Nenhum registro encontrado!")
    
    print("\n✅ Teste 3: Verificando estatísticas...")
    stats = gerenciador.get_estatisticas()
    print(f"  Total de registros: {stats['total']}")
    print(f"  Valor total: R$ {stats['total_valor']:.2f}")
    print(f"  Valor médio: R$ {stats['media_valor']:.2f}")
    print(f"  Maior valor: R$ {stats['maior_valor']:.2f}")
    print(f"  Menor valor: R$ {stats['menor_valor']:.2f}")
    
    print("\n✅ Teste 4: Removendo um registro...")
    if not df.empty:
        primeiro_id = df.iloc[0]['id']
        sucesso = gerenciador.remover_registro(primeiro_id)
        if sucesso:
            print(f"  ✓ Registro ID {primeiro_id} removido com sucesso!")
            
            # Verifica se foi removido
            df_atualizado = gerenciador.listar_registros()
            print(f"  Novo total de registros: {len(df_atualizado)}")
        else:
            print(f"  ✗ Erro ao remover registro ID {primeiro_id}")
    
    print("\n✅ Teste 5: Salvando e carregando dados...")
    gerenciador.salvar_registros()
    print("  ✓ Dados salvos em registros.json")
    
    # Carrega novamente para verificar persistência
    novo_gerenciador = GerenciadorRegistros()
    df_carregado = novo_gerenciador.listar_registros()
    print(f"  ✓ Dados carregados: {len(df_carregado)} registros")
    
    print("\n" + "=" * 50)
    print("✅ TESTE CONCLUÍDO COM SUCESSO!")
    print("=" * 50)

if __name__ == "__main__":
    testar_sistema()