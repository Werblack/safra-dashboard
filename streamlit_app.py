#!/usr/bin/env python3
"""
Aplicação principal do Streamlit para deploy no Streamlit.io
Sistema Safra - Dashboard de Monitoramento
"""

import streamlit as st
import sys
import os
from pathlib import Path
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Adicionar o diretório do projeto ao path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Configuração da página
st.set_page_config(
    page_title="Sistema Safra - Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Verificar se estamos no ambiente Streamlit.io
def is_streamlit_cloud():
    """Verifica se está rodando no Streamlit Cloud"""
    return os.environ.get('STREAMLIT_SERVER_RUN_ON_SAVE', 'false').lower() == 'true'

# Função para criar diretórios necessários
def criar_diretorios_necessarios():
    """Cria diretórios necessários se não existirem"""
    diretorios = [
        'data/input',
        'data/processed', 
        'data/backup',
        'logs'
    ]
    
    for dir_path in diretorios:
        Path(dir_path).mkdir(parents=True, exist_ok=True)

# Função para verificar e criar arquivo de dados de exemplo
def verificar_arquivo_dados():
    """Verifica se existe arquivo de dados e cria exemplo se necessário"""
    arquivo_dados = Path('data/input/Relatorio_Diario.xlsx')
    
    if not arquivo_dados.exists():
        try:
            import pandas as pd
            from datetime import datetime, timedelta
            
            # Criar dados de exemplo
            dados_exemplo = pd.DataFrame({
                'Ordem PagBank': [12345, 12346, 12347, 12348, 12349, 12350],
                'Provider': ['POLO_A', 'POLO_B', 'POLO_A', 'POLO_C', 'POLO_B', 'POLO_A'],
                'SLA Cliente': [5, 3, 7, 4, 6, 8],
                'Status da Ordem': ['Em Aberto', 'Finalizado', 'Em Aberto', 'Em Aberto', 'Cancelado', 'Em Aberto'],
                'Criação da Ordem': [
                    (datetime.now() - timedelta(days=3)).strftime('%d/%m/%Y'),
                    (datetime.now() - timedelta(days=1)).strftime('%d/%m/%Y'),
                    (datetime.now() - timedelta(days=5)).strftime('%d/%m/%Y'),
                    (datetime.now() - timedelta(days=2)).strftime('%d/%m/%Y'),
                    (datetime.now() - timedelta(days=7)).strftime('%d/%m/%Y'),
                    (datetime.now() - timedelta(days=10)).strftime('%d/%m/%Y')
                ],
                'Estado': ['SP', 'RJ', 'SP', 'MG', 'RJ', 'SP'],
                'Cidade': ['São Paulo', 'Rio de Janeiro', 'Campinas', 'Belo Horizonte', 'Niterói', 'Santos'],
                'CEP': ['01000-000', '20000-000', '13000-000', '30000-000', '24000-000', '11000-000'],
                'Último Tracking': ['Em trânsito', 'Entregue', 'Saiu para entrega', 'Em separação', 'Cancelado', 'Aguardando coleta']
            })
            
            # Criar diretório se não existir
            arquivo_dados.parent.mkdir(parents=True, exist_ok=True)
            
            # Salvar arquivo
            dados_exemplo.to_excel(arquivo_dados, index=False)
            logger.info(f"Arquivo de dados de exemplo criado: {arquivo_dados}")
            
        except Exception as e:
            logger.error(f"Erro ao criar arquivo de dados de exemplo: {e}")

# Inicialização
def inicializar_app():
    """Inicializa a aplicação com verificações necessárias"""
    try:
        # Criar diretórios necessários
        criar_diretorios_necessarios()
        
        # Verificar arquivo de dados
        verificar_arquivo_dados()
        
        # Mostrar informações do ambiente
        if is_streamlit_cloud():
            st.sidebar.success("🌐 Executando no Streamlit Cloud")
        else:
            st.sidebar.info("💻 Executando localmente")
            
    except Exception as e:
        st.error(f"Erro na inicialização: {e}")
        logger.error(f"Erro na inicialização: {e}")

# Executar inicialização
inicializar_app()

# Executar o dashboard
try:
    # Verificar se o arquivo do dashboard existe
    dashboard_path = Path('dashboard/app_dashboard.py')
    
    if dashboard_path.exists():
        # Executar o código do dashboard
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            dashboard_code = f.read()
        
        # Executar o código do dashboard
        exec(dashboard_code)
        
    else:
        st.error("❌ Arquivo dashboard/app_dashboard.py não encontrado!")
        st.info("Verifique se todos os arquivos do projeto estão presentes.")
        
except Exception as e:
    st.error(f"❌ Erro ao carregar o dashboard: {e}")
    logger.error(f"Erro ao carregar dashboard: {e}")
    
    # Mostrar informações de debug
    with st.expander("🔍 Informações de Debug"):
        st.write(f"Diretório atual: {Path.cwd()}")
        st.write(f"Arquivos disponíveis:")
        for arquivo in Path('.').glob('**/*.py'):
            st.write(f"- {arquivo}")
    
    st.info("💡 Dicas para resolver:")
    st.write("1. Verifique se todos os arquivos estão no repositório")
    st.write("2. Certifique-se de que o requirements.txt está correto")
    st.write("3. Verifique os logs no Streamlit.io") 