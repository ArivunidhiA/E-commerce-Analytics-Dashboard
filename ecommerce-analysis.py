import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

# Load and process data
@st.cache_data
def load_data():
    # Load the datasets
    orders = pd.read_csv('https://raw.githubusercontent.com/olist/brazilian-ecommerce/master/olist_orders_dataset.csv')
    order_items = pd.read_csv('https://raw.githubusercontent.com/olist/brazilian-ecommerce/master/olist_order_items_dataset.csv')
    products = pd.read_csv('https://raw.githubusercontent.com/olist/brazilian-ecommerce/master/olist_products_dataset.csv')
    
    # Merge datasets
    df = orders.merge(order_items, on='order_id')
    df = df.merge(products[['product_id', 'product_category_name']], on='product_id')
    
    # Convert date columns
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    
    # Add date components
    df['year'] = df['order_purchase_timestamp'].dt.year
    df['month'] = df['order_purchase_timestamp'].dt.month
    df['date'] = df['order_purchase_timestamp'].dt.date
    
    return df

def main():
    st.set_page_config(page_title="E-commerce Analytics Dashboard", layout="wide")
    st.title("E-commerce Analytics Dashboard")
    
    # Load data
    df = load_data()
    
    # Date filter
    min_date = df['order_purchase_timestamp'].min().date()
    max_date = df['order_purchase_timestamp'].max().date()
    
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", min_date)
    with col2:
        end_date = st.date_input("End Date", max_date)
    
    # Filter data based on date range
    mask = (df['date'] >= start_date) & (df['date'] <= end_date)
    filtered_df = df[mask]
    
    # Key Metrics
    total_sales = filtered_df['price'].sum()
    total_orders = filtered_df['order_id'].nunique()
    avg_order_value = total_sales / total_orders
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${total_sales:,.2f}")
    col2.metric("Total Orders", f"{total_orders:,}")
    col3.metric("Average Order Value", f"${avg_order_value:.2f}")
    
    # Daily Sales Trend
    daily_sales = filtered_df.groupby('date')['price'].sum().reset_index()
    fig_daily = px.line(daily_sales, x='date', y='price',
                        title='Daily Sales Trend',
                        labels={'price': 'Sales ($)', 'date': 'Date'})
    st.plotly_chart(fig_daily, use_container_width=True)
    
    # Top Categories
    col1, col2 = st.columns(2)
    
    with col1:
        top_categories = filtered_df.groupby('product_category_name')['price'].sum()\
            .sort_values(ascending=True).tail(10)
        fig_categories = px.bar(top_categories, orientation='h',
                              title='Top 10 Categories by Sales',
                              labels={'value': 'Sales ($)', 'product_category_name': 'Category'})
        st.plotly_chart(fig_categories, use_container_width=True)
    
    with col2:
        # Monthly Sales Heatmap
        monthly_sales = filtered_df.pivot_table(
            index='year', 
            columns='month', 
            values='price', 
            aggfunc='sum'
        ).fillna(0)
        
        fig_heatmap = go.Figure(data=go.Heatmap(
            z=monthly_sales.values,
            x=monthly_sales.columns,
            y=monthly_sales.index,
            colorscale='Blues'
        ))
        
        fig_heatmap.update_layout(
            title='Monthly Sales Heatmap',
            xaxis_title='Month',
            yaxis_title='Year'
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # Order Status Distribution
    status_dist = filtered_df['order_status'].value_counts()
    fig_status = px.pie(values=status_dist.values, 
                       names=status_dist.index,
                       title='Order Status Distribution')
    st.plotly_chart(fig_status, use_container_width=True)

if __name__ == "__main__":
    main()
