# Diabetes-Predictor
Developed a diabetes prediction model for women using Support Vector Machine (SVM) as the underlying machine learning algorithm. This model effectively determines the likelihood of diabetes in women based on a set of input parameters. The dataset employed for training and validation originates from the National Institute of Diabetes and Digestive and Kidney Diseases, ensuring its reliability and accuracy. Furthermore, a user-friendly web application has  been designed which allows individuals to input their relevant parameters and obtain real-time predictions regarding their diabetes status.

 Here's the screenshot of the app
![Screenshot 2023-05-21 125310](https://github.com/Akash-kolladikkel/Diabetes-Predictor/assets/91449571/5f7bc77f-2297-4d68-85d0-e6eaccce27f3)

# Workflow of the Diabetes Prediction Code
1. Imporing dependancies: importing essential libraries and packages, including numpy, pandas, and scikit-learn (sklearn), to support data manipulation, preprocessing, and machine learning algorithms.

2. Data Collection: [diabetes.csv](https://github.com/Akash-kolladikkel/Diabetes-Predictor/files/11523935/diabetes.csv)
3. Data Preprocessing: preprocessing tasks were conducted,there were no duplicated or null values.Dataset was splitted into training and testing sets
4. Model Building: Implemented a machine learning model using Support Vector Machine (SVM) algorithm. Trained the model using the preprocessed dataset
5. Model Evaluation: Accuracy of both training and testing datas where evaluated along with r2-score
6. Saved and Loaded the Model: The trained SVM model was saved using Pickle to a file for later use. This allowed for easy loading of the pre-trained model without the need for retraining.
7. Web Application Development:  A simple user-friendly web application was developed using the streamlit library. The loaded SVM model was incorporated into the application to generate real-time predictions. The interface was designed to enable users to input their parameters and receive instant predictions.
