## SaaS Customer Churn Prediction
---

Predicting customer churn using classical machine learning models with business-aligned evaluation.
Live API: [docs](https://saas-customer-churn-prediction.onrender.com/docs)
---

**Overview**

This project uses historical customer account and service data to predict churn risk.  
The focus is not just accuracy, but identifying at-risk customers early enough to intervene.

---

**Models Evaluated**

- Logistic Regression  
- Decision Tree (depth-constrained)  
- Random Forest (tuned)  
- Gradient Boosting  

Final selection prioritized recall over raw accuracy.

---

**Final Model**

*Logistic Regression (threshold = 0.4)*
- Strong ranking ability (ROC-AUC ≈ 0.81)
- Improved recall after threshold adjustment
- Stable and interpretable compared to tree-based ensembles

---

**Business Framing**

False negatives (missed churners) are more costly than false positives.  
The classification threshold was lowered to increase recall so that potential churners do not become a blind spot in the system.



