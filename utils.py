from datetime import datetime
import atexit
import os

def filter_orders(orders, order_id, start_date, end_date):
    filtered_orders = {}
    for order in orders.values():
        if (order_id is None or order['order_id'] == order_id) and \
           (start_date is None or order['date'] >= start_date) and \
           (end_date is None or order['date'] <= end_date):
            filtered_orders[order['order_id']] = order
    return filtered_orders

def filter_data(processed_data, order_id, start_date, end_date):
    filtered_data = []
    for user_data in processed_data:
        filtered_orders = filter_orders(user_data['orders'], order_id, start_date, end_date)
        if filtered_orders:
            user_data_copy = user_data.copy()
            user_data_copy['orders'] = list(filtered_orders.values())
            filtered_data.append(user_data_copy)

    # Round total values
    for user_data in filtered_data:
        for order in user_data['orders']:
            order['total'] = round(order['total'], 2)

    return filtered_data

def is_valid_txt_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'txt'

def is_valid_date(date_str):
    if date_str is None:
        return True  # Considera datas em branco como válidas
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        # Verifica se a data é anterior ou igual à data atual
        current_date = datetime.now().date()
        return date_obj.date() <= current_date
    except ValueError:
        return False

def is_valid_order_id(order_id, processed_data):
    for user_data in processed_data:
        for order in user_data['orders'].values():
            if order.get('order_id') == order_id:
                return True
    return False

def limpar_pasta_uploads():
    pasta_uploads = 'uploads'
    for arquivo in os.listdir(pasta_uploads):
        caminho_arquivo = os.path.join(pasta_uploads, arquivo)
        os.remove(caminho_arquivo)

# Registrar a função de limpeza para ser chamada no encerramento do programa
atexit.register(limpar_pasta_uploads)
