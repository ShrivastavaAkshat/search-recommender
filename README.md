# Product Recommender System

This project implements a product recommender system using cosine similarity on product descriptions.

## Steps:

1. **Data Loading and Preprocessing:**
   - Load product data from 'Electronics.csv'.
   - Handle missing values and duplicates.
   - Extract keywords from product names, convert them to lowercase, and remove special characters.

2. **Text Preprocessing:**
   - Apply stemming to keywords using Porter Stemmer.

3. **Feature Vectorization:**
   - Convert text data into numerical feature vectors using CountVectorizer with a maximum of 5000 features and English stop words removal.

4. **Cosine Similarity Calculation:**
   - Compute the cosine similarity matrix between all pairs of product feature vectors.

5. **Recommendation Function:**
   - Define a function `recommender` that takes a product name as input and returns a list of similar products based on cosine similarity.

6. **Pickle:**
   - Save the similarity matrix and processed data using pickle.

7. **Streamlit UI:**
   - Created a UI using streamlit lib so that a user can search similar products.

## Project Setup:

1. **Create A Virtual Environment**

2. **Install Requirments.txt**

3. **Run Model.ipynb**
   - it will create a pkl dump file
4. **Run app.py**
   - use streamlit run app.py
## Project Screenshots:
   **Homepage**
   
   ![image](https://github.com/user-attachments/assets/e342da02-c596-42b6-b157-86044641ca48)
   
   **Product Search**
   
   ![image](https://github.com/user-attachments/assets/b76dcc58-e34d-4359-9111-e0163827f49a)
   
   **Earphones Search**
   
   ![image](https://github.com/user-attachments/assets/5577c0e5-01ec-41ca-92e7-fc66bf88e41b)
   
   **Searching Pen** 
   
  ![image](https://github.com/user-attachments/assets/8dd76dbe-37a5-4d55-bbbc-c051723af808)
  
   **Monitor Arm**
   
  ![image](https://github.com/user-attachments/assets/cf5216c5-26ee-4cc7-8f33-18acbba116ef)


