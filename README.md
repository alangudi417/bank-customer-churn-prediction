# Beta Bank Customer Churn Prediction

## 📊 Project Overview
This project develops a Machine Learning classification model to predict whether a Beta Bank customer is likely to leave the bank. Customer retention is significantly more cost-effective than customer acquisition, making churn prediction a critical business objective.
Using historical customer behavior and contract termination data, multiple classification algorithms were trained and evaluated. The primary performance metric is the F1 score, with a project goal of achieving a minimum score of 0.59 on the test dataset. The final model successfully surpasses this threshold and provides actionable insights for customer retention strategies.

## 📊 Dataset Description
The dataset contains customer demographic and behavioral information, including:
- Customer demographics (Age, Geography, Gender)
- Banking activity metrics (Balance, Number of Products, Credit Score)
- Customer tenure and account activity
- Contract termination indicator (Exited – Target Variable)
The dataset is used to identify behavioral patterns associated with customer churn.

## ⚙️ Methodology
The project follows a structured machine learning workflow:
1. Data Analysis & Preprocessing
    - Removed non-predictive features:
        - RowNumber
        - CustomerId
        - Surname
    - Handled missing values in Tenure using median imputation
    - Performed feature engineering and data transformation
    - Split data into training and testing sets
    - Identified and addressed class imbalance:
        - Only 20.37% of customers had exited
        - Applied class balancing techniques to improve model performance

2. Model Development
- Three classification algorithms were evaluated:
    - Decision Tree Classifier
    - Logistic Regression
    - Random Forest Classifier
- Each model was tested under multiple balancing strategies:
    - Unbalanced dataset
    - Class-weight adjustment
    - Undersampling techniques

3. Model Evaluation
- Models were evaluated using:
    - F1 Score (Primary Metric)
    - ROC-AUC Score
    - Classification performance metrics (Precision and Recall)

# 📈 Project Highlights
- Addressed real-world class imbalance challenges
- Compared multiple machine learning classification algorithms
- Applied class weighting and sampling strategies
- Delivered a model exceeding the required performance threshold
- Generated actionable business retention insights

📈 Results
1.	Key Model Performance
Model	Best F1 Score	Performance Summary
Decision Tree	0.574	Below target threshold
Logistic Regression	0.489	Poor performance due to non-linear relationships
Random Forest	0.629	Best performing and selected final model

2.	Final Model Selection
The Random Forest Classifier with class_weight='balanced' was selected as the final model.
Performance Metrics:
- F1 Score: 0.629
- ROC-AUC Score: 0.757
These results demonstrate strong predictive capability and effective class separation.

💼 Business Impact
Customer Retention Strategy
The model enables Beta Bank to identify customers at risk of leaving with balanced precision and recall. This allows the bank to:
- Reduce revenue loss from churn
- Allocate retention resources more efficiently
- Improve customer lifetime value

Actionable Insights
By integrating churn prediction into operational workflows, Beta Bank can:
- Offer targeted incentives
- Provide personalized service improvements
- Implement proactive engagement strategies
This approach is significantly more effective than untargeted retention campaigns.

▶️ How to Run the Project
1.	Clone this repository: git clone https://github.com/alangudi417/bank-customer-churn-prediction.git
2.	Navigate to the project folder: cd bank-customer-churn-prediction
3.	Create and activate virtual environment: python -m venv venv venv\Scripts\activate # Windows source venv/bin/activate # Mac/Linux
4.	Install dependencies: pip install -r requirements.txt
5.	Launch Jupyter Notebook: jupyter notebook
6.	Open notebooks/bank_churn_pred.ipynb