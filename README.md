📈 COVID-19 Trend Forecasting

🔧 Tools: Python, ARIMA, Pandas, NumPy

📉 Model Type: Time-Series Forecasting

📊 R² Score: 0.82

Challenges Faced and Solutions
 - Data Quality Issues
   - Missing Values in Province/State Column
   - Handling Large Dataset with Numerous Features
   - Unpivoting the Data
   - Time Series Forecasting with ARIMA Model
   - Performance Evaluation of Predictive Models
 - Model Performance
   - Feature selection techniques were used to reduce the dimensionality of the data
   - The data was unpivoted to transform it into a long format, which is better suited for time series analysis
   - The ARIMA model was selected, and careful parameter tuning was performed to ensure that the best fit for the data was achieved
   - Feature selection was used to avoid overfitting

Built a predictive model using ARIMA to forecast future COVID-19 trends globally. Used data from Johns Hopkins University and developed time-series plots, trend decomposition, and future predictions to support healthcare decision-making and policy insights. Included hyperparameter tuning for best results. The analysis of the Johns Hopkins University COVID-19 dataset highlighted global trends in cases, deaths, and recoveries. By cleaning and transforming the data, we applied the ARIMA model for time series forecasting, achieving good accuracy with an R-squared value of 0.82. Challenges like missing values, large feature sets, and data unpivoting were addressed through feature selection, log transformations, and focusing on relevant data. The findings, including daily trends and forecasts, provide valuable insights for managing the pandemic. The analysis emphasizes the role of predictive models in planning for future healthcare needs and responding to ongoing COVID-19 developments.
