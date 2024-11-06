# E-commerce Analytics Dashboard

## Overview
This project provides a comprehensive analytics dashboard for e-commerce data analysis, built using Python and Streamlit. It uses real-world data from the Brazilian E-commerce Public Dataset by Olist to create meaningful insights for merchants.

## Features
- Real-time sales analytics
- Interactive date range filtering
- Key performance metrics
- Daily sales trends visualization
- Top-performing product categories analysis
- Monthly sales heatmap
- Order status distribution

## Technologies Used
- Python 3.8+
- Streamlit
- Pandas
- Plotly
- Real e-commerce data from Olist

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ecommerce-analytics.git
cd ecommerce-analytics
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run main.py
```

## Requirements
Create a `requirements.txt` file with the following dependencies:
```
pandas>=1.3.0
streamlit>=1.12.0
plotly>=5.3.0
```

## Data Source
This project uses the Brazilian E-commerce Public Dataset by Olist, available on Kaggle. The dataset is automatically downloaded when running the application.

## Features in Detail

### 1. Sales Analytics
- Total sales calculation
- Number of orders
- Average order value
- Daily sales trends

### 2. Product Analysis
- Top-selling product categories
- Product category performance over time
- Monthly sales patterns

### 3. Order Status Tracking
- Distribution of order statuses
- Order fulfillment analysis

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Olist for providing the public dataset
- Streamlit for the excellent framework
- The open-source community for various tools and libraries used in this project
