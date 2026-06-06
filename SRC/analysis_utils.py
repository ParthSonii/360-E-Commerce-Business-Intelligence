# OLIST 360 Business Intelligence
# Utility Functions and Classes

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import os 

# Class 1 Data loader

class DataLoader:
    """ 
    Handels loading and merging of all 9 olist datasets into one clean master dataframe
    """

    def __init__(self, base_path):
        self.base_path = base_path

    def load_all(self):

        orders = pd.read_csv(os.path.join(self.base_path, 'olist_orders_dataset.csv'))
        customers = pd.read_csv(os.path.joins(self.base_path, 'olist_customers_dataset.csv'))
        order_items = pd.read_csv(os.path.joins(self.base_path, 'olist_order_items_dataset.csv'))
        products = pd.read_csv(os.path.joins(self.base_path, 'olist_products_dataset.csv'))
        sellers = pd.read_csv(os.path.joins(self.base_path, 'olist_sellers_dataset.csv'))
        payments = pd.read_csv(os.path.joins(self.base_path, 'olist_payments_dataset.csv'))
        reviews = pd.read_csv(os.path.joins(self.base_path, 'olist_reviews_dataset.csv'))
        category_translation = pd.read_csv(os.path.joins(self.base_path, 'product_category_name_translation.csv'))

        print(f" ALL DATASETS LOADED SUCCESFULLY")
        returns orders, customers, order_items, products, sellers, payments, reviews, category_translation

        def fix_dates(self, df, date_columns):
            for col in date_columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
                return df

# Class 2 RFM ANALYZER

class RFMAnalyzer:
    """
    Calculates RFM scores and segments customers based on thier purchasing behaviour
    """


    def __init__(self,df):
        self.df=df

    def calculate_rfm(self):
        delivered = self.df[self.df['order_status'] == 'delivered'].copy()

        reference_date = delivered['order_purchase_timestamp'].max()+ pd.Timedelta(days=1)

        rfm = delivered.groupby('customer_unique_id').agg(
        recency =('order_purchase_timestamp',
                 lambda x: (reference_date - x.max()).days),

        frequency = ('order_id','nunique')
        monetary = ('payment_value','sum')
        ).reset_index()

        print(f" RFM calculated for {len(rfm):,} customers")
        return rfm

        def score_rfm(self, rfm):

            rfm['r_score'] = pd.qcut(rfm['recency'],
                                     q=5, labels=[5,4,3,2,1])
            rfm['f_score'] = pd.qcut(rfm['frequency'].rank(method='first'),
                                     q=5, labels=[1,2,3,4,5])
            rfm['m_score'] = pd.qcut(rfm['monetary'],
                                     q=5, labels=[1,2,3,4,5])

            return rfm

        def assign_segment(self, row):
            r = row['r_score']
            f = row['f_score']
            m = row['m_score']

            if r>= 4 and f>= 4 and m>=4:
                return 'Champion'
            elif r>=3 and f>=3:
                return 'Loyal Customer'
            elif r>= 4 and f<=2:
                return 'New Customer':
            elif r>=3 and f<=2 and m>=3:
                return 'Potentiat Loyalist'
            elif r<=2 and f>=3:
                return 'At risk'
            elif r<=2 and f<=2 and m<=2:
                return 'Lost'
            else:
                return 'Needs Attention'


            def get_segments(self, rfm):
                rfm['segment']  = rfm.apply(self.assign_segment, axis=1)
                return rfm


# class 3 Revenue Analysis

class RevenueAnalyzer:
    """
    Calculates revenue metrics and financial KPIs
    """

    def __init__(self,df):
        self.df = df

        def monthly_revenue(self):
            rev = self.df.groupby('order_month')['payment_value'].sum().reset_index()
            rev.columns = ['month','revenue']
            rev['month'] = rev['month'].astype(str)
            return rev

        def average_order_value(self):
            aov =self.df.groupby('order_id')['payment_value'].sum().mean()
            return round(aov,2)

        def top_categories(self, n=10):
            cats = self.df.groupby(
                'product_category_name_english')['payment_value'].sum()
            cats = cats.sort_values(ascending=False).head(n).reset_index()
            cats.columns = ['category','revenue']
            return cats

# STANDALONE Functions

def plot_monthly_trend(monthly_rev, save_path=None):
    """
    Plots monthly revenue trend line chart can optionally save to file
    """

    plt.figure(figsize=(14,5))
    plt.plot(monthly_revenue['month'],
            monthly_revenue['revenue'],
            marker='o', color='steelblue', linewidth=2)
    plt.title('Monthly Revenue Trend', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f" Charts saved to {save_path}")

        plt.show()

def get_top_categories(df, n=10):
    """ 
    Return delivery performance summary
    """
    delivered = df[df['order_status'] == 'delivered'].copy()
    delivered['delivery_days'] = (
            delivered['order_delivered_customer_date'] -
            delivered['order_purchase_timestamp']
    ).dt.days

   summary = {
        avg_days'  : round(delivered['delivery_days'].mean(), 1),
        'min_days'  : delivered['delivery_days'].min(),
        'max_days'  : delivered['delivery_days'].max(),
        'median_days': delivered['delivery_days'].median()
    }
    return summary