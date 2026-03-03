# IIMSTC-Cohort10-Urban-AQI-Modeler
Predicting PM2.5 concentration levels for SDG 11 using traffic and wind data. Includes Hour of Day feature engineering for peak pattern regression.

## 🎯 Project Objective
[span_3](start_span)To predict **PM2.5 concentration levels** based on traffic volume and wind speed, specifically focusing on **SDG 11: Sustainable Cities and Communities**[span_3](end_span). 

## [span_4](start_span)👥 Team Roles & Accountability[span_4](end_span)
* **[span_5](start_span)President:** Priyaguna R - Project Manager & GitHub Admin[span_5](end_span).
* **[span_6](start_span)Vice President:** Tamirahsharieff - Operations & Time Log Manager[span_6](end_span).
* **[span_7](start_span)Secretary:** Kashish - Documentation & Meeting Lead[span_7](end_span).
* **[span_8](start_span)Vice Secretary:** Lasya T P - QA & SDG Impact Analyst[span_8](end_span).
* **[span_9](start_span)[span_10](start_span)Data Engineers (4):** Data cleaning, feature engineering (Hour of Day)[span_9](end_span)[span_10](end_span).
* **[span_11](start_span)[span_12](start_span)Model Specialists (4):** Regression model training and tuning[span_11](end_span)[span_12](end_span).
* **[span_13](start_span)[span_14](start_span)Documentation Leads (4):** Weekly reports and GitHub commit verification[span_13](end_span)[span_14](end_span).

## 📈 Technical Scope
* **Target Variable:** PM2.5 Concentration.
* **Features:** Traffic Volume, Wind Speed, Hour of Day (Extracted from Timestamps).
* **Goal:** Capture peak traffic patterns to improve regression accuracy.

## 🔄 Model Training & Deployment
The `deployment/train_fixed_model.py` script encapsulates the entire model training workflow:

1. **Data source**: `../cleaned_air_quality_data (1) (1).csv`
2. **Features**: `['PM10','SO2','NO2','CO','O3','TEMP','PRES','DEWP','RAIN','WSPM','month','hour']`
3. **Run training**:
   ```bash
   cd deployment
   python train_fixed_model.py
   ```
   This produces `pm25_xgb_model.pkl` and `feature_names.pkl` in the `deployment/` folder.
4. **Push to repo**: commit the new pickles and training script to the `deployment` branch (or whichever branch holds the Streamlit app). Your fork is already configured as `fork`; simply:
   ```bash
   git add deployment/pm25_xgb_model.pkl deployment/feature_names.pkl deployment/train_fixed_model.py
   git commit -m "retrain model vX" 
   git push origin deployment        # update upstream
   git push fork deployment          # update your fork
   ```

The app (both root `app.py` and `deployment/app.py`) load the XGB pickle file relative to their location, so keeping the model in `deployment/` ensures the cloud deployment works correctly.

> 💡 Tip: when you change the list of features or model hyperparameters, update the script accordingly and rerun the training step.

## [span_15](start_span)[span_16](start_span)📅 Operational Rules[span_15](end_span)[span_16](end_span)
* **[span_17](start_span)Daily Commitment:** 4–5 hours per member logged in the weekly report[span_17](end_span).
* **[span_18](start_span)Daily Sync:** 1-hour mandatory discussion (Discord/Google Meet)[span_18](end_span).
* **[span_19](start_span)Submission:** Final report due by Tuesday EOD[span_19](end_span).
*

