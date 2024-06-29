## Turkish Fake News Detection 


 A fake news detector to check the accuracy of Turkish news text.

https://github.com/MelihUlular/TurkishFakeNewsDetection/assets/92888821/0dab5cda-5a66-4698-9310-11dfb229e9ee



## Folders 

1) Dataset Preparation : This file contains the code used to merge fake and real news files we found on Github(1) into Fake.csv and Real.csv. After these steps, our output dataset is news.csv. 

2) Dataset Preprocess : This file contains the code file containing the data cleaning steps. The news.csv file in the Input Data folder has turned into clean_news.csv file in the Output Data folder. Transformers models, Bow, Bow+TF-IDF, FastTEXT and Word2vec models applied in this study were created with the cleaned data (clean_news.csv).

3) Translated Dataset Using Google Trans API : In this study, the Google Trans API library was used. According to the model training results obtained, the translation dataset was extracted from the final version of the project called Fake News Detection. However, the relevant code and datasets are in this file.

4) Transformers : This file contains the relevant codes of 4 transformer models trained for this study. Clean_news.csv is used as dataset. There are 4 models trained in the Transformers file with .ipyn and .py extensions.

5) Bag of Word and Bag of Word + TF-IDF : This file contains the relevant code where Bag of Word and Bag of Word + TF-IDF techniques are applied on the cleaned news data.

6) FastText : This file contains the relevant code where the FastText technique is applied to the cleaned news data.

7) Word2vec : This file contains the relevant code where the Word2vec technique is applied to the cleaned news data.

8) Linguistic Regression : This file contains outputs new_linguistic_data by applying linguistic regression to news.csv file.

9) Feature Selection : This file contains the code for your implementation of feature selection to the new_linguistic_data dataset.

10) Fake News Detection GUI with Flask : This file contains the interface code created using Python Flask on top of the best result ConvBert transformers model.


## Data Files 

news.csv :  Main dataset used in this project and it contains a total of 4455 fake and real news data.

clean_news.csv : Data preprocessing of the main dataset used in this project and it contains a total of 4455 fake and real news data.

new_linguistic_data.csv : This dataset is a linguistic regression applied to the news.csv dataset.
