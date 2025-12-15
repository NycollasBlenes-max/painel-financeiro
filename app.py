from flask import Flask, render_template, jsonify, request, send_from_directory
from datetime import datetime
import random
import logging
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Rota para favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'Simbolo.png', mimetype='image/png')

# DADOS EM MEMÓRIA
dados_bancos_memoria = [
    {'BANCO': 'SICOOB - REDE CONFIANÇA', 'CONTA': 'AG: 301 CC: 203409', 'APLICACAO_INVESTIMENTO': 5000.00, 'UTILIZACAO_CONTA_GARANTIDA': 2000.00, 'SALDO': 15000.00, 'TOTAL_DISPONIVEL': 20000.00, 'PAGAMENTOS': 1200.50, 'TRANSFERENCIA': 800.00, 'SALDO_FINAL': 18000.00, 'LINHA_SHEETS': 2},
    {'BANCO': 'BANESTES - REDE CONFIANÇA', 'CONTA': 'AG: 083 CC: 1272125', 'APLICACAO_INVESTIMENTO': 3000.00, 'UTILIZACAO_CONTA_GARANTIDA': 1500.00, 'SALDO': 12000.00, 'TOTAL_DISPONIVEL': 15500.00, 'PAGAMENTOS': 950.00, 'TRANSFERENCIA': 500.00, 'SALDO_FINAL': 14550.00, 'LINHA_SHEETS': 3},
    {'BANCO': 'BRADESCO - REDE CONFIANÇA', 'CONTA': 'AG: 2612 CC: 36365', 'APLICACAO_INVESTIMENTO': 4500.00, 'UTILIZACAO_CONTA_GARANTIDA': 1800.00, 'SALDO': 18000.00, 'TOTAL_DISPONIVEL': 22500.00, 'PAGAMENTOS': 1500.75, 'TRANSFERENCIA': 1000.00, 'SALDO_FINAL': 21000.00, 'LINHA_SHEETS': 4},
    {'BANCO': 'BANCO DO BRASIL', 'CONTA': 'AG: 21 CC: 21719', 'APLICACAO_INVESTIMENTO': 6000.00, 'UTILIZACAO_CONTA_GARANTIDA': 2500.00, 'SALDO': 25000.00, 'TOTAL_DISPONIVEL': 33500.00, 'PAGAMENTOS': 2000.00, 'TRANSFERENCIA': 1500.00, 'SALDO_FINAL': 32000.00, 'LINHA_SHEETS': 5},
    {'BANCO': 'BANCO INTER - REDE CONFIANÇA', 'CONTA': 'AG: 0001 CC: 8413470', 'APLICACAO_INVESTIMENTO': 3500.00, 'UTILIZACAO_CONTA_GARANTIDA': 1200.00, 'SALDO': 10000.00, 'TOTAL_DISPONIVEL': 14700.00, 'PAGAMENTOS': 800.00, 'TRANSFERENCIA': 600.00, 'SALDO_FINAL': 13900.00, 'LINHA_SHEETS': 6},
    {'BANCO': 'CORA - REDE CONFIANÇA', 'CONTA': 'AG: 0001 CC: 5000000', 'APLICACAO_INVESTIMENTO': 2000.00, 'UTILIZACAO_CONTA_GARANTIDA': 500.00, 'SALDO': 8000.00, 'TOTAL_DISPONIVEL': 10500.00, 'PAGAMENTOS': 600.00, 'TRANSFERENCIA': 400.00, 'SALDO_FINAL': 10100.00, 'LINHA_SHEETS': 7},
    {'BANCO': 'XP INVESTIMENTOS - REDE CONFIANÇA', 'CONTA': 'AG: 0001 CC: 1614928', 'APLICACAO_INVESTIMENTO': 7000.00, 'UTILIZACAO_CONTA_GARANTIDA': 3000.00, 'SALDO': 22000.00, 'TOTAL_DISPONIVEL': 29000.00, 'PAGAMENTOS': 1800.00, 'TRANSFERENCIA': 1200.00, 'SALDO_FINAL': 28400.00, 'LINHA_SHEETS': 8},
    {'BANCO': 'INFINITY PAY - REDE CONFIANÇA', 'CONTA': 'AG: 0001 CC: 9999999', 'APLICACAO_INVESTIMENTO': 2500.00, 'UTILIZACAO_CONTA_GARANTIDA': 800.00, 'SALDO': 9000.00, 'TOTAL_DISPONIVEL': 12000.00, 'PAGAMENTOS': 700.00, 'TRANSFERENCIA': 450.00, 'SALDO_FINAL': 11750.00, 'LINHA_SHEETS': 9},
    {'BANCO': 'PAGSEGURO - REDE CONFIANÇA', 'CONTA': 'AG: 0001 CC: 52166027', 'APLICACAO_INVESTIMENTO': 1500.00, 'UTILIZACAO_CONTA_GARANTIDA': 400.00, 'SALDO': 5500.00, 'TOTAL_DISPONIVEL': 7200.00, 'PAGAMENTOS': 450.00, 'TRANSFERENCIA': 300.00, 'SALDO_FINAL': 7050.00, 'LINHA_SHEETS': 10}
]

