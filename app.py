from flask import Flask, render_template, send_file,jsonify
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)
churn_data = pd.read_csv('data/churn_data.csv')
# Load data
may_kpi = pd.read_csv('data/may_kpi.csv')
ab_test_summary = pd.read_csv('data/ab_test_summary.csv')

@app.route('/')
def health_check():
    return jsonify({"status": "healthy flask"}), 200

@app.route('/flask')
def index():
    # KPI Visualizations
    may_kpi_chart = px.bar(
        may_kpi, x='tier_id', y='Revenue', color='Platform',
        title='Revenue by Tier and Platform'
    ).to_json()

    ab_test_chart = px.pie(
        ab_test_summary, names='SegmentGroup', values='NetRevenue',
        title='Net Revenue Distribution - A/B Test'
    ).to_json()

    churn_chart = px.scatter(
        churn_data,
        x='DailyActiveTime',
        y='ChurnProbability',
        size='Purchases',
        color='DaysSinceLastLogin',
        title='Churn Prediction Visualization',
        labels={
            'DailyActiveTime': 'Daily Active Time (min)',
            'ChurnProbability': 'Churn Probability',
            'DaysSinceLastLogin': 'Days Since Last Login'
        }
    ).to_json()
 
    return render_template(
        'index.html',
        may_kpi_chart=may_kpi_chart,
        ab_test_chart=ab_test_chart,
        churn_chart=churn_chart
    )

@app.route('/flask/questions')
def questions():
    return render_template('questions.html')

@app.route('/flask/ab_test_analysis')
def ab_test_analysis():
    return render_template('ab_test_analysis.html')

@app.route('/flask/forecasting')
def forecasting():
    return render_template('forecasting.html')

@app.route('/flask/download/<filename>')
def download(filename):
    filepath = os.path.join('data', filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
