from collections import OrderedDict
import pandas as pd
from pathlib import Path

attributes_and_values = OrderedDict({
    "existing_checking_account_status": {
        "A11": "< 0",
        "A12": "[0, 200)",
        "A13": ">= 200",
        "A14": "no checking account"
    },
    "duration": None,
    "credit_history": {
        "A30": "no credits taken / all credits paid back duly",
        "A31": "all credits at this bank paid back duly",
        "A32": "existing credits paid back duly till now",
        "A33": "delay in paying off in the past",
        "A34": "critical account / other credits existing (not at this bank)"
    },
    "purpose": {
        "A40": "car (new)",
        "A41": "car (used)",
        "A42": "furniture/equipment",
        "A43": "radio/television",
        "A44": "domestic appliances",
        "A45": "repairs",
        "A46": "education",
        "A47": "(vacation - does not exist?)",
        "A48": "retraining",
        "A49": "business",
        "A410": "others"
    },
    "credit_amount": None,
    "savings_account_or_bonds": {
        "A61": "< 100",
        "A62": "[100, 500]",
        "A63": "[500, 1000)",
        "A64": ">= 1000",
        "A65": "unknown/no savings account"
    },
    "present_employment_since": {
        "A71": "unemployed",
        "A72": "< 1",
        "A73": "[1, 4)",
        "A74": "[4, 7)",
        "A75": "> 7"
    },
    "installment_rate_in_percentage_of_disposable_income": None,
    "personal_status_and_sex": {
        "A91": "male : divorced / separated",
        "A92": "female : divorced / separated / married",
        "A93": "male : single",
        "A94": "male : married / widowed",
        "A95": "female : single"
    },
    "other_debtors_or_guarantors":{
        "A101": "none",
        "A102": "co-applicant",
        "A103": "guarantor"
    },
    "present_residence_since": None,
    "property": {
        "A121": "real estate",
        "A122": "building society savings agreement / life insurance",
        "A123": "car or other, not in attribute 6",
        "A124": "unknown / no property"
    },
    "age": None,
    "other_installment_plans": {
        "A141": "bank",
        "A142": "stores",
        "A143": "none"
    },
    "housing":{
        "A151": "rent",
        "A152": "own",
        "A153": "for free"
    },
    "number_of_existing_credits_at_this_bank": None,
    "job": {
        "A171": "unemployed / unskilled - non-resident",
        "A172": "unskilled - resident",
        "A173": "skilled employee / official",
        "A174": "management / self-employed / highly qualified employee / officer"
    },
    "number_of_people_being_liable_to_provide_maintenance_for": None,
    "telephone": {
        "A191": "none",
        "A192": "yes, registered under the customers name"
    },
    "foreign_worker": {
        "A201": "yes",
        "A202": "no"
    },
    'credit_rating': {
        1: 'good',
        2: 'bad'
    }
})

if __name__ == '__main__':
    data_dir = Path(__file__).parent / 'data' # change this if needed
    df = pd.read_csv(data_dir / 'german.data', sep=' ', names=list(attributes_and_values.keys()))
    for col in df:
        if attributes_and_values[col]:
            df[col] = df[col].map(attributes_and_values[col], na_action='ignore')
    df.to_json(data_dir / 'german_credit_rating.ndjson', orient='records', lines=True)
