# routes.py
from flask import render_template, redirect, url_for, request
from models import DataProcessor
from utils import is_valid_order_id, is_valid_txt_file, filter_data

def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if not is_valid_txt_file(uploaded_file.filename):
            return render_template('index.html', error="Somente arquivos .txt sao permitidos")
        
        file_path = DataProcessor.save_uploaded_file(uploaded_file) # Save uploaded file
        processed_data = DataProcessor.process_data(file_path) # Process data
        return redirect(url_for('display_data')) 
    else:
        return render_template('index.html')

def display_data():
    order_id = request.args.get('order_id') or None
    start_date = request.args.get('start_date') or None
    end_date = request.args.get('end_date') or None

    # Check if the order_id is valid
    if order_id and not is_valid_order_id(order_id, DataProcessor.processed_data):
       errors = [{"error": "Order ID nao encontrado"}]
       return render_template('display.html', errors=errors), 400

    # Filter data based on passed parameters
    filtered_data = filter_data(DataProcessor.processed_data, order_id, start_date, end_date)
    
    # Check if filtered data is empty
    if not filtered_data:
        errors = [{"error": "Dados nao encontrados"}]
        return render_template('display.html', errors=errors), 404

    return render_template('display.html', data=filtered_data), 200

def index():
    return render_template('index.html')

def clear_filters():
    return redirect('/display')
