# 📊 Financial Health Assessment Tool

## Problem Statement
Small and medium enterprises (SMEs) often struggle to understand their financial health due to a lack of analytical tools and financial expertise. There is a need for a simple, intelligent system that can analyze basic financial data and provide meaningful insights for better decision-making.

## Solution Overview
The Financial Health Assessment Tool is a web-based application that allows users to upload financial data in CSV format and instantly receive:
- Key financial metrics
- Visual analysis of revenue and expenses
- AI-driven business insights

This solution is designed to be simple, fast, and accessible for non-finance users.

## Key Features
- CSV-based financial data upload  
- Automatic calculation of revenue, expenses, profit, and profit margin  
- Financial health classification (Strong / Moderate / Weak)  
- Visual representation of revenue vs expenses  
- AI-driven recommendations for business improvement  

## Tech Stack
- **Frontend & UI:** Streamlit  
- **Backend & Logic:** Python  
- **Data Processing:** Pandas  
- **Visualization:** Matplotlib  

## Folder Structure
```text
financial-health-tool/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── sample_financial_data.csv
│
├── utils/
│   ├── __init__.py
│   ├── data_processing.py
│   └── insights.py
│
└── assets/
    └── screenshots/

## How to Run the Application
1. Install Python (3.10 or above)
2. Install dependencies:
pip install -r requirements.txt
3. Run the app:
streamlit run app.py
4. Open browser and go to:
http://localhost:8501

## Sample Input
A sample CSV file is provided with the following columns:
- Month
- Revenue
- Expenses
- Loan

## Output
- Financial summary with metrics
- Revenue vs Expenses line chart
- AI-generated financial insights

## Use Case
This tool can be used by:
- Small business owners
- Startup founders
- Financial analysts
- Students and early-stage entrepreneurs

## Conclusion
The Financial Health Assessment Tool demonstrates how AI-powered analytics can simplify financial decision-making for SMEs by providing quick, visual, and actionable insights.
💾 Save the file.