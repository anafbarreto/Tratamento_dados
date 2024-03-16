from flask import Flask, render_template, request, jsonify, redirect, url_for
from controllers import DataProcessor
from utils import is_valid_date, is_valid_order_id, is_valid_txt_file, filter_data, limpar_pasta_uploads
import atexit


app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            return render_template('init.html', error="Nenhum arquivo selecionado")
        
        if not is_valid_txt_file(uploaded_file.filename):
            return render_template('init.html', error="Somente arquivos .txt são permitidos")
        
        file_path = DataProcessor.save_uploaded_file(uploaded_file)
        processed_data = DataProcessor.process_data(file_path)
        return redirect(url_for('display_data'))
    else:
        return render_template('init.html')

@app.route('/display', methods=['GET'])
def display_data():
    order_id = request.args.get('order_id') or None
    start_date = request.args.get('start_date') or None
    end_date = request.args.get('end_date') or None

    if not is_valid_date(start_date) or not is_valid_date(end_date):
        errors = [{"error": "Data invalida"}]
        return render_template('display.html', errors=errors)

    # Verifica se o order_id é válido
    if order_id and not is_valid_order_id(order_id, DataProcessor.processed_data):
        errors = [{"error": "Order ID não encontrado"}]
        return render_template('display.html', errors=errors)

    # Filtrar os dados
    filtered_data = filter_data(DataProcessor.processed_data, order_id, start_date, end_date)

    # Passar os dados filtrados para o template HTML
    return render_template('display.html', data=filtered_data)

@app.route('/')
def index():
    return render_template('init.html')

@app.route('/clear_filters')
def clear_filters():
    return redirect('/display')

# Registrar a função de limpeza para ser chamada no encerramento do programa
atexit.register(limpar_pasta_uploads)