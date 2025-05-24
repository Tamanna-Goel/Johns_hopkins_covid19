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

Built a predictive model using ARIMA to forecast future COVID-19 trends globally. Used data from Johns Hopkins University and developed time-series plots, trend decomposition, and future predictions to support healthcare decision-making and policy insights. Included hyperparameter tuning for best results.
