# SafeGuard AI Banking Transaction Fraud Detection

SafeGuard AI is a machine learning application designed to detect fraudulent banking transactions. It uses advanced algorithms to identify suspicious activities, generate detailed reports, and help financial institutions prevent fraud.

## Table des Matières

- [Features](#features)
- [Prerequisites](#Prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#Usage)
- [Project Structure](#project-structure)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Fraud Detection Pipeline** : Detects fraudulent transactions using machine learning models like Random Forest.
- **Database Support** : Connects to PostgreSQL or MySQL databases to retrieve transaction data.
- **Dynamic Field Management** : Configurable fields to adapt to different database schemas.
- **Report Generation** : Generates fraud detection reports in CSV or PDF format.
- **Modular Design** : Clear code structure with separate modules for data loading, model training, and fraud detection services.

---

## Prerequisites

- **Python 3.7 or higher**
- **pip** (Python package manager)
- **Git** (to clone the repository)
- **PostgreSQL** ou **MySQL** database with transaction data
- **Virtual Environment** (recommended)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/malekbig/SafeGuard_AI_Banking_Transaction.git
cd SafeGuard_AI_Banking_Transaction
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
```bash
python3 -m venv safeguard-env
```
###  3. Activate the Virtual Environment
On macOS/Linux:
```bash
source safeguard-env/bin/activate
```
On Windows:
```bash
safeguard-env\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration
Before running the application, you need to configure the database connection and other settings.

###  1. Créer un Fichier de Configuration
Create a configuration file named safeguard_ai_config.yml in the config/ directory.

```bash
mkdir config
touch config/safeguard_ai_config.yml
```
###  2.  Add Configuration Details
Fill in safeguard_ai_config.yml with your specific settings:
```yaml
database:
  type: postgresql  # or 'mysql'
  host: your-database-host
  port: 5432        # or 3306 for MySQL
  name: your-database-name
  user: your-username
  password: your-password
  schema: your-database-schema

table:
  name: transactions  # Name of the table containing transaction data

fields:
  transaction_id: transaction_id
  user_id: user_id
  amount: amount
  merchant: merchant
  location: location
  transaction_time: transaction_time
  user_frequency: user_frequency
  average_user_amount: average_user_amount
  last_transaction_location: last_transaction_location
  user_country: user_country
  transaction_country: transaction_country
  fraudulent: fraudulent

fraud_detection:
  report_format: csv      # 'csv' or 'pdf'
  report_output_path: reports/  # Directory where reports will be saved

```
Note: Ensure you replace the placeholders with your actual database and configuration information.

### 3.  Prepare the Database
 - Ensure your database is running and accessible.
 - Create the required tables using the provided SQL scripts (if applicable).
 - Insert sample data into your transactions table for testing.

## Usage
#### 1. Run the Application
With the virtual environment activated and the configuration in place, you can run the main script:

```bash
python main.py
```
#### 2. Results
The application will connect to your database, train the fraud detection model, and generate a report.
Reports will be saved in the directory specified in report_output_path (e.g., reports/).
#### 3. Logs
The console output will display the progress, including detected fraudulent transactions.

Check the generated report for detailed information.

## Project Structure

```bash
SafeGuard_AI_Banking_Transaction/
│
├── config/
│   └── safeguard_ai_config.yml          # Configuration file
│
├── data/
│   ├── __init__.py
│   ├── DataLoader.py                    # Loads data from the database
│   └── DatabaseConnector.py             # Manages database connections
│
├── models/
│   ├── __init__.py
│   └── ModelTrainer.py                  # Trains and evaluates ML models
│
├── services/
│   ├── __init__.py
│   └── SafeGuardTransactionService.py   # Detects fraud and generates reports
│
├── reports/                             # Generated reports (added to .gitignore)
│
├── main.py                              # Main execution script
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```
## Contribution

Contributions are welcome! Please follow these steps:

#### 1. Fork the repository to your own GitHub account.

#### 2. Clone the project to your machine:

```bash
git clone https://github.com/votre-utilisateur/SafeGuard_AI_Banking_Transaction.git
```
#### 3. Create a branch for your feature or bug fix:
```bash
git checkout -b feature/your-feature-name
```
#### 4. Commit your changes with clear messages:

```bash
git commit -am "Add a new feature"
```
#### 5. Push to your branch:
```bash
git push origin feature/your-feature-name
```
#### 6. Create a Pull Request on the original repository.

## Licence
This project is under the MIT License.

## Contact
For any questions or suggestions, please open an issue or contact the project maintainer.

Note: Disclaimer: This project is intended for educational purposes. Always ensure compliance with all applicable laws and regulations when handling financial data.

