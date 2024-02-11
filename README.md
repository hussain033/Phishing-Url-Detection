# Phishing Url Detection
Welcome to Phishing Url Detection Repository! This project focuses on the development of a machine learning model to accurately detect whether a URL is a Phishing Url or Legitimate Url. The project utilizes LGBM Classifier. The model achieves an impressive accuracy of about 80% on unseen data, making it a valuable resource for phishing url detection.

## Introduction

### Background
In an era where digital threats are constantly evolving, ensuring online security is of paramount importance. Phishing attacks, in particular, remain a pervasive threat, attempting to deceive users into divulging sensitive information by mimicking trustworthy websites. Recognizing the critical need for robust protection against phishing attempts, this project was initiated to develop an efficient and reliable phishing URL detection system.

### Motivation

The motivation behind this project stems from the increasing sophistication of phishing techniques and the potential harm they pose to individuals and organizations. Phishing URLs often appear as legitimate websites, making it challenging for users to discern the malicious intent behind them. By leveraging advanced detection algorithms and technologies, our goal is to empower users with a tool that can identify and mitigate the risks associated with phishing attacks.

### Project Objectives

1. **Accuracy:** Develop a phishing URL detection system with a high level of accuracy to minimize false positives and negatives.
   
2. **Ease of Integration:** Provide a solution that is easy to integrate into existing security infrastructures, enabling organizations to enhance their overall cybersecurity posture.

3. **Open Source Collaboration:** Foster collaboration within the open-source community, encouraging contributions and improvements to the detection mechanisms.

4. **User Education:** Accompany the tool with educational resources to raise awareness about phishing threats and empower users to make informed decisions when navigating the online landscape.

By addressing these objectives, we aim to contribute to a safer online environment for users and organizations alike. Your feedback and contributions are crucial in advancing the effectiveness of this phishing URL detection project.

## Methodology

### Data Collection

We have used a dataset of 4000 phishing URLs and 4000 benign URLs. The dataset 
was created by sampling URLs from the Phishtank website and then extracting 
features from the URLs using a Python script. The features that were extracted include 
the URL structure, the presence of certain keywords, and the use of suspicious 
characters.
This dataset can be used to train machine learning models that can classify URLs as 
phishing or benign. The models can then be used to identify phishing URLs in the 
wild.
Here are some of the key features of our dataset:
1. The dataset is balanced, with 4000 phishing URLs and 4000 benign URLs. This is 
important for training machine learning models, as it helps to ensure that the 
models are not biased towards one class or the other.
2. The dataset is relatively large, with 8000 URLs. This allows the machine learning 
models to learn more complex patterns in the data.
3. The dataset is diverse, with a variety of different features that can be used to 
classify URLs. This makes the models more robust and less likely to be tricked by 
phishing URLs that are not in the training data.

### Feature Extraction
To extract meaningful characteristics from the URLs, a Python script was employed. 
This script meticulously analyzed each URL, extracting features that can effectively 
distinguish between phishing and benign URLs.
Clustering and Dimentionaly reduction techniques are used to create new features from combination of high correlated features.

### Model Development
The machine learning model is developed on the Dataset created using LGBM Classifier Algorithm. LightGBM is a fast, distributed, high performance gradient boosting framework based on decision tree algorithms, used for ranking, classification and many other machine learning tasks. A gradient Boosting algorithm is based on ensemble learning where an ML model makes predictions based on n number of distinct models. From these models, this learning approach finds less biased and varied data points. It ensures that the successor decision tree will be better trained.

## Usage

### User Interface
To use the model in a user interface, check out our Hugging Face space,
[Phishing URL Detection](https://huggingface.co/spaces/Hussain033/Phishing-URL-Detection).
![image](https://github.com/hussain033/Phishing-Url-Detection/assets/83116894/deeb0c75-7b0c-4df6-9b98-6a4ef70aa9ad)



It is an easy to use interface, built with gradio and hosted Hugging Face platform. 

### Inference
To use the leaf image classification model for inference, follow these steps:

1. Cloning the repository: 
   ```
   git clone https://github.com/hussain033/Phishing-URL-Detection
   ```
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
4. Place your leaf image in the appropriate directory.
5. Run the inference script:
   ```
   python app.py url
   ```

### Experimentation
You can experiment with the model training of the project by replacing the LGBM Classifier model with any other  simple classification model such as Logistic Regression, Decision Tree, Random Forest or any ensemble based classification models such as XGBoost, Catboost to mention a few. 

We have provided the model training ipynb file, feel free to experiment with it by cloning the repo.

for Cloning the repo, use the following command:
``` 
git clone https://github.com/hussain033/Phishing-Url-Detection
```

## Results

The developed model achieves an accuracy rate of about 80% on unseen data. This high accuracy demonstrates the model's proficiency in detecting Phishing urls . 
