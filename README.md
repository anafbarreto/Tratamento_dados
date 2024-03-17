# Desafio
Create API system that receives denormalized data, performs processing, and returns it in a normalized file. <br>

# Index
* [Data example](#application-result)
* [Project description](#project-description)
* [Technologies used](#technologies-used)
* [Tests](#tests)
* [Project execution](#project-execution)
* [Localhost](#Localhost)
* [Test execution](#test-execution)
* [Thanks](#thanks)

### Application result
Input data: <br><br>
<img src=Images/entrada-dados.png>

Output data: <br><br>
<img src=Images/saida-dados.png>

### Project description
The application has two main routes: <br>
1. '/process' route: which can receive one or more files as a query parameter, reading and processing the data. <br>
2. Route '/display': allows you to view the processed data, and filter it based on optional parameters, such as order ID, start date and end date. <br>

Main functions: <br>
1. `Process_data(file_paths)`: processes data from the provided files. Extracts information such as user ID, name, order ID, product ID, total, and purchase date. <br>
2. `Filter_data(user_data, order_id, start_date, end_date)`: filters user data based on the parameters provided, such as order ID, start date and end date. <br>

### Technologies used
1. Flask: Using the Flask web framework due to its simplicity and flexibility. Flask allowed you to create API routes quickly and easily. <br>
2. Jsonify: Flask's jsonify function was used to format API responses in JSON in a simple and direct way. <br>
3. Datetime: The standard Python datetime library was used to manipulate dates. Allowing you to convert and validate dates as needed during data processing. <br>
4. Pytest: The pytest testing framework was chosen due to its ease of use and powerful testing capabilities. It has clear and concise writing to validate the application's behavior. <br>

Architectural Patterns: <br>
1. MVC (Model-View-Controller) pattern: Although it is not a complete MVC framework, it has a similar approach by dividing the application into model, view and control layers. This allows you to keep the code organized and separated into distinct components. <br>
2. RESTful API: The application follows the principles of a RESTful API, where operations are mapped to HTTP methods (GET, POST, etc.) and resources are accessed through URLs. <br>
3. Separation of Responsibilities: Seeking to maintain a clear separation of responsibilities in the code, where each component (such as API routes, business logic and data manipulation) has a specific and well-defined function. <br>

The choice of technologies and standards were made with a view to simplicity, the volume of data used in testing and maintenance of the application. <br>

### Tests
We have a test chain to cover system functions such as: <br>
1. `test_invalid_file_upload` which validates whether the file has the desired format (.txt). <br>
2. `test_file_upload_and_display` data processing, display route call and filter validation. <br>

Code and test coverage: 70%** (Coverage Report) <br>
** Not taking into account the import and function definition lines. <br>

### Project Execution
Acess: <br>
Datas for test: [data_1.txt](https://github.com/anafbarreto/Tratamento_dados/files/14629307/data_1.txt)  and 
[data_2.txt](https://github.com/anafbarreto/Tratamento_dados/files/14629308/data_2.txt)


### Localhost
The environments with the necessary technologies to run the project locally are already in the .venv folder of this repository. <br>
If in doubt, a file with all the libraries used and how to install them is available in the repository in the “libraries” folder. <br>

1. In the top corner, make a fork. <br><br>
<img src=Images/image-1.png>

2. To activate the .venv environment, in the terminal use: `.\.venv\Scripts\activate`. <br><br>
<img src=Images/image-2.png>

3. To run the application, in the terminal use: flask --app app run <br><br>
<img src=Images/image-3.png>
   Your local server can be opened in the browser itself like Chrome and Edge. <br>

4. To send a file you can use the `Choose file` field. <br><br>
<img src=Images/image-6.png> 

5. As soon as the file is sent using the `Send` button, the page will be automatically redirected to display the processed data. <br><br>
<img src=Images/image-7.png>


### Test execution
1. In the terminal use: pytest test.py to generate the test report. The display will be on the terminal itself. <br>
2. Coverage is enabled to generate HTML output, showing test and application coverage, which can be accessed from the 'Index.html' file in the 'Coverage_html_report' folder in the directory. <br><br>
<img src=Images/image-8.png> <br><br>
Another option is to execute the command: coverage report -m, so the visualization will also be directly in the terminal. <br><br>
<img src=Images/image-9.png>


<br>
<br>
<br>

### Thanks!
![thanks dog](https://github.com/anafbarreto/Tratamento_dados/assets/44984838/a8f741d9-6817-4a2f-a075-8b1bfd1f0a33)









