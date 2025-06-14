import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations(data_path, output_dir):
    """
    Create visualization images from car data
    
    Parameters:
    data_path (str): Path to the data CSV file
    output_dir (str): Directory to save generated images
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read data
    df = pd.read_csv(data_path)
    
    # Configure plot styles
    sns.set(style="whitegrid")
    plt.rcParams.update({'font.size': 12})
    
    # 1. Distribution of car prices
    plt.figure(figsize=(10, 6))
    sns.histplot(df['selling_price'], kde=True, bins=30, color='#3b82f6')
    plt.title('Distribution of Car Prices', fontweight='bold')
    plt.xlabel('Price (₹)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'price_distribution.png'), dpi=300)
    plt.close()
    
    # 2. Price by fuel type (boxplot)
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='fuel', y='selling_price', data=df, palette='Blues')
    plt.title('Car Price Distribution by Fuel Type', fontweight='bold')
    plt.xlabel('Fuel Type')
    plt.ylabel('Price (₹)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'price_by_fuel_boxplot.png'), dpi=300)
    plt.close()
    
    # 3. Price by transmission type (violin plot)
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='transmission', y='selling_price', data=df, palette='Blues')
    plt.title('Car Price Distribution by Transmission Type', fontweight='bold')
    plt.xlabel('Transmission Type')
    plt.ylabel('Price (₹)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'price_by_transmission_violin.png'), dpi=300)
    plt.close()
    
    # 4. Price by seller type (barplot)
    plt.figure(figsize=(10, 6))
    seller_avg = df.groupby('seller_type')['selling_price'].mean().reset_index()
    sns.barplot(x='seller_type', y='selling_price', data=seller_avg, palette='Blues')
    plt.title('Average Price by Seller Type', fontweight='bold')
    plt.xlabel('Seller Type')
    plt.ylabel('Average Price (₹)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'price_by_seller_barplot.png'), dpi=300)
    plt.close()
    
    # 5. Price by owner (barplot)
    plt.figure(figsize=(12, 6))
    owner_avg = df.groupby('owner')['selling_price'].mean().reset_index()
    sns.barplot(x='owner', y='selling_price', data=owner_avg, palette='Blues')
    plt.title('Average Price by Owner Type', fontweight='bold')
    plt.xlabel('Owner Type')
    plt.ylabel('Average Price (₹)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'price_by_owner_barplot.png'), dpi=300)
    plt.close()
    
    # 6. Correlation between year and price (scatter plot with regression line)
    plt.figure(figsize=(10, 6))
    sns.regplot(x='year', y='selling_price', data=df, scatter_kws={'alpha':0.4}, line_kws={'color':'red'})
    plt.title('Car Price vs. Manufacturing Year', fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Price (₹)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'price_vs_year.png'), dpi=300)
    plt.close()
    
    # 7. Correlation between km_driven and price (scatter plot with regression line)
    plt.figure(figsize=(10, 6))
    sns.regplot(x='km_driven', y='selling_price', data=df, scatter_kws={'alpha':0.4}, line_kws={'color':'red'})
    plt.title('Car Price vs. Kilometers Driven', fontweight='bold')
    plt.xlabel('Kilometers Driven')
    plt.ylabel('Price (₹)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'price_vs_km.png'), dpi=300)
    plt.close()
    
    # 8. Heatmap of correlations between numerical features
    plt.figure(figsize=(10, 8))
    numerical_df = df.select_dtypes(include=['int64', 'float64'])
    corr = numerical_df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, annot=True, fmt='.2f')
    plt.title('Correlation Heatmap', fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'), dpi=300)
    plt.close()
    
    # 9. Price trends over years (line plot)
    plt.figure(figsize=(12, 6))
    year_price = df.groupby('year')['selling_price'].mean().reset_index()
    sns.lineplot(x='year', y='selling_price', data=year_price, marker='o', linewidth=2)
    plt.title('Average Car Price Trend by Year', fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Average Price (₹)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'price_trend_by_year.png'), dpi=300)
    plt.close()
    
    # 10. Count of cars by fuel type (countplot)
    plt.figure(figsize=(10, 6))
    sns.countplot(x='fuel', data=df, palette='Blues')
    plt.title('Number of Cars by Fuel Type', fontweight='bold')
    plt.xlabel('Fuel Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'car_count_by_fuel.png'), dpi=300)
    plt.close()

if __name__ == "__main__":
    data_path = os.path.join('artifacts', 'train.csv')
    output_dir = os.path.join('frontend', 'static', 'images', 'visualizations')
    create_visualizations(data_path, output_dir)
    print(f"Visualizations generated in {output_dir}")
