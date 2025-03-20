# 🚔 FBI Most Wanted Data Fetcher

## 📌 Assignment Description

This Python program fetches data from the **FBI's "Most Wanted" API** or reads it from a provided **JSON file**. It extracts essential fields such as:
- **Title**
- **Subjects**
- **Field Offices**

The data is then formatted, with fields separated using the **lowercase thorn character (þ)**.

---

## ✨ Features

✅ Fetch data from the **FBI API** or a **local JSON file**  
✅ Format the extracted fields in a structured manner  
✅ Command-line execution for flexible usage  
✅ Uses **spaCy NLP** for efficient text processing  
✅ Lightweight and easy to use  

---

## 📥 Installation Guide

Ensure you have `pipenv` installed to **create a virtual environment** and **manage dependencies**.

Run the following command to set up the environment:

```sh
pipenv install -e .

## 📜 **Functions Overview**

### **🔹 `main.py`**
This file contains all core functions of the project.

### 1️⃣ **`fetch_data(page)`**
- **Purpose:** Fetches data from the **FBI API** for the given page number.
- **Process:**
  - Constructs the **API URL**.
  - Makes an **HTTP request**.
  - Returns the **JSON response** containing the "Most Wanted" criminals.

### 2️⃣ **`read_file(file_location)`**
- **Purpose:** Reads data from a **local JSON file**.
- **Process:**
  - Takes the **file path** as an argument.
  - Opens the file and **parses the JSON data**.
  - Returns the structured JSON content.

### 3️⃣ **`format_data(data)`**
- **Purpose:** Extracts and formats **specific fields** from the JSON data.
- **Process:**
  - Extracts **title, subjects, and field_offices** fields.
  - Joins multiple values with **commas**.
  - Returns a list of **rows formatted with the thorn character (þ) as a separator**.

### 4️⃣ **`main(page=None, thefile=None)`**
- **Purpose:** Controls program execution based on user input.
- **Process:**
  - **Decides** whether to fetch data from the **FBI API** or a **local file**.
  - Calls the **appropriate functions** (`fetch_data` or `read_file`).
  - Formats the output using `format_data`.
  - Prints the **formatted data** in the specified format.

## 🚀 **How to Run**

The program supports **two execution modes**:
1. **Fetch data from the FBI API**
2. **Read data from a local JSON file**

### 🔹 **Fetching Data from the FBI API**
To fetch real-time data from the **FBI's Most Wanted API**, use the following command:

```sh
pipenv run python main.py --page <integer>


