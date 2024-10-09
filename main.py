from lxml import etree  # Import the etree module from the lxml library for working with XML
import json  # Import the json library to handle JSON data
from pathlib import Path  # Import Path from the pathlib library to manage file paths

# Define the directory path where the input and output files are located
data_dir = Path.cwd() / 'data'

# Specify the path to your JSON file
input_file_path = data_dir / 'input.json'  # Path for the input JSON file
output_file_path = data_dir / 'output.xml'  # Path for the output XML file

# Open and read the JSON file
with open(/Users/sriramyapanja/PycharmProjects/week_7_lab_1 'r') as file:
    data = json.load(file)  # Load JSON data into a Python dictionary

# Extract healthcare data and patient information from the JSON data
healthcare_data = data['healthcare_data']  # Access the main 'healthcare_data' dictionary
patients = healthcare_data['patients']  # Access the list of patients within the healthcare data
first_patient = patients[0]  # Select the first patient in the list

# Extract specific details of the first patient
first_patient_id = first_patient['id']  # Retrieve the patient's ID
first_patient_name = first_patient['name']  # Retrieve the patient's name
first_patient_age = first_patient['age']  # Retrieve the patient's age
first_patient_gender = first_patient['gender']  # Retrieve the patient's gender

# Create the XML structure
root = etree.Element("patient")  # Create the root element for the XML document
root.set("id", str(first_patient_id))  # Set the patient's ID as an attribute of the root element

# Add a sub-element for the patient's name and set its text
patient_name = etree.SubElement(root, "name")  # Create a 'name' element as a child of 'patient'
patient_name.text = first_patient_name  # Set the text of the 'name' element to the patient's name

# Add sub-elements for age and gender
patient_age = etree.SubElement(root, "age")  # Create an 'age' element as a child of 'patient'
patient_age.text = str(first_patient_age)  # Set the text of the 'age' element to the patient's age

patient_gender = etree.SubElement(root, "gender")  # Create a 'gender' element as a child of 'patient'
patient_gender.text = first_patient_gender  # Set the text of the 'gender' element to the patient's gender

# Create an ElementTree object from the root element
tree = etree.ElementTree(root)

# Open the file for writing in binary mode and write the XML content to it
# The 'pretty_print=True' option formats the output nicely with indentation
# 'xml_declaration=True' adds the XML declaration (e.g., <?xml version='1.0'?>)
# 'encoding="UTF-8"' ensures the file is encoded in UTF-8
with open(output_file_path, "wb") as file:
    file.write(etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))
