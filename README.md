# MTC Typing Competition

Welcome to the MTC Typing Competition! This is a custom Tkinter-based application designed for a typing competition, evaluating typing speed and accuracy, and recording the results in a MySQL database.

## Features

- **Random Paragraphs**: Provides random paragraphs for typing tests.
- **Speed and Accuracy Calculation**: Measures typing speed in WPM and accuracy.
- **Database Integration**: Stores results in a MySQL database.
- **Resource Links**: Provides additional learning resources.

## Requirements

- Python 3.x
- `customtkinter`
- `mysql-connector-python`
- `PIL` (Pillow)

## Installation

1. **Clone the repository:**
    ```sh
    git clone <https://github.com/Mahin200405/MTC-Typing-Competition/tree/main>
    cd <MTC-Typing-Competition>
    ```

2. **Install the required packages:**
    ```sh
    pip install customtkinter mysql-connector-python pillow
    ```

3. **Set up the MySQL database:**
    ```sql
    CREATE DATABASE MTCTyping;
    USE MTCTyping;
    CREATE TABLE results (
        name varchar(100),
        speed varchar(5),
        accuracy varchar(5)
    );
    ```

## Configuration

Update the MySQL database credentials in the script:
```python
mydb = mysql.connector.connect(host="localhost", user="root", password="YourPassword", database="MTCTyping")
