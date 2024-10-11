import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
import os

class SafeGuardTransactionService:
    """
    Service for fraud detection and report generation.

    Author: BERRAHAL Malek
    Date: 05/11/2024
    """
    def __init__(self, data_loader, model_trainer, config):
        self.data_loader = data_loader
        self.model_trainer = model_trainer
        self.fields = config['fields']
        self.report_format = config['fraud_detection']['report_format']
        self.report_output_path = config['fraud_detection']['report_output_path']

    def detect_fraud(self):
        """ Train the model and display the detected fraudulent transactions """
        data = self.data_loader.load_data()
        X, y = self.prepare_data(data)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        sm = SMOTE(random_state=42, k_neighbors=1)
        X_res, y_res = sm.fit_resample(X_train, y_train)
        self.model_trainer.train(X_res, y_res)
        y_pred = self.model_trainer.predict(X_test)
        self.model_trainer.evaluate(y_test, y_pred)
        fraud_indices = [i for i, pred in enumerate(y_pred) if pred == 1]
        fraud_transactions = data.iloc[fraud_indices]
        if not fraud_transactions.empty:
            print("\nDetected fraudulent transactions :")
            for index, row in fraud_transactions.iterrows():
                print(f"Transaction ID: {row[self.fields['transaction_id']]}, User ID: {row[self.fields['user_id']]}")

            self.generate_report(fraud_transactions)
        else:
            print("Aucune transaction frauduleuse détectée.")

    def prepare_data(self, data):
        """ No fraudulent transactions detected. """
        data['transaction_hour'] = pd.to_datetime(data[self.fields['transaction_time']]).dt.hour
        data['transaction_day'] = pd.to_datetime(data[self.fields['transaction_time']]).dt.weekday
        data['foreign_transaction'] = data['user_country'] != data['transaction_country']
        data['deviation_from_avg'] = abs(data[self.fields['amount']] - data[self.fields['average_user_amount']]) / data[self.fields['average_user_amount']]
        data['recent_transaction_count'] = data.groupby(self.fields['user_id'])[self.fields['transaction_id']].transform('count')

        data.fillna(0, inplace=True)
        X = data[[self.fields['amount'], self.fields['merchant'], self.fields['location'], self.fields['user_frequency'],
                  'transaction_hour', 'transaction_day', 'deviation_from_avg', 'recent_transaction_count', 'foreign_transaction']]
        y = data['fraudulent']

        X = pd.get_dummies(X, columns=[self.fields['merchant'], self.fields['location']], drop_first=True)
        return X, y

    def generate_report(self, fraud_transactions):
        """ Generate a report of the detected fraudulent transactions """
        if not os.path.exists(self.report_output_path):
            os.makedirs(self.report_output_path)

        if self.report_format == "csv":
            filename = os.path.join(self.report_output_path, "fraud_report.csv")
            fraud_transactions.to_csv(filename, index=False)
            print(f"Fraud report saved under {filename}.")
        elif self.report_format == "pdf":
            filename = os.path.join(self.report_output_path, "fraud_report.pdf")
            self.generate_pdf_report(fraud_transactions, filename)
            print(f"Fraud report saved under {filename}.")
        else:
            print("Unsupported report format.")

    def generate_pdf_report(self, fraud_transactions, filename):
        """ Generate a PDF report for the fraudulent transactions """
        from fpdf import FPDF

        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Fraudulent Transactions Report", ln=True, align='C')

        for index, row in fraud_transactions.iterrows():
            text = f"Transaction ID: {row[self.fields['transaction_id']]}, User ID: {row[self.fields['user_id']]}"
            pdf.cell(200, 10, txt=text, ln=True, align='L')

        pdf.output(filename)
