Assignment Description
This Python program fetches data from the FBI's "Most Wanted" API or reads it from a provided JSON file. It extracts fields such as title, subjects, and field_offices and formats the data, separating fields using the lowercase thorn character þ. The program can be executed via command-line arguments to either download data from the FBI API or read it from a local file. The data is printed in the specified format.

How to Install:
To install the package, make sure you are using pipenv to create a virtual environment and install dependencies.

pipenv install -e .

This will set up the environment and dependencies for the project.

How to Run:
The program can be run using the following commands based on whether you want to fetch data from the FBI API or read a local JSON file:

1. Fetch data from FBI API
pipenv run python main.py --page <integer>

2. Read from a local file
pipenv run python main.py --file <file-location>


Functions:

main.py

1. fetch_data(page)
This function downloads data from the FBI API based on the page number provided. It constructs a URL for the API, makes an HTTP request, and returns the fetched data as a JSON object.

2. read_file(file_location):
This function reads data from a local JSON file. It takes the file location as an argument, opens the file, and returns the parsed JSON data.

3. format_data(data):
This function takes the JSON data and extracts the title, subjects, and field_offices fields. It formats these fields, joining multiple values with commas, and returns a list of rows where each field is separated by the thorn character þ.

4. main(page=None, thefile=None):
The main function handles user input to either fetch data from the API or read from a local file. It calls the appropriate functions based on the command-line arguments and prints the formatted data.
