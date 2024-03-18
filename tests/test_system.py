import pytest
import coverage
import os
from app import app
from controllers import DataProcessor
from werkzeug.datastructures import FileStorage

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_invalid_file_upload(client):
    # Test case: Upload invalid file
    with open('tests/invalid_file.pdf', 'rb') as f:  
        file = FileStorage(f)
        response = client.post('/upload', data={'file': file})
    assert response.status_code == 200
    assert b"Somente arquivos .txt sao permitidos" in response.data

def test_file_upload_and_display(client):
    # Test case: Upload valid file
    with open('tests/valid_file.txt', 'rb') as f:
        file = FileStorage(f)
        response = client.post('/upload', data={'file': file})
    
    assert response.status_code == 302  # Redirect to display_data route

    # Test case: Display data after upload
    response = client.get('/display')
    assert response.status_code == 200
    assert b"Palmer Prosacco" in response.data
    assert b"Bobbie Batz" in response.data

def test_data_processing():
    # File input data
    input_file_path = 'tests/valid_file.txt'  
    
    # Processed data
    processed_data = DataProcessor.process_data(input_file_path)
    for user_data in processed_data:
        assert "user_id" in user_data
        assert "name" in user_data
        assert "orders" in user_data

def test_filters(client):
    # Test case: Invalid order_id filter
    response = client.get('/display?order_id=0')
    assert response.status_code == 400
    assert b"Order ID nao encontrado" in response.data
    
    # Test case: Valid date filter
    response = client.get('/display?start_date=2021-01-01&end_date=2021-12-31')
    assert response.status_code == 200
    assert b"Palmer Prosacco" in response.data
    assert b"Bobbie Batz" in response.data
    
    # Test case: Valid order_id filter
    response = client.get('/display?order_id=753')
    assert response.status_code == 200
    assert b"Palmer Prosacco" in response.data
    
    # Test case: all valid filters
    response = client.get('/display?start_date=2021-01-01&end_date=2021-12-31&order_id=798')
    assert response.status_code == 200
    assert b"Bobbie Batz" in response.data

def test_upload_folder_emptiness():
    # Verify if the upload folder is empty
    assert len(os.listdir('uploads')) == 0
    
def test_coverage():
    cov = coverage.Coverage()
    cov.start()

    pytest.main(['-v'])  # Running all tests

    cov.stop()
    cov.html_report(directory='coverage_html_report')  # Generating coverage report
