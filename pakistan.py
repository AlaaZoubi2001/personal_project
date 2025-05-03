import streamlit as st
import pandas as pd
import numpy as np
import os

#static
import matplotlib.pyplot as plt
import seaborn as sns


st.markdown("""
       <div style="background-color: white; padding: 10px; border-radius: 10px;">
        <h1 style="color: #2A261E; text-align: center;">Hello and welcome to my Dashboard</h1>
        <h3 style="color:5E4534; text-align: center;">Pakistan's Largest E-Commerce Dataset</h3>  
          <p style="font-size:18px; line-height:1.5; color: #333;">
    In this project, we’ll dive into Pakistan’s e‑commerce dataset to uncover customer patterns, sales dynamics, and potential growth areas.<br>
    Start by uploading a CSV file with your data to get started.
  </p>
    </div>""",
    unsafe_allow_html=True
)

df =pd.read_csv('C:/Users/כללי/Downloads/personal_project/Pakistan_data cleaniing.csv', encoding='latin-1')


st.markdown("""
    <style>
    .centered-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .centered-button button {
        font-size: 24px !important;
        padding: 15px 40px !important;
        background-color: #FF5733;
        color: white;
        border: none;
        border-radius: 12px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)
#st.write(df.columns.tolist())
# Sidebar filters
year_options = ["All"] + sorted(df['Year'].dropna().unique().tolist())
selected_year = st.sidebar.selectbox("Select Year", year_options)

status_options = ["All"] + sorted(df['status'].dropna().unique().tolist())
selected_status = st.sidebar.selectbox("Select Status", status_options)

statusbi_options = ["All"] + sorted(df['BI Status'].dropna().unique().tolist())
selected_statusbi = st.sidebar.selectbox("Select BI Status", statusbi_options)

statusbi_options = ["All"] + sorted(df['category_name_1'].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", statusbi_options)
filtered_df = df[
    ((df['Year'] == selected_year) | (selected_year == "All")) &
    ((df['status'] == selected_status) | (selected_status == "All")) &
    ((df['BI Status'] == selected_status) | (selected_status == "All"))&
    ((df['category_name_1'] == selected_status) | (selected_status == "All"))
]
filtered_df = df.copy()

if selected_year != "All":
    filtered_df = filtered_df[filtered_df['Year'] == selected_year]
if selected_status   != "All":
    filtered_df = filtered_df[filtered_df['status'] == selected_status]
if selected_statusbi  != "All":
    filtered_df = filtered_df[filtered_df['BI Status'] == selected_statusbi]
if selected_category != "All":
    filtered_df = filtered_df[filtered_df['category_name_1'] == selected_category]



with st.sidebar:
    st.markdown("---")
    st.markdown("Download Data")

    @st.cache_data
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(filtered_df)

    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name="DataCleaning-Pakistan Largest Ecommerce Dataset.csv",
        mime="text/csv"
    )
    st.markdown("Export your filtered data for further analysis")

#-----------------------------
def display_data_random(df):
    sample = df.sample(5)
    return sample

#st.caption('click on the button below to display the row randomly')
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    button = st.button('click on the button below to display the row randomly', use_container_width=True)
if button:
    sample = display_data_random(df)
    st.dataframe(sample)
#------------------------------------------------------------------------------
st.markdown("""
    <style>
    [data-testid="metric-container"] {
        background-color: white !important;
        border-radius: 12px !important;
        padding: 20px 10px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
        margin: 10px !important;
        min-width: 12rem !important;
        flex: 1 1 200px !important;
    }
    [data-testid="metric-container"] > div {
        text-align: center !important;
        white-space: nowrap;
    }
    </style>
""", unsafe_allow_html=True)

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(1)

with row1[0]:
    st.metric("Total Revenue", f"{948_781_627:,}")
with row1[1]:
    st.metric("Total Number of Orders", f"{106_734:,}")
with row1[2]:
    st.metric("Order Cancellation", "20.2%")

with row2[0]:
    st.metric("Unique Customers", f"{13_777:,}")
with row2[1]:
    st.metric("Average Revenue per Customer", f"{68_867:,}$")
with row2[2]:
    st.metric("Average Order Value", f"{8_889:,}$")

with row3[0]:
    st.metric("Repeat Customers Rate", "62.28%")


#yearly dales trends
st.markdown("""
    <div style="background-color: #BCCCAB; padding: 8px; border-radius: 10px; margin-top: 20px;">
        <h2 style="color: black; text-align: center;">Yearly Sales Trends in Pakistan</h2>
    </div>
""", unsafe_allow_html=True)
with st.container():
    value_counts =filtered_df['Year'].value_counts()
    colors = ['#7E7365', '#B1A592', '#D1CCBD'] 
    fig,ax =plt.subplots()
    ax.pie(value_counts,autopct='%0.2f%%',labels=value_counts.index,colors=colors)
    st.pyplot(fig)
    st.dataframe(value_counts)
#---------------
#yearly dales trends
st.markdown("""
    <div style="background-color: #BCCCAB; padding: 8px; border-radius: 10px; margin-top: 20px;">
        <h2 style="color: black; text-align: center;">Count of BI Status</h2>
    </div>
""", unsafe_allow_html=True)
with st.container():
    value_counts =filtered_df['BI Status'].value_counts()
    colors = ['#FEC8D8','#FFDFD3','#D4A5A5'] 
    fig,ax =plt.subplots()
    ax.pie(value_counts,autopct='%0.2f%%',labels=value_counts.index,colors=colors)
    st.pyplot(fig)
    st.dataframe(value_counts)
#-------------------
#Category Distribution
st.markdown("""
    <div style="background-color: #BCCCAB; padding: 8px; border-radius: 10px; margin-top: 20px;">
        <h2 style="color: black; text-align: center;">Category Distribution</h2>
    </div>
""", unsafe_allow_html=True)
with st.container():
    value_counts=df['category_name_1'].value_counts()
    fig,ax =plt.subplots()
    ax.bar(value_counts.index,value_counts,color='skyblue')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

#Order Stauts
st.markdown("""
    <div style="background-color: #BCCCAB; padding: 8px; border-radius: 10px; margin-top: 20px;">
        <h2 style="color: black; text-align: center;">Business Intelligence Status</h2>
    </div>
""", unsafe_allow_html=True)
with st.container():
    value_counts=filtered_df['BI Status'].value_counts()
    fig,ax =plt.subplots()
    ax.bar(value_counts.index,value_counts,color='#9AB87A') 
    ax.set_ylabel('Count') 
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

##-----------------------------
st.markdown("""
    <div style="background-color: #BCCCAB; padding: 8px; border-radius: 10px; margin-top: 20px;">
        <h2 style="color: black; text-align: center;">Revenue Distribution by BI Status</h2>
    </div>
""", unsafe_allow_html=True)
df['calculated_revenue'] = df['price'] * df['qty_ordered']
revenue_by_status = df.groupby('BI Status')['grand_total'].sum() 
fig, ax = plt.subplots()
revenue_by_status.plot(kind='bar', stacked=True, color=['#60424D', '#8E6E73', '#B49F9E'], ax=ax)

#ax.set_xlabel('BI Status') 
ax.set_ylabel('Total Revenue')  
#ax.set_title('Revenue Distribution by BI Status') 

st.pyplot(fig)


#----------------------------------------------

fig, ax = plt.subplots(2, 1, figsize=(8, 12))

# Normal scale plot
st.markdown("""
    <div style="background-color: #BCCCAB; padding: 8px; border-radius: 10px; margin-top: 20px;">
        <h2 style="color: black; text-align: center;">Monthly Sales</h2>
    </div>
""", unsafe_allow_html=True)
ax[0].plot(df['created_at'], df['grand_total'])
ax[0].set_title('Monthly Sales')
ax[0].set_xlabel('Months')
ax[0].set_ylabel('Sales')

# Log scale plot
ax[1].plot(df['created_at'], np.log10(df['grand_total']))
ax[1].set_title('Logarithm of Monthly Sales (base 10)')
ax[1].set_xlabel('Months')
ax[1].set_ylabel('log10(Sales)')

plt.tight_layout()
st.pyplot(fig)

##-------------------

def set_size_style(w, h, style):
    sns.set_style(style)
    plt.figure(figsize=(w, h))

# Custom plot labeling function (replace if you have your own)
def customize_plot(ax, title, xlabel, ylabel, title_size, label_size):
    ax.set_title(title, fontsize=title_size)
    ax.set_xlabel(xlabel, fontsize=label_size)
    ax.set_ylabel(ylabel, fontsize=label_size)

#---------
st.markdown("""
    <div style="background-color: #BCCCAB; padding: 8px; border-radius: 10px; margin-top: 20px;">
        <h2 style="color: black; text-align: center;">Count of Orders with Specific Statuses</h2>
    </div>
""", unsafe_allow_html=True)
desired_statuses = ['canceled', 'order_refunded', 'refund']
df_filtered = df[df['status'].isin(desired_statuses)]
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(4, 4))
plot = sns.countplot(data=df_filtered, x='status' ,ax=ax)

# Add labels with the count on the bars
for container in ax.containers:
    ax.bar_label(container)

plot.set_xticklabels(plot.get_xticklabels(), rotation=40)
#ax.set_xlabel("Order Status")
ax.set_ylabel("Orders")
#ax.set_title("Count of Orders with Specific Statuses")  
st.pyplot(fig)


#----------
st.markdown("""
    <div style="background-color: #BCCCAB; padding: 8px; border-radius: 10px; margin-top: 20px;">
        <h2 style="color: black; text-align: center;">Monthly Total Grand by Year</h2>
    </div>
""", unsafe_allow_html=True)
df['created_at'] = pd.to_datetime(df['created_at'])

# Extract year and month
df['year'] = df['created_at'].dt.year
df['month'] = df['created_at'].dt.month
df['month_name'] = df['created_at'].dt.strftime('%B')

# Group by year and month
monthly_sales = df.groupby(['year', 'month', 'month_name'])['grand_total'].sum().reset_index()

# Sort by month number
monthly_sales = monthly_sales.sort_values(by='month')

# Pivot data (years as columns)
pivot_df = monthly_sales.pivot(index='month_name', columns='year', values='grand_total')
pivot_df = pivot_df.reindex(['January', 'February', 'March', 'April', 'May', 'June',
                             'July', 'August', 'September', 'October', 'November', 'December'])

# Plotting with bigger style
fig, ax = plt.subplots(figsize=(20, 10))  # Bigger figure

pivot_df.plot(
    ax=ax, 
    marker='o', 
    markersize=8,        # Bigger points
    linewidth=3          # Thicker lines
)

# Add labels to each point
for year in pivot_df.columns:
    for month_idx, value in enumerate(pivot_df[year]):
        if not pd.isna(value):
            ax.annotate(
                f"{int(value):,}", 
                (month_idx, value), 
                textcoords="offset points", 
                xytext=(0, 10), 
                ha='center',
                fontsize=10, 
                color='black'
            )

# Styling
ax.set_title('Monthly Total Grand by Year', fontsize=18)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Total Grand', fontsize=14)
ax.legend(title='Year', fontsize=12, title_fontsize=13)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Show in Streamlit
st.pyplot(fig)

#----------------------------------------------------
st.markdown("""
    <div style="background-color: #BCCCAB; padding: 8px; border-radius: 10px; margin-top: 20px;">
        <h2 style="color: black; text-align: center;">Distribution of Orders by Date</h2>
    </div>
""", unsafe_allow_html=True)
def set_size_style(w, h, style='whitegrid'):
    sns.set_style(style)
    plt.figure(figsize=(w, h))

def customize_plot(ax, title, xlabel, ylabel, title_size=14, label_size=12):
    ax.set_title(title, fontsize=title_size)
    ax.set_xlabel(xlabel, fontsize=label_size)
    ax.set_ylabel(ylabel, fontsize=label_size)



df['created_at'] = pd.to_datetime(df['created_at'])


fig, ax = plt.subplots(figsize=(10, 5))
sns.set_style("whitegrid")

sns.histplot(
    data=df,
    x='created_at',
    bins=20,
    color='#B49F9E',
    kde=True,
    ax=ax
)

customize_plot(ax, 'Distribution of Orders by Date', 'Date', 'Order Frequency', 12, 10)
st.pyplot(fig)

