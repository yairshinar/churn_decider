import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
churn_data = pd.DataFrame({
    'User': [f'User_{i}' for i in range(1, 101)],
    'DailyActiveTime': np.random.randint(0, 120, 100),
    'DaysSinceLastLogin': np.random.randint(0, 30, 100),
    'Purchases': np.random.randint(0, 10, 100),
    'ChurnProbability': np.random.uniform(0, 1, 100)
})

# Save to a CSV for use in the dashboard
churn_data.to_csv('data/churn_data.csv', index=False)