estatisticas_memoria = {'saldo': 94500.00, 'aplicacao': 34000.00, 'pagamentos': 10401.25, 'saldo_final': 116750.00}

demonstrativo_diario_memoria = [
    {'vencimento': '14/12/2025', 'fornecedor': 'FORNECEDOR A', 'observacoes': 'Serviços de Consultoria', 'filial': 'MATRIZ', 'valor_liquido': 5000.00, 'banco_pagador': 'SICOOB - REDE CONFIANÇA'},
    {'vencimento': '14/12/2025', 'fornecedor': 'FORNECEDOR B', 'observacoes': 'Materiais e Suprimentos', 'filial': 'FILIAL 1', 'valor_liquido': 3200.00, 'banco_pagador': 'BANESTES - REDE CONFIANÇA'},
    {'vencimento': '14/12/2025', 'fornecedor': 'FORNECEDOR C', 'observacoes': 'Serviços de Manutenção', 'filial': 'FILIAL 2', 'valor_liquido': 2500.00, 'banco_pagador': 'BRADESCO - REDE CONFIANÇA'}
]

filtro_datas_memoria = {'data_inicio': '2025-12-01', 'data_fim': '2025-12-31'}

@app.template_filter('currency')
def currency_filter(value):
    try:
        if isinstance(value, str):
            value = float(value.replace(',', '.'))
        if value >= 1000:
            formatted = f"R$ {value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        else:
            formatted = f"R$ {value:.2f}".replace('.', ',')
        return formatted
    except (ValueError, TypeError):
        return "R$ 0,00"

