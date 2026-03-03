# Urban Air Quality Index Modeler
## SDG 11: Sustainable Cities and Communities


## 1. Introduction

Urban air pollution is a growing concern in rapidly developing cities, posing serious health and environmental challenges. Among various pollutants, fine particulate matter (PM2.5) is particularly harmful because it can penetrate deep into the lungs and bloodstream, leading to respiratory and cardiovascular problems.

Traffic congestion and meteorological conditions, such as wind speed, significantly influence PM2.5 concentration levels. Predicting PM2.5 levels using machine learning models can help city planners and policymakers take proactive measures to reduce pollution exposure and improve public health.

This project aims to develop a predictive regression model that estimates PM2.5 concentrations based on traffic volume and wind speed data. By identifying patterns and trends, the model supports data-driven urban planning and contributes toward achieving **SDG 11: Sustainable Cities and Communities**.


## 2. Problem Statement

To design and implement a predictive model capable of estimating PM2.5 concentration levels based on traffic volume and wind speed data, while incorporating temporal patterns through Hour-of-Day feature engineering.


## 3. Objectives

- Analyze the relationship between traffic volume, wind speed, and PM2.5 levels  
- Perform feature engineering by extracting Hour-of-Day from timestamp data  
- Train and evaluate regression models for PM2.5 prediction  
- Generate insights that support sustainable urban air quality management

## 1. Introduction
  Rapid urbanization, widespread industrialization, and a constant surge in vehicular emissions 
have collectively precipitated a severe deterioration in global air quality, with fine particulate 
matter (PM2.5) representing one of the most critical environmental health hazards. Because of 
their microscopic size, these particles can bypass the body's natural defensive mechanisms, 
penetrating deep into the respiratory system and even entering the bloodstream, which is directly 
linked to chronic respiratory conditions and cardiovascular diseases. Traditionally, environmental 
agencies have relied on physical monitoring stations that are inherently reactive, only alerting the 
public after hazardous conditions have already materialized. To effectively protect vulnerable 
populations and implement timely interventions, there is an urgent need to transition from 
reactive monitoring to proactive forecasting. Addressing this gap, this project leverages advanced 
machine learning techniques to develop a robust predictive model for PM2.5 concentrations 
using comprehensive historical datasets that encompass both air quality metrics (such as PM10, 
CO, NO₂, and SO₂) and localized meteorological factors (including temperature, pressure, wind 
speed, and humidity). Crucially, engineered temporal features specifically the Month and Hour 
of the day—are integrated into the dataset to capture cyclical environmental patterns, such as 
seasonal winter smog and diurnal peak-hour traffic emissions. The ultimate objective of this 
study is not only to achieve high predictive accuracy but also to ensure the model is practically 
accessible. Consequently, the optimized machine learning algorithm is integrated into a 
localized, interactive web application built with Streamlit. This interface allows end-users to 
input real-time environmental parameters and instantly visualize forecasted PM2.5 levels, 
bridging the gap between raw data science and a user-friendly deployment to provide a scalable, 
data-driven tool that directly supports sustainable urban management. 

## 2. Problem Statement  
Urban air pollution levels fluctuate significantly due to the complex interplay between traffic 
density, fluctuating weather patterns, and seasonal transitions. While modern monitoring systems 
are effective at providing real-time data, they often fall short in offering the predictive foresight 
necessary for proactive public health management. To bridge this gap, there is a critical need for 
a reliable machine learning-based system capable of accurately forecasting PM2.5 concentrations 
by capturing the intricate, non-linear relationships between various pollutants and atmospheric 
factors. By integrating these sophisticated modeling techniques into an accessible web platform 
such a system would empower stakeholders and the general public with actionable, real-time 
predictions to better navigate environmental risks.

## 3. Methodology  
1. Data Preprocessing and Analysis: Conduct thorough cleaning and exploratory data analysis 
(EDA) on air quality datasets to identify key trends and ensure data integrity. 
2. Model Development and Comparison: Implement and compare three distinct machine 
learning algorithms: Linear Regression, Random Forest, and XGBoost to determine the most 
effective approach for predicting PM2.5 levels. 
3. Model Performance Evaluation: Assess the accuracy and reliability of each model using 
standardized metrics, including Root Mean Square Error (RMSE), Mean Absolute Error (MAE), 
and R² score. 
4. Interactive Model Deployment: Develop and launch a real-time prediction interface using 
the Streamlit framework, allowing users to interact with the best-performing model. 
5. Support for Sustainable Urban Planning: Align the project outcomes with UN Sustainable 
Development Goal 11 to provide actionable insights for building safer, more resilient, and 
sustainable cities 

