from flask import Flask, render_template, request, jsonify, redirect, url_for
from controllers import DataProcessor
from utils import is_valid_date, is_valid_order_id, is_valid_txt_file, filter_data, clean_uploads_folder
import atexit

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            return render_template('init.html', error="Nenhum arquivo selecionado")
        
        if not is_valid_txt_file(uploaded_file.filename):
            return render_template('init.html', error="Somente arquivos .txt sao permitidos")
        
        file_path = DataProcessor.save_uploaded_file(uploaded_file) # Save uploaded file
        processed_data = DataProcessor.process_data(file_path) # Process data
        return redirect(url_for('display_data')) 
    else:
        return render_template('init.html')

@app.route('/display', methods=['GET'])
def display_data():
    order_id = request.args.get('order_id') or None
    start_date = request.args.get('start_date') or None
    end_date = request.args.get('end_date') or None

    # Check if the dates are valid
    if not is_valid_date(start_date) or not is_valid_date(end_date):
        errors = [{"error": "Data invalida"}]
        return render_template('display.html', errors=errors), 400

    # Check if the order_id is valid
    if order_id and not is_valid_order_id(order_id, DataProcessor.processed_data):
       errors = [{"error": "Order ID nao encontrado"}]
       return render_template('display.html', errors=errors), 400

    # Filter data based on passed parameters
    filtered_data = filter_data(DataProcessor.processed_data, order_id, start_date, end_date)

    return render_template('display.html', data=filtered_data), 200

@app.route('/')
def index():
    return render_template('init.html')

# Clear filters 
@app.route('/clear_filters')
def clear_filters():
    return redirect('/display')

# Register the cleanup function to be called when the program exits
atexit.register(clean_uploads_folder)