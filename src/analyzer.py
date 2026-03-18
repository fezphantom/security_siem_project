
import pandas as pd
from sklearn.ensemble import IsolationForest

def run_analysis(file_path):
    df = pd.read_csv(file_path)
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    df['is_night'] = ((df['hour'] < 6) | (df['hour'] > 22)).astype(int)

    df['failed_attempts'] = df.groupby('user')['status'].transform(
        lambda x: (x == 'failed').cumsum()
    )

    df['unique_ips'] = df.groupby('user')['ip'].transform('nunique')

    features = df[['hour', 'failed_attempts', 'unique_ips', 'is_night']]

    model = IsolationForest(contamination=0.05, random_state=42)
    df['anomaly'] = model.fit_predict(features)

    df['brute_force_flag'] = df['failed_attempts'] > 5
    df['night_login_flag'] = df['is_night'] == 1
    df['ip_risk_flag'] = df['unique_ips'] > 2

    df['risk_score'] = (
        df['brute_force_flag'] * 3 +
        df['night_login_flag'] * 2 +
        df['ip_risk_flag'] * 2 +
        (df['anomaly'] == -1) * 4
    )

    return df
