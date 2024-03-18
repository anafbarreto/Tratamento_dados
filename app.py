# app.py (ou main.py)
from flask import Flask
from routes import upload_file, display_data, index, clear_filters
from utils import  clean_uploads_folder
import atexit

app = Flask(__name__)

# Rotas
app.route('/upload', methods=['GET', 'POST'])(upload_file)
app.route('/display', methods=['GET'])(display_data)
app.route('/', methods=['GET'])(index)
app.route('/clear_filters', methods=['GET'])(clear_filters)

# Registro da função de limpeza
atexit.register(clean_uploads_folder)

if __name__ == '__main__':
    app.run(debug=True)
