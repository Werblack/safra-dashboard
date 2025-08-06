# 🚀 Sistema Safra - Dashboard de Monitoramento

Dashboard interativo para monitoramento de ordens e métricas do Sistema Safra, desenvolvido com Streamlit.

## 📊 Funcionalidades

- **Dashboard Interativo**: Visualização em tempo real de métricas
- **Gráficos Dinâmicos**: Gráficos de barras, pizza e linha com Plotly
- **Filtros Avançados**: Filtros por data, provider, status e região
- **Exportação de Dados**: Exportação para Excel com formatação
- **Integração Azure**: Envio de dados para Power Automate
- **Responsivo**: Interface adaptável para diferentes dispositivos

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework para aplicações web
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Gráficos interativos
- **OpenPyXL**: Leitura/escrita de arquivos Excel
- **PyArrow**: Formato de dados otimizado

## 🚀 Deploy no Streamlit.io

### Pré-requisitos

1. **Conta no GitHub** (gratuita)
2. **Conta no Streamlit.io** (gratuita)
3. **Git instalado** no seu computador

### Passo a Passo

#### 1. Preparar Repositório GitHub

```bash
# Navegar para a pasta do projeto
cd "C:\Users\sbahia\OneDrive - UNIVERSO ONLINE S.A\Área de Trabalho\Ambiente PY\logins\Projeto Safra"

# Inicializar repositório Git
git init

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "Initial commit - Sistema Safra Dashboard"

# Renomear branch para main
git branch -M main

# Adicionar repositório remoto (SUBSTITUA pela URL do seu repositório)
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

# Enviar para o GitHub
git push -u origin main
```

#### 2. Configurar Deploy no Streamlit.io

1. **Acesse:** [share.streamlit.io](https://share.streamlit.io)
2. **Faça login** com sua conta GitHub
3. **Clique em "New app"**
4. **Configure:**
   - **Repository:** Selecione seu repositório
   - **Branch:** `main`
   - **Main file path:** `streamlit_app.py`
   - **App URL:** (opcional - será gerado automaticamente)
5. **Clique em "Deploy"**

#### 3. Verificar Deploy

- Aguarde alguns minutos para o deploy ser concluído
- Acesse a URL gerada pelo Streamlit.io
- Teste todas as funcionalidades do dashboard

## 📁 Estrutura do Projeto

```
Projeto Safra/
├── streamlit_app.py          # ✅ Ponto de entrada principal
├── requirements.txt          # ✅ Dependências Python
├── packages.txt             # ✅ Dependências do sistema
├── .streamlit/
│   └── config.toml          # ✅ Configurações do Streamlit
├── dashboard/
│   └── app_dashboard.py     # ✅ Dashboard principal
├── data/                    # ✅ Dados do projeto
│   ├── input/              # Arquivos de entrada
│   ├── processed/          # Dados processados
│   └── backup/            # Backups
├── config/                  # ✅ Configurações
├── models/                  # ✅ Modelos
├── src/                     # ✅ Código fonte
├── .gitignore              # ✅ Arquivos ignorados
└── README.md               # ✅ Documentação
```

## 🔧 Configurações

### Arquivo Principal: `streamlit_app.py`

- Ponto de entrada para o Streamlit.io
- Configura a página e executa o dashboard
- Inclui verificações de ambiente e inicialização automática

### Dependências: `requirements.txt`

```
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.15.0
openpyxl>=3.1.0
pyarrow>=12.0.0
pytz>=2023.3
pyyaml>=6.0
psutil>=5.9.0
requests>=2.31.0
```

### Configurações: `.streamlit/config.toml`

- Tema personalizado com cores do Safra
- Configurações de servidor otimizadas
- Modo de desenvolvimento desabilitado

## 🚨 Solução de Problemas

### Erro: "Module not found"

- Verifique se todas as dependências estão em `requirements.txt`
- Certifique-se de que os caminhos dos arquivos estão corretos

### Erro: "File not found"

- Verifique se os arquivos de dados estão na pasta `data/`
- O sistema criará arquivos de exemplo automaticamente

### Erro: "Permission denied"

- Verifique se o arquivo `streamlit_app.py` tem permissões de execução

### Erro: "Cache issues"

- O sistema usa cache otimizado para melhor performance
- Em caso de problemas, o cache será recriado automaticamente

## 📞 Suporte

Se encontrar problemas:

1. **Verifique os logs** no Streamlit.io
2. **Teste localmente** primeiro: `streamlit run streamlit_app.py`
3. **Verifique se todos os arquivos** estão no repositório
4. **Consulte a documentação** do Streamlit.io

## 🎉 Próximos Passos

Após o deploy bem-sucedido:

1. **Configure integrações** com Azure Logic Apps
2. **Adicione dados reais** na pasta `data/`
3. **Personalize o tema** conforme necessário
4. **Configure notificações** e alertas
5. **Monitore o desempenho** da aplicação

## 📈 Métricas Disponíveis

- **Total de Ordens em Aberto**
- **Ordens em Atraso**
- **Percentual de Atraso**
- **SLA Médio**
- **Ranking de Polos**
- **Distribuição por Status**
- **Análise por Região**

## 🔐 Segurança

- **Dados sensíveis** não são incluídos no repositório
- **Configurações de segurança** aplicadas
- **Logs de erro** para debugging
- **Validação de entrada** implementada

---

**Desenvolvido com ❤️ para o Sistema Safra**
