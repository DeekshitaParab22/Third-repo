
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("best_xgboost_model.joblib")

st.title("Digital Marketing Campaign Conversion Prediction")

st.write(
    "Enter customer and campaign details to predict "
    "whether a customer is likely to convert."
)

# Customer details
st.header("Customer Details")

age = st.number_input(
    "Age", min_value=18, max_value=69, value=30
)

gender = st.selectbox("Gender", ["Female", "Male"])

income = st.number_input(
    "Income", min_value=20014, max_value=149986, value=50000
)

# Campaign details
st.header("Campaign Details")

campaign_channel = st.selectbox(
    "Campaign Channel",
    ["Email", "Social Media", "SEO", "PPC", "Referral"]
)

campaign_type = st.selectbox(
    "Campaign Type",
    ["Awareness", "Consideration", "Conversion", "Retention"]
)

ad_spend = st.number_input(
    "Ad Spend", min_value=100.05, max_value=9997.91, value=1000.0
)

click_through_rate = st.number_input(
    "Click Through Rate",
    min_value=0.01, max_value=0.30, value=0.15
)

conversion_rate = st.number_input(
    "Conversion Rate",
    min_value=0.01, max_value=0.20, value=0.10
)

# Customer engagement
st.header("Customer Engagement")

website_visits = st.number_input(
    "Website Visits", min_value=0, max_value=49, value=10
)

pages_per_visit = st.number_input(
    "Pages Per Visit", min_value=0.0, max_value=10.0, value=3.0
)

time_on_site = st.number_input(
    "Time on Site", min_value=0.0, max_value=15.0, value=5.0
)

social_shares = st.number_input(
    "Social Shares", min_value=0, max_value=99, value=5
)

email_opens = st.number_input(
    "Email Opens", min_value=0, max_value=19, value=5
)

email_clicks = st.number_input(
    "Email Clicks", min_value=0, max_value=9, value=2
)

# Customer history
st.header("Customer History")

previous_purchases = st.number_input(
    "Previous Purchases", min_value=0, max_value=9, value=2
)

loyalty_points = st.number_input(
    "Loyalty Points", min_value=0, max_value=4999, value=100
)

# Predict
if st.button("Predict Conversion"):
    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Income": income,
        "CampaignChannel": campaign_channel,
        "CampaignType": campaign_type,
        "AdSpend": ad_spend,
        "ClickThroughRate": click_through_rate,
        "ConversionRate": conversion_rate,
        "WebsiteVisits": website_visits,
        "PagesPerVisit": pages_per_visit,
        "TimeOnSite": time_on_site,
        "SocialShares": social_shares,
        "EmailOpens": email_opens,
        "EmailClicks": email_clicks,
        "PreviousPurchases": previous_purchases,
        "LoyaltyPoints": loyalty_points
    }])

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("The customer is predicted to convert.")
    else:
        st.warning("The customer is predicted not to convert.")
