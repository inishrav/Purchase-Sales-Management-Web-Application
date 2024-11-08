# Namma Kadai Inventory Management System

Welcome to **Namma Kadai** – an inventory management system built using Flask and SQLAlchemy to manage items, purchases, and sales, as well as track cash balance in real time.

## Table of Contents

- [About the Project](#about-the-project)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Features](#features)


## About the Project

Namma Kadai is a web-based inventory management system designed to streamline the process of managing items, tracking purchases and sales, and viewing the current cash balance. This application provides a simple interface for small businesses to track their inventory.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **Flask-SQLAlchemy**: Provides a seamless way to integrate SQLAlchemy with Flask, making database interactions straightforward.
- **SQLite**: A lightweight relational database used to store application data.

## Getting Started

### Prerequisites

- **Python 3.x**
- **pip**: Python package installer

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/namma-kadai.git
    cd namma-kadai
    ```

2. Create a virtual environment:
    ```bash
    python -m venv myenv
    ```

3. Activate the virtual environment:
    - **Windows**:
      ```bash
      .\myenv\Scripts\Activate.ps1
      ```
    - **MacOS/Linux**:
      ```bash
      source myenv/bin/activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Initialize the database:
    ```python
    python
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

6. Run the Flask application:
    ```bash
    flask run
    ```

7. Open your browser and go to `http://127.0.0.1:5000` to access the application.

### Configuration

The application settings are stored in `config.py`. You can modify the `SQLALCHEMY_DATABASE_URI` to connect to a different database if desired.

## Features

- **Manage Items**: Add, edit, and delete items in the inventory.
- **Purchases**: Add purchase entries that increase item quantities and decrease the company's cash balance.
- **Sales**: Add sales entries that decrease item quantities and increase the company's cash balance.
- **Cash Balance Display**: Real-time cash balance updates based on purchases and sales.
- **Quick Links**: Navigate easily to manage items, purchases, and sales.