def gerar_dados_aleatorios():
    global dados_bancos_memoria, estatisticas_memoria
    for banco in dados_bancos_memoria:
        variacao = random.uniform(0.95, 1.05)
        banco['SALDO'] = round(banco['SALDO'] * variacao, 2)
        banco['APLICACAO_INVESTIMENTO'] = round(banco['APLICACAO_INVESTIMENTO'] * variacao, 2)
        banco['PAGAMENTOS'] = round(random.uniform(500, 3000), 2)
        banco['TRANSFERENCIA'] = round(random.uniform(200, 1500), 2)
        banco['TOTAL_DISPONIVEL'] = round(banco['SALDO'] + banco['APLICACAO_INVESTIMENTO'], 2)
        banco['SALDO_FINAL'] = round(banco['TOTAL_DISPONIVEL'] - banco['PAGAMENTOS'] + banco['TRANSFERENCIA'], 2)
    
    estatisticas_memoria['saldo'] = round(sum(b['SALDO'] for b in dados_bancos_memoria), 2)
    estatisticas_memoria['aplicacao'] = round(sum(b['APLICACAO_INVESTIMENTO'] for b in dados_bancos_memoria), 2)
    estatisticas_memoria['pagamentos'] = round(sum(b['PAGAMENTOS'] for b in dados_bancos_memoria), 2)
    estatisticas_memoria['saldo_final'] = round(sum(b['SALDO_FINAL'] for b in dados_bancos_memoria), 2)
    logger.info(f"Dados atualizados - Saldo Total: {estatisticas_memoria['saldo']}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

@app.route('/api/estatisticas')
def obter_estatisticas():
    try:
        logger.info("Solicitação de estatísticas recebida")
        return jsonify({'success': True, 'estatisticas': estatisticas_memoria, 'timestamp': datetime.now().isoformat()})
    except Exception as e:
        logger.error(f"Erro ao obter estatísticas: {str(e)}")
        return jsonify({'success': False, 'message': f'Erro ao obter estatísticas: {str(e)}'}), 500

@app.route('/api/demonstrativo-diario')
def obter_demonstrativo_diario():
    try:
        logger.info("Solicitação de demonstrativo diário recebida")
        data_hoje = datetime.now().strftime('%d/%m/%Y')
        registros_hoje = [r for r in demonstrativo_diario_memoria if r['vencimento'] == data_hoje]
        valor_total = sum(r['valor_liquido'] for r in registros_hoje)
        return jsonify({'success': True, 'registros': registros_hoje, 'total_registros': len(registros_hoje), 'valor_total': valor_total, 'data_consulta': data_hoje, 'timestamp': datetime.now().isoformat()})
    except Exception as e:
        logger.error(f"Erro ao obter demonstrativo diário: {str(e)}")
        return jsonify({'success': False, 'message': f'Erro ao obter demonstrativo: {str(e)}'}), 500

@app.route('/api/acompanhamento-contas')
def obter_acompanhamento_contas():
    try:
        logger.info("Solicitação de acompanhamento de contas recebida")
        bancos = []
        for banco in dados_bancos_memoria:
            banco_info = {'nome': banco['BANCO'], 'conta': banco['CONTA'], 'saldo': banco['SALDO'], 'aplicacao': banco['APLICACAO_INVESTIMENTO'], 'pagamentos': banco['PAGAMENTOS'], 'transferencia': banco['TRANSFERENCIA'], 'saldo_final': banco['SALDO_FINAL']}
            bancos.append(banco_info)
        return jsonify({'success': True, 'bancos': bancos, 'total_bancos': len(bancos), 'timestamp': datetime.now().isoformat()})
    except Exception as e:
        logger.error(f"Erro ao obter acompanhamento de contas: {str(e)}")
        return jsonify({'success': False, 'message': f'Erro ao obter acompanhamento: {str(e)}'}), 500

@app.route('/api/teste')
def teste_api():
    return jsonify({'success': True, 'message': 'API funcionando corretamente', 'timestamp': datetime.now().isoformat()})

@app.route('/carregar-saldo-bancos', methods=['GET'])
def carregar_saldo_bancos_route():
    try:
        logger.info("Carregando dados dos bancos")
        return jsonify({'success': True, 'dados_bancos': dados_bancos_memoria, 'message': f'Dados carregados: {len(dados_bancos_memoria)} bancos'})
    except Exception as e:
        logger.error(f"Erro ao carregar saldo bancos: {str(e)}")
        return jsonify({'success': False, 'message': f'Erro ao carregar dados: {str(e)}'}), 500

@app.route('/salvar-saldo-bancos', methods=['POST'])
def salvar_saldo_bancos_route():
    try:
        global dados_bancos_memoria
        data = request.get_json()
        dados_bancos = data.get('dados_bancos', [])
        if not dados_bancos:
            return jsonify({'success': False, 'message': 'Nenhum dado fornecido para salvar'}), 400
        logger.info(f"Salvando dados: {len(dados_bancos)} bancos")
        dados_bancos_memoria = dados_bancos
        estatisticas_memoria['saldo'] = round(sum(b.get('SALDO', 0) for b in dados_bancos_memoria), 2)
        estatisticas_memoria['aplicacao'] = round(sum(b.get('APLICACAO_INVESTIMENTO', 0) for b in dados_bancos_memoria), 2)
        estatisticas_memoria['pagamentos'] = round(sum(b.get('PAGAMENTOS', 0) for b in dados_bancos_memoria), 2)
        estatisticas_memoria['saldo_final'] = round(sum(b.get('SALDO_FINAL', 0) for b in dados_bancos_memoria), 2)
        return jsonify({'success': True, 'message': f'Dados salvos com sucesso! {len(dados_bancos)} bancos atualizados.', 'bancos_atualizados': len(dados_bancos)})
    except Exception as e:
        logger.error(f"Erro ao salvar saldo bancos: {str(e)}")
        return jsonify({'success': False, 'message': f'Erro ao salvar dados: {str(e)}'}), 500

@app.route('/aplicar-filtro-data', methods=['POST'])
def aplicar_filtro_data():
    try:
        global filtro_datas_memoria
        data = request.get_json()
        data_inicio = data.get('data_inicio')
        data_fim = data.get('data_fim')
        logger.info(f"Aplicando filtro de data: {data_inicio} a {data_fim}")
        if not data_inicio or not data_fim:
            return jsonify({'success': False, 'message': 'Datas de início e fim são obrigatórias'}), 400
        try:
            datetime.strptime(data_inicio, '%Y-%m-%d')
            datetime.strptime(data_fim, '%Y-%m-%d')
        except ValueError:
            return jsonify({'success': False, 'message': 'Formato de data inválido (use YYYY-MM-DD)'}), 400
        filtro_datas_memoria['data_inicio'] = data_inicio
        filtro_datas_memoria['data_fim'] = data_fim
        return jsonify({'success': True, 'message': f'Filtro de data aplicado: {data_inicio} a {data_fim}', 'data_inicio': data_inicio, 'data_fim': data_fim})
    except Exception as e:
        logger.error(f"Erro ao aplicar filtro de data: {str(e)}")
        return jsonify({'success': False, 'message': f'Erro ao aplicar filtro: {str(e)}'}), 500

@app.route('/gerar-planilha', methods=['POST'])
def gerar_planilha():
    try:
        data_inicio = request.form.get('data_inicio')
        data_fim = request.form.get('data_fim')
        logger.info(f"Atualizando dados - Período: {data_inicio} a {data_fim}")
        gerar_dados_aleatorios()
        data_hoje = datetime.now().strftime('%d/%m/%Y')
        for reg in demonstrativo_diario_memoria:
            reg['vencimento'] = data_hoje
        try:
            periodo_formatado = f"{datetime.strptime(data_inicio, '%Y-%m-%d').strftime('%d/%m/%Y')} a {datetime.strptime(data_fim, '%Y-%m-%d').strftime('%d/%m/%Y')}"
        except:
            periodo_formatado = f"{data_inicio} a {data_fim}"
        return render_template('sucesso.html', total_registros=len(dados_bancos_memoria), timestamp=datetime.now().strftime('%H:%M:%S'), periodo=periodo_formatado, resultado_google_sheets={'success': True, 'message': 'Dados atualizados em memória'}, pagamentos_por_banco={}, dados_saldo_bancos=dados_bancos_memoria, data_inicio=filtro_datas_memoria['data_inicio'], data_fim=filtro_datas_memoria['data_fim'])
    except Exception as e:
        error_message = str(e)
        logger.error(f"Erro ao atualizar dados: {error_message}")
        return jsonify({'success': False, 'message': f'Erro ao atualizar: {error_message}'}), 500

@app.route('/enviar-whatsapp', methods=['POST'])
def enviar_whatsapp_route():
    return jsonify({'success': False, 'message': 'Funcionalidade de WhatsApp não disponível. Os dados foram atualizados na memória do sistema.'})

@app.route('/verificar-google-config')
def verificar_google_config():
    return jsonify({'configured': True, 'message': 'Sistema funcionando com dados fictícios em memória!'})

if __name__ == '__main__':
    logger.info("Iniciando aplicação Flask na porta 5011")
    app.run(host='0.0.0.0', port=5011)