## 4. Model Development 
Algorithm Selection & Comparison 
To find the most accurate way to predict PM2.5 levels, we initially trained and evaluated three 
different machine learning algorithms: 
1. Linear Regression: Used as a baseline model to understand basic relationships in the data. 
2. Random Forest: Applied to capture non-linear patterns and complex interactions between 
variables. 
3. XGBoost: Tested for its advanced gradient boosting framework, which is highly 
optimized for tabular data. 
Performance Metrics 
We compared the models based on their Root Mean Square Error (RMSE), Mean Absolute Error 
(MAE), and R-squared (R²) scores: 
• Linear Regression: R² = 0.771 | MAE = 0.369 | RMSE = 0.479 
• Random Forest: R² = 0.861 | MAE = 0.265 | RMSE = 0.373 
• XGBoost: R² = 0.884 | MAE = 0.237 | RMSE = 0.341 
As the metrics show, XGBoost clearly outperformed the other two algorithms. It achieved the 
highest accuracy (explaining over 88% of the variance in PM2.5) while keeping the prediction 
errors (MAE and RMSE) to a minimum. 
Because it provided the best balance of high performance and reliability, we selected XGBoost 
as the final model for our real-time prediction system. Additionally, we plotted the model's 
Feature Importance to visualize exactly which input variables had the strongest impact on the 
final PM2.5 predictions.

## 5. Results 
1. Model Tuning & Performance  
During model development, multiple algorithms and hyperparameter configurations were tested. 
As shown in the table below, while a basic Random Forest (n_estimators=10) achieved good 
accuracy, it took significantly longer to train. XGBoost (n_estimators=300, depth=6) was 
selected as the final model because it offered the best trade-off: it matched the highest accuracy 
(R² ~ 0.88) and lowest error rates (RMSE ~ 0.34) while training in just ~5 seconds. 

2. Feature Importance Analysis  
To interpret the XGBoost model's predictions, feature importance scores were extracted. As 
illustrated in Figure X below, PM10 is the dominant predictor for PM2.5, followed by CO. 
Meteorological factors and engineered temporal features (month/hour) had minimal impact on 
the model's decision-making process.

## 6. SDG 11 Impact & Analysis 
This project directly supports the United Nations Sustainable Development Goal 11 (SDG 11), 
which aims to make cities and human settlements inclusive, safe, resilient, and sustainable. 
Specifically, the model aligns with Target 11.6, which emphasizes reducing the adverse per 
capita environmental impact of cities by paying special attention to air quality. 
The deployment of this real-time PM2.5 prediction system provides actionable value in the 
following ways: 
• Proactive Public Health Protection: By accurately forecasting PM2.5 spikes using the 
XGBoost model, the system serves as an early warning tool. This allows municipalities to 
issue timely health advisories, enabling vulnerable populations to take precautions and 
reducing respiratory-related hospitalizations. 
• Data-Driven Urban Policy: The feature importance analysis revealed that PM10 and CO 
are the dominant drivers of PM2.5 pollution. This precise insight empowers city planners 
and environmental agencies to move away from guesswork and target specific emission 
sources (like vehicular exhaust or industrial CO output) with strict, localized regulations. 
• Resource Optimization: Instead of reacting to pollution after it has blanketed a city, 
local governments can use these real-time predictions to implement temporary preventive 
measures such as rerouting traffic or pausing specific industrial activities only when the 
predictive model indicates a critical threshold will be breached.

## 7. Conclusion 
This study successfully developed and deployed a highly reliable machine learning pipeline for 
predicting PM2.5 air pollution levels. After rigorously evaluating Linear Regression, Random 
Forest, and XGBoost algorithms, XGBoost clearly emerged as the optimal solution. It 
demonstrated superior predictive reliability, successfully explaining approximately 88% of the 
variance in PM2.5 concentrations while maintaining the lowest error margins (RMSE of 0.34 
and MAE of 0.23). Furthermore, the feature importance analysis validated the model's scientific 
soundness by correctly identifying PM10 and Carbon Monoxide (CO) as the primary drivers of 
PM2.5 fluctuations. By successfully deploying this optimized model through an interactive 
Streamlit web application, this project proves that advanced machine learning can be effectively 
translated into a practical, real-time tool to monitor air quality and support sustainable urban 
environments.

## 8. References 
Data Source: https://www.kaggle.com/datasets/aravindpcoder/beijing-multi-site-air-quality-data
