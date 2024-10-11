# -*- coding: utf-8 -*-
"""
SafeGuard AI Banking Transaction Fraud Detection
Author: BERRAHAL Malek
Date: 05/11/2024
Description: Main script for running the application.
"""

import yaml

from data.DataLoader import DataLoader
from models.ModelTrainer import ModelTrainer
from services.SafeGuardTransactionService import SafeGuardTransactionService
from sklearn.ensemble import RandomForestClassifier

with open('config/safeguard_ai_config.yml', 'r') as file:
    config = yaml.safe_load(file)
data_loader = DataLoader(config)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model_trainer = ModelTrainer(model)
safeguard_service = SafeGuardTransactionService(data_loader, model_trainer, config)
print("Fraud detection in historical data:")
safeguard_service.detect_fraud()
