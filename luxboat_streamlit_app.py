"""
LuxBoat Due Date Calculator - Streamlit App
============================================

This app allows users to upload production data and calculate due dates
with specified confidence levels.

To run this app:
1. Save this file as 'luxboat_app.py'
2. Install streamlit: pip install streamlit
3. Run: streamlit run luxboat_app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="LuxBoat Due Date Calculator",
    page_icon="🚤",
    layout="wide"
)

# Title and description
st.title("🚤 LuxBoat Due Date Calculator")
st.markdown("""
This app calculates reliable due dates for boat production orders based on 
historical throughput data and desired confidence levels.
""")

# Sidebar for inputs
st.sidebar.header("Input Parameters")

# Function to calculate due date
def calculate_due_date(inter_throughput_times, boats_needed, confidence_level):
    """
    Calculate due date with specified confidence level.
    
    Parameters:
    -----------
    inter_throughput_times : list
        List of inter-throughput times in hours
    boats_needed : int
        Number of boats to produce
    confidence_level : float
        Confidence level (e.g., 0.90 for 90%)
    
    Returns:
    --------
    dict : Dictionary with all calculation results
    """
    # Basic statistics
    X_bar = np.mean(inter_throughput_times)
    S_squared = np.var(inter_throughput_times, ddof=1)
    S = np.std(inter_throughput_times, ddof=1)
    
    # Lag-1 autocorrelation
    series_1 = inter_throughput_times[:-1]
    series_2 = inter_throughput_times[1:]
    rho_1 = np.corrcoef(series_1, series_2)[0, 1]
    
    # Calculate parameters
    mu_b = boats_needed * X_bar
    variance_multiplier = (1 + rho_1) / (1 - rho_1)
    sigma_squared_b = variance_multiplier * boats_needed * S_squared
    sigma_b = np.sqrt(sigma_squared_b)
    
    # Calculate due date
    z_alpha = stats.norm.ppf(confidence_level)
    T_due_hours = mu_b + z_alpha * sigma_b
    T_due_days = T_due_hours / 24
    
    # Safety time
    safety_time_days = (T_due_hours - mu_b) / 24
    average_time_days = mu_b / 24
    
    return {
        'mean': X_bar,
        'std': S,
        'variance': S_squared,
        'autocorrelation': rho_1,
        'mu_b': mu_b,
        'sigma_b': sigma_b,
        'z_score': z_alpha,
        'due_date_hours': T_due_hours,
        'due_date_days': T_due_days,
        'safety_time_days': safety_time_days,
        'average_time_days': average_time_days
    }

# Data input method selection
data_input_method = st.sidebar.radio(
    "How would you like to input data?",
    ["Use Example Data", "Upload CSV File", "Enter Manually"]
)

# Initialize data
inter_throughput_times = None

if data_input_method == "Use Example Data":
    st.sidebar.info("Using the LuxBoat case study data")
    # Example data from the case
    inter_throughput_times = [
        32.5, 35.5, 40, 38.5, 29.5, 37, 40, 49, 44,
        33.5, 44, 37.5, 47, 49, 45, 37.5, 30, 32, 34.5,
        34, 51, 48, 41.5, 39.5, 36, 31, 36, 41, 34
    ]
    
elif data_input_method == "Upload CSV File":
    st.sidebar.markdown("""
    **CSV Format:** Single column with header 'inter_throughput_time'
    
    Example:
    ```
    inter_throughput_time
    32.5
    35.5
    40.0
    ```
    """)
    
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if 'inter_throughput_time' in df.columns:
                inter_throughput_times = df['inter_throughput_time'].tolist()
                st.sidebar.success(f"✓ Loaded {len(inter_throughput_times)} data points")
            else:
                st.sidebar.error("CSV must have a column named 'inter_throughput_time'")
        except Exception as e:
            st.sidebar.error(f"Error reading file: {e}")
            
elif data_input_method == "Enter Manually":
    st.sidebar.markdown("Enter inter-throughput times separated by commas:")
    manual_input = st.sidebar.text_area(
        "Times (in hours)",
        "32.5, 35.5, 40, 38.5, 29.5",
        height=100
    )
    
    if manual_input:
        try:
            inter_throughput_times = [float(x.strip()) for x in manual_input.split(',')]
            st.sidebar.success(f"✓ Parsed {len(inter_throughput_times)} values")
        except ValueError:
            st.sidebar.error("Please enter valid numbers separated by commas")

# Other inputs
if inter_throughput_times:
    boats_needed = st.sidebar.number_input(
        "Number of boats needed",
        min_value=1,
        max_value=100,
        value=25,
        step=1
    )
    
    confidence_level = st.sidebar.slider(
        "Confidence Level (%)",
        min_value=50,
        max_value=99,
        value=90,
        step=1
    ) / 100

# Main content
if inter_throughput_times and len(inter_throughput_times) >= 2:
    
    # Calculate results
    results = calculate_due_date(inter_throughput_times, boats_needed, confidence_level)
    
    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Results", 
        "📈 Visualizations", 
        "📋 Statistics", 
        "❓ Help"
    ])
    
    with tab1:
        st.header("Due Date Calculation Results")
        
        # Main results in columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="Due Date",
                value=f"{results['due_date_days']:.1f} days",
                delta=f"{confidence_level*100:.0f}% confidence"
            )
        
        with col2:
            st.metric(
                label="Average Time",
                value=f"{results['average_time_days']:.1f} days",
                delta="50% confidence"
            )
        
        with col3:
            st.metric(
                label="Safety Time",
                value=f"{results['safety_time_days']:.1f} days",
                delta=f"+{(results['safety_time_days']/results['average_time_days']*100):.1f}%"
            )
        
        st.markdown("---")
        
        # Detailed breakdown
        st.subheader("Calculation Breakdown")
        
        breakdown_df = pd.DataFrame({
            'Parameter': [
                'Number of boats needed',
                'Mean inter-throughput time',
                'Standard deviation',
                'Autocorrelation (ρ₁)',
                'Expected time (μ_b)',
                'Standard deviation (σ_b)',
                'Z-score',
                'Due date'
            ],
            'Value': [
                f"{boats_needed}",
                f"{results['mean']:.2f} hours",
                f"{results['std']:.2f} hours",
                f"{results['autocorrelation']:.3f}",
                f"{results['mu_b']:.1f} hours ({results['average_time_days']:.1f} days)",
                f"{results['sigma_b']:.2f} hours",
                f"{results['z_score']:.2f}",
                f"{results['due_date_hours']:.1f} hours ({results['due_date_days']:.1f} days)"
            ]
        })
        
        st.table(breakdown_df)
        
        # Interpretation
        st.info(f"""
        **Interpretation:** With {confidence_level*100:.0f}% confidence, the order of {boats_needed} boats 
        will be completed within {results['due_date_days']:.1f} days. This includes 
        {results['safety_time_days']:.1f} days of safety time to account for variability 
        and autocorrelation in production times.
        """)
    
    with tab2:
        st.header("Data Visualizations")
        
        # Histogram
        st.subheader("Distribution of Inter-Throughput Times")
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.hist(inter_throughput_times, bins=15, edgecolor='black', alpha=0.7, color='steelblue')
        ax1.axvline(results['mean'], color='red', linestyle='--', linewidth=2, 
                    label=f"Mean: {results['mean']:.1f} hrs")
        ax1.set_xlabel('Inter-Throughput Time (hours)')
        ax1.set_ylabel('Frequency')
        ax1.set_title('Distribution of Inter-Throughput Times')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        st.pyplot(fig1)
        
        # Normal distribution
        st.subheader("Confidence Interval Visualization")
        time_range = np.linspace(
            results['mu_b'] - 4*results['sigma_b'], 
            results['mu_b'] + 4*results['sigma_b'], 
            1000
        )
        pdf = stats.norm.pdf(time_range, results['mu_b'], results['sigma_b'])
        
        fig2, ax2 = plt.subplots(figsize=(12, 6))
        ax2.plot(time_range, pdf, 'b-', linewidth=2, label='Distribution')
        
        # Shade confidence area
        x_fill = time_range[time_range <= results['due_date_hours']]
        y_fill = stats.norm.pdf(x_fill, results['mu_b'], results['sigma_b'])
        ax2.fill_between(x_fill, y_fill, alpha=0.3, color='green', 
                         label=f'{confidence_level*100:.0f}% confidence')
        
        # Add lines
        ax2.axvline(results['mu_b'], color='orange', linestyle='--', linewidth=2,
                   label=f"Average: {results['mu_b']:.0f} hrs")
        ax2.axvline(results['due_date_hours'], color='red', linestyle='--', linewidth=2,
                   label=f"Due date: {results['due_date_hours']:.0f} hrs")
        
        ax2.set_xlabel('Time (hours)')
        ax2.set_ylabel('Probability Density')
        ax2.set_title(f'Due Date with {confidence_level*100:.0f}% Confidence')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        st.pyplot(fig2)
        
        # Time series plot
        st.subheader("Time Series of Inter-Throughput Times")
        fig3, ax3 = plt.subplots(figsize=(12, 5))
        ax3.plot(range(1, len(inter_throughput_times)+1), inter_throughput_times, 
                marker='o', linestyle='-', color='steelblue')
        ax3.axhline(results['mean'], color='red', linestyle='--', 
                   label=f"Mean: {results['mean']:.1f} hrs")
        ax3.set_xlabel('Boat Number')
        ax3.set_ylabel('Inter-Throughput Time (hours)')
        ax3.set_title('Inter-Throughput Times Over Time')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        st.pyplot(fig3)
    
    with tab3:
        st.header("Detailed Statistics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Descriptive Statistics")
            desc_stats = pd.DataFrame({
                'Statistic': ['Count', 'Mean', 'Std Dev', 'Min', 'Max', 'Range'],
                'Value': [
                    len(inter_throughput_times),
                    f"{results['mean']:.2f} hrs",
                    f"{results['std']:.2f} hrs",
                    f"{min(inter_throughput_times):.2f} hrs",
                    f"{max(inter_throughput_times):.2f} hrs",
                    f"{max(inter_throughput_times) - min(inter_throughput_times):.2f} hrs"
                ]
            })
            st.table(desc_stats)
        
        with col2:
            st.subheader("Advanced Metrics")
            adv_stats = pd.DataFrame({
                'Metric': ['Variance', 'Autocorrelation', 'Coefficient of Variation'],
                'Value': [
                    f"{results['variance']:.2f} hrs²",
                    f"{results['autocorrelation']:.3f}",
                    f"{(results['std']/results['mean']*100):.1f}%"
                ]
            })
            st.table(adv_stats)
            
            # Interpretation of autocorrelation
            if results['autocorrelation'] > 0.3:
                st.warning("⚠️ **Moderate positive autocorrelation detected!** "
                          "Consecutive throughput times are related.")
            elif results['autocorrelation'] > 0.1:
                st.info("ℹ️ Weak positive autocorrelation detected.")
            else:
                st.success("✓ Negligible autocorrelation.")
        
        # Show raw data
        st.subheader("Raw Data")
        raw_df = pd.DataFrame({
            'Observation': range(1, len(inter_throughput_times)+1),
            'Inter-Throughput Time (hours)': inter_throughput_times
        })
        st.dataframe(raw_df, use_container_width=True)
    
    with tab4:
        st.header("Help & Information")
        
        st.markdown("""
        ### How to Use This Calculator
        
        1. **Input Data**: Choose one of three methods to input your data:
           - Use the example data from the LuxBoat case
           - Upload a CSV file with inter-throughput times
           - Enter data manually
        
        2. **Set Parameters**: 
           - Specify how many boats are needed
           - Choose your desired confidence level (typically 80-95%)
        
        3. **Interpret Results**:
           - The **due date** is when you can promise delivery
           - The **safety time** is extra buffer to achieve your confidence level
           - Higher confidence = longer due date = more safety time
        
        ### Key Concepts
        
        **Inter-Throughput Time**: The time between two consecutive completions
        
        **Autocorrelation**: Measures if consecutive times are related. Positive 
        autocorrelation means if one boat takes longer, the next probably will too.
        
        **Confidence Level**: The probability that the actual completion time will 
        be less than or equal to the quoted due date.
        
        **Safety Time**: Additional time added to the average to achieve the 
        desired confidence level.
        
        ### Formula
        
        The due date is calculated using:
        
        ```
        T_due = μ_b + z_α × σ_b
        
        where:
        μ_b = b × X̄ (mean time for b boats)
        σ_b² = [(1+ρ₁)/(1-ρ₁)] × b × S² (variance with autocorrelation)
        z_α = z-score for desired confidence level
        ```
        
        ### CSV Format
        
        Your CSV file should have a single column named `inter_throughput_time` 
        with one time value per row (in hours):
        
        ```
        inter_throughput_time
        32.5
        35.5
        40.0
        38.5
        ```
        """)
        
        # Download example CSV
        example_data = pd.DataFrame({
            'inter_throughput_time': inter_throughput_times[:10]
        })
        csv = example_data.to_csv(index=False)
        st.download_button(
            label="📥 Download Example CSV",
            data=csv,
            file_name="example_inter_throughput_times.csv",
            mime="text/csv"
        )

else:
    st.warning("⚠️ Please input data using the sidebar options to begin calculations.")
    
    st.markdown("""
    ### Getting Started
    
    Use the sidebar to:
    1. Choose a data input method
    2. Enter or upload your inter-throughput time data
    3. Set the number of boats needed
    4. Select your desired confidence level
    
    The app will automatically calculate and display your results!
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>LuxBoat Due Date Calculator | Built with Streamlit</p>
    <p><small>Based on throughput analysis and Central Limit Theorem</small></p>
</div>
""", unsafe_allow_html=True)
