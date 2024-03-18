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


def is_valid_order_id(order_id, processed_data):
    for user_data in processed_data:
        for order in user_data['orders'].values():
            if order.get('order_id') == order_id:
                return True
    return False

def clean_uploads_folder():
    folder_uploads = 'uploads'
    for file in os.listdir(folder_uploads):
        way_file = os.path.join(folder_uploads, file)
        os.remove(way_file)

