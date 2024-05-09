import os

# Pasta principal onde todos os diretórios serão criados
pasta_principal = "Relatorios"

# Dicionário com as categorias e os nomes dos relatórios
categorias = {
    "Medio": [
        "EM.EF02 - Quadro de Recuperação (Médio)",
        "EM.EF01 - Relatório sobre Alunos",
        "EM.EP01 - Análise de Provas Testes",
        "EM.EP02 - Análise de Resultados (Correção Digital)",
        "EM.EP03 - Controle de Instrumentos Avaliativos",
        "EM.EP04 - Escolhas de Eletivas",
        "EM - ENEM"
    ],
    "Parcial": [
        "EF.Par.EF02 - Quadro de Recuperação (Fundamental Parcial)",
        "EF.Par.EF01 - Relatório sobre Alunos",
        "EF.Par.EF01.prof - Relatório sobre Alunos",
        "EF.Par.EP03 - Controle de Instrumentos Avaliativos",
        "Inscrições- Extracurriculares e Treinamentos Esportivos (Parcial)"  # substituído ':' por '-'
    ],
    "Integral": [
        "EF.Int.EF02 - Quadro de Recuperação (Fundamental Integral)",
        "EF.Int.EF01 - Relatório sobre Alunos",
        "EF.Int.EF01.prof - Relatório sobre Alunos",
        "EF.Int.EP03 - Controle de Instrumentos Avaliativos",
        "Inscrições- Extracurriculares e Treinamentos Esportivos (Integral)"  # substituído ':' por '-'
    ],
    "Especificos": [
        "Acompanhamento de Matriz Curricular",
        "Relatório Pesquisa de Procura",
        "Pesquisa de Clima - 2023 (2024)",
        "Pesquisa Satisfação - 2023",
        "Financeiro",
        "Logs de Replicação",
        "Origem de Inscrições",
        "Ranking de Alunos",
        "Evasão EM",
        "Pesquisa Étnico Racial",
        "Percepção de Operações"
    ]
}

# Criar a pasta principal se não existir
caminho_pasta_principal = os.path.join(os.getcwd(), pasta_principal)
os.makedirs(caminho_pasta_principal, exist_ok=True)

# Criar subdiretórios para cada categoria e relatório
for categoria, relatorios in categorias.items():
    caminho_categoria = os.path.join(caminho_pasta_principal, categoria)
    os.makedirs(caminho_categoria, exist_ok=True)  # Criar diretório da categoria
    for relatorio in relatorios:
        # Substituição segura de caracteres não permitidos
        relatorio_seguro = relatorio.replace(":", "-").replace("/", "-").replace("\\", "-").replace("|", "-")
        caminho_relatorio = os.path.join(caminho_categoria, relatorio_seguro)
        os.makedirs(caminho_relatorio, exist_ok=True)  # Criar diretório para cada relatório
        print(f"Diretório criado: {caminho_relatorio}")
