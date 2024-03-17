from os import makedirs, path
from datetime import datetime
from utils import is_valid_date

class DataProcessor:
    processed_data = []

    def save_uploaded_file(uploaded_file):
        uploads_folder = 'uploads'
        if not path.exists(uploads_folder):
            makedirs(uploads_folder)
        
        file_path = path.join(uploads_folder, uploaded_file.filename)
        uploaded_file.save(file_path)
        return file_path
    
    def process_data(file_path):
        users_data = {}

        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read each line
                
        for line in lines:  # Extract data from each line
            user_id = line[:10].lstrip('0')  # Line[:10] = dividing each line into specific fields based on character positions.
            name = line[10:55].strip()  # Strip() = remove white spaces
            order_id = line[55:65].lstrip('0')  # Lstring() = remove leading zeros
            product_id = line[65:75].lstrip('0')
            total = float(line[75:87])
            date_str = line[87:].strip()
            purchase_date = datetime.strptime(date_str, '%Y%m%d').strftime('%Y-%m-%d')

            # Create a new user if user_id doesn't exist yet
            if user_id not in users_data:
                users_data[user_id] = {
                    'user_id': user_id,
                    'name': name,
                    'orders': {}
                }

            # Create a new order if order_id doesn't exist yet
            if order_id not in users_data[user_id]['orders']:
                users_data[user_id]['orders'][order_id] = {
                    'order_id': order_id,
                    'date': purchase_date,
                    'total': 0,
                    'products': []
                }

            # Add product to the order
            users_data[user_id]['orders'][order_id]['products'].append({
                'product_id': product_id,
                'value': "{:.2f}".format(total)
            })

            # Assign total to the order
            users_data[user_id]['orders'][order_id]['total'] += total 

        DataProcessor.processed_data.extend(users_data.values())
        return DataProcessor.processed_data
