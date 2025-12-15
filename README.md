# Painel Financeiro

Um painel de controle financeiro desenvolvido em Flask para gerenciar e acompanhar informações bancárias, demonstrativos diários e estatísticas financeiras.

## 📋 Características

- **Dashboard Interativo**: Visualização de dados bancários em tempo real
- **Gerenciamento de Contas**: Acompanhamento de múltiplas contas bancárias
- **Demonstrativo Diário**: Registro de pagamentos e transações
- **Estatísticas Financeiras**: Análise de saldos, aplicações e transferências
- **Filtros de Data**: Consulta de dados por período
- **Interface Responsiva**: Design adaptado para desktop e dispositivos móveis
- **Integração WhatsApp**: Funcionalidade para notificações via WhatsApp
- **Google Sheets**: Integração com Google Sheets para sincronização de dados

## 🚀 Tecnologias Utilizadas

- **Flask** 2.3.3 - Framework web Python
- **Python 3.x** - Linguagem de programação
- **Jinja2** - Template engine
- **pandas** - Manipulação e análise de dados
- **Google Sheets API** - Integração com Google Sheets
- **MySQL** - Banco de dados (opcional)
- **Bootstrap** - Framework CSS (frontend)

## 📦 Dependências

Todas as dependências estão listadas em `requirements.txt`. As principais são:

- Flask e extensões (Flask-Cors, Flask-Session, Flask-SQLAlchemy)
- Google APIs (google-api-python-client, gspread)
- pandas, numpy - Processamento de dados
- mysql-connector-python - Conexão com MySQL
- python-dotenv - Gerenciamento de variáveis de ambiente

## 🛠️ Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. **Clone o repositório**
   ```bash
   git clone https://github.com/NycollasBlenes-max/painel-financeiro.git
   cd painel-financeiro
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure variáveis de ambiente**
   Crie um arquivo `.env` na raiz do projeto com as configurações necessárias:
   ```env
   FLASK_ENV=development
   FLASK_DEBUG=False
   SECRET_KEY=sua_chave_secreta_aqui
   ```

5. **Execute a aplicação**
   ```bash
   python3 app.py
   ```

   A aplicação estará disponível em `http://localhost:5011`

## 📁 Estrutura do Projeto

```
painel-financeiro/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências do projeto
├── README.md             # Este arquivo
├── static/               # Arquivos estáticos (CSS, JS, imagens)
│   └── FUNDO-BI.jpg     # Imagem de fundo
├── templates/            # Templates HTML
│   ├── index.html       # Dashboard principal
│   ├── relatorios.html  # Página de relatórios
│   ├── sucesso.html     # Página de sucesso
│   └── sucesso_backup.html
└── __pycache__/         # Cache Python (ignorar)
```

## 📊 Funcionalidades Principais

### Dashboard (index.html)
- Visualização de contas bancárias
- Exibição de estatísticas financeiras
- Demonstrativo diário de pagamentos
- Filtros por data

### Relatórios (relatorios.html)
- Geração de relatórios detalhados
- Exportação de dados

### API Endpoints

#### GET `/`
Retorna o dashboard principal

#### GET `/api/bancos`
Retorna lista de todas as contas bancárias

#### GET `/api/estatisticas`
Retorna estatísticas financeiras consolidadas

#### GET `/api/demonstrativo`
Retorna demonstrativo diário de transações

#### POST `/atualizar-dados`
Atualiza dados na memória do sistema

#### POST `/backup`
Realiza backup dos dados

#### POST `/enviar-whatsapp`
Envia notificações via WhatsApp

#### GET `/verificar-google-config`
Verifica configuração do Google Sheets

## 🔒 Segurança

- A aplicação usa uma chave secreta para sessões
- Debug mode desativado em produção
- Variáveis sensíveis devem ser configuradas via `.env`
- CORS configurado para produção

## 📝 Dados em Memória

A aplicação atualmente armazena dados em memória com informações fictícias dos seguintes bancos:

- SICOOB - REDE CONFIANÇA
- BANESTES - REDE CONFIANÇA
- BRADESCO - REDE CONFIANÇA
- BANCO DO BRASIL
- BANCO INTER - REDE CONFIANÇA
- CORA - REDE CONFIANÇA
- XP INVESTIMENTOS - REDE CONFIANÇA
- INFINITY PAY - REDE CONFIANÇA
- PAGSEGURO - REDE CONFIANÇA

## 🚦 Desenvolvimento

Para desenvolvimento local com hot-reload:

```bash
export FLASK_ENV=development
export FLASK_DEBUG=True
python3 app.py
```

## 📦 Deployment

Para deploy em produção:

1. Garanta que `debug=False` em `app.run()`
2. Use um servidor WSGI como Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5011 app:app
   ```

3. Configure um proxy reverso (Nginx/Apache)
4. Use HTTPS em produção

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

## 👨‍💻 Autor

**Nycollas Blenes**
- GitHub: [@NycollasBlenes-max](https://github.com/NycollasBlenes-max)

## 📧 Contato

Para dúvidas ou sugestões, abra uma issue no repositório.

## 🔄 Versão

**Versão:** 1.0.0  
**Última atualização:** 14 de dezembro de 2025

---

**Nota:** Este projeto utiliza dados fictícios em memória para demonstração. Para produção, configure uma conexão com banco de dados real.
