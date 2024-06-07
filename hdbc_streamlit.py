import streamlit as st
import pandas as pd
import duckdb
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
import altair as alt


db_path = str(Path.cwd() / 'hdbc.duckdb')
conn = duckdb.connect(db_path)

st.set_page_config(page_title = "Hotel Demand Boooking and Cancellation",
                page_icon= "🏨", layout="wide")
st.title("Hotel Demand: Booking & Cancellation")



Int, Ovw, Bkg, cxl = st.tabs(["Context","Overview", "Booking Trends & Insights", "Cancellation Insights"])

#--------------------Introduction--------------------#
with Int:
    st.header("Unlocking Hotel Booking Demand and Cancellation Analysis Dynamics")
    st.markdown(
        """
        Embark on a revealing exploration into hotel booking dynamics through our analysis, 
        which uncovers the intricate interplay between demand and cancellation trends crucial for travelers and hoteliers alike. 
        By delving into a comprehensive dataset spanning city and resort hotels, we uncover patterns revealing optimal booking timing, 
        pricing dynamics influenced by stay durations, and predictive insights into special request likelihood. 
        Our analysis provides valuable insights into booking behaviors, empowering stakeholders to make informed decisions. 
        Wondering about the ideal booking time or predicting special request likelihood? Dive into our dataset, 
        scrubbed for privacy, for illuminating answers encompassing booking dates.
        
        #### Key Aspects Explored
        - **Booking and Cancellation Trends**: Discover the trends in hotel booking demand and cancellations, unraveling insights that can influence booking decisions.
        - **Pricing Dynamics**: Explore how pricing varies with factors like room type, booking lead time, and seasonality.
        - **Guest Preferences**: Understand guest preferences and behaviors, such as the likelihood of special requests and the impact of cancellation policies.
        - **Market Segmentation**: Analyze booking trends across different market segments, providing insights for targeted marketing strategies.

        #### Dataset Origins and Preparation
        The dataset originates from the article "Hotel Booking Demand Datasets" by Nuno Antonio, Ana Almeida, and Luis Nunes, published in Data in Brief, Volume 22, February 2019. 
        The data has been meticulously cleaned and prepared by Thomas Mock and Antoine Bichat for the #TidyTuesday initiative in February 2020. 
        It includes a wealth of information, such as booking dates, stay durations, guest demographics, parking availability, and more, 
        while ensuring the privacy of all guests by removing any personally identifiable information.

        #### Significance of the Analysis
        This analysis not only aids travelers in making cost-effective and well-timed booking decisions but also assists hoteliers in optimizing their pricing strategies, 
        improving guest satisfaction, and managing their operations more efficiently. 
        By understanding the underlying trends and patterns in hotel bookings and cancellations, both parties can benefit from a more predictable and streamlined experience.

        Dive into the detailed analysis to uncover the intricate dynamics of hotel booking demand and cancellation, and equip yourself with the knowledge to navigate the hospitality landscape with confidence.
        """
        )
#--------------------Overview--------------------#
colors = ['#FFECCA','#859887']
with Ovw:
    st.header("Overview of Booking & Cancellation Analysis")
    # st.caption("This page is intended for giving the overview")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    #--------------------Hotel Category Breakdown--------------------#
    with col1:
        hotel_type = conn.sql(""" SELECT * FROM perc_hotel_type""")
        hotel_type_df = hotel_type.df()
        
        st.subheader("Hotel Category Breakdown")
        explode = (0.05, 0)
        fig, ax = plt.subplots(figsize=(4,2))
        ax.pie(hotel_type_df['percentage'], labels=hotel_type_df['hotel'], 
            autopct='%1.0f%%', startangle=140, colors=colors, explode=explode,  textprops={'fontsize': 4})
        ax.axis('equal')
        st.pyplot(fig)

    #--------------------Percentage Breakdown by Market Segment--------------------#
    with col2:    
        market_segment = conn.sql(""" SELECT * FROM market_segment """)
        market_segment_df = market_segment.df()
        
        st.subheader("Percentage Breakdown by Market Segment")
        st.bar_chart(
            market_segment_df,
            x="Market Segment",
            y="Percentage(%)",  
            color=["#859887"],
            height=500)
        
    #--------------------Breakdown of Cancellation Rate--------------------#
    with col3:
        cancel_rate = conn.sql("""SELECT * FROM cancel_rate""")
        cancel_rate_df = cancel_rate.df()
        
        st.subheader("Breakdown of Cancellation Rate")
        explode = (0.05, 0)
        fig, ax = plt.subplots(figsize=(4,2))
        ax.pie(cancel_rate_df["Percentage"], labels=cancel_rate_df['Cancellation'], 
            autopct='%1.0f%%', startangle=140, colors=colors, explode=explode,  textprops={'fontsize': 4})
        ax.axis('equal')
        st.pyplot(fig)
        
    #--------------------Repeated Guest--------------------#
    with col4:
        rep_guests = conn.sql("""SELECT * FROM repeated_guest """)
        rep_guests_df = rep_guests.df()
        
        st.subheader("Bookings by Distribution Channel and Guest Type")
        c = alt.Chart(rep_guests_df).mark_bar().encode(
            x=alt.X("Guest_Type:N", title=None),
            y=alt.Y("Guest:Q", title='Number of Guest', scale=alt.Scale(type='log')),
            color=alt.Color("Guest_Type:N", title='Guest Type', scale=alt.Scale(range=colors)),
            column=alt.Column("Distribution_Channel:N", title='Distribution Channel')
        ).properties(height=400, width=150
        ).configure_axis(grid=False  
        )
        st.altair_chart(c, use_container_width=False)

#--------------------Booking--------------------#
with Bkg:
    st.header("Booking Characteristics and Trends")
    #st.caption("###")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    #--------------------Average Monthly Room Rates by Hotel Over Time--------------------#
    with col1:
        room_price = conn.sql("""SELECT * FROM room_price""")
        room_price_df = room_price.df()
        
        st.subheader("Average Monthly Room Rates by Hotel Over Time")
        c = alt.Chart(room_price_df).mark_line().encode(
            x= alt.X("month", title='Month', sort=alt.SortField('numeric_arrival_date_month', order = 'ascending')),
            y=alt.Y('average_monthly_rate:Q', title='Average Monthly Rate'),
            color=alt.Color('hotel',scale=alt.Scale(range=colors)),
            tooltip=['month', 'average_monthly_rate', 'hotel']
        )
        st.altair_chart(c, use_container_width=True)
                
    with col2:
        guest_month = conn.sql("""SELECT * FROM avg_guest_month""")
        guest_month_df = guest_month.df()
        
        st.subheader("Number of Guests by Hotel Over Time")
        c = alt.Chart(guest_month_df).mark_line().encode(
            x=alt.X("month", title='Month', sort=alt.SortField('numeric_arrival_date_month', order = 'ascending')),
            y=alt.Y('guests:Q', title='Number of Guest'),
            color=alt.Color('hotel', scale=alt.Scale(range=colors)),
            tooltip=['month', 'guests', 'hotel']
        )
        st.altair_chart(c, use_container_width=True)
        
    with col3:
        price_night = conn.sql("""
            SELECT 
                average_daily_rate,
                reserved_room_type,
                hotel
            FROM dim_hotel
        """)
        price_night_df = price_night.df()
        
        st.subheader("Distribution of Room Prices per Night by Room Type")
        plt.figure(figsize=(12, 8))
        sns.boxplot(x="reserved_room_type",
                    y="average_daily_rate",
                    hue="hotel",
                    data=price_night_df,
                    palette=colors,
                    fliersize=0,
                    order=sorted(price_night_df['reserved_room_type'].unique()))
        plt.xlabel("Type of Room", fontsize=16)
        plt.ylabel("Room Price", fontsize=16)
        plt.legend(loc="upper right")
        plt.ylim(-10, 450)
        st.pyplot(plt)
    
    with col4:
        special_request = conn.sql("""SELECT * FROM special_request""")
        special_request_df = special_request.df()
        
        st.subheader("Number of Guests with Special Requests")
        st.caption("0 indicates no special requests from guest")
        c = alt.Chart(special_request_df).mark_bar().encode(
            x=alt.X('total_of_special_requests:N', title='Number of Special Requests', axis=alt.Axis(labelAngle=0)),
            y=alt.Y('guest:Q', title='Number of Guests'),
            color=alt.Color('hotel:N', title='total_of_special_requests', scale=alt.Scale(range=colors)),
            column=alt.Column('hotel:N', title='Hotel')
        ).properties(
            height=400, width=300
        ).configure_axis(
            grid=False  
        )

        st.altair_chart(c, use_container_width=False)
            
#--------------------Cancellation--------------------#
with cxl:
    st.header("Cancellations Insights")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        cxl_month = conn.sql("""SELECT * FROM cancel_month""")
        cxl_month_df = cxl_month.df()
        
        st.subheader("Cancellation Percentage by Month")
        c = alt.Chart(cxl_month_df).mark_bar().encode(
            x=alt.X('Cancellation:N', title=None),
            y=alt.Y('Percentage:Q', title='Percentage(%)'),
            color=alt.Color('Cancellation:N', scale=alt.Scale(range=colors)),
            column=alt.Column('arrival_date_month:N',title='Arrival Date Month', sort=alt.EncodingSortField(field='numeric_arrival_date_month', order='ascending'))
        ).properties(
            height=400, width=35
        ).configure_axis(
            grid=False   
        )
        st.altair_chart(c, use_container_width=False)  

    with col2:
        cxl_depo_type = conn.sql("""SELECT * FROM cancel_deposit_type""")
        cxl_depo_type_df = cxl_depo_type.df()
        
        st.subheader("Cancellation Rate by Deposit Type and Number of Guests")
        c = alt.Chart(cxl_depo_type_df).mark_bar().encode(
            x=alt.X('Number_of_Guest', title='Number of Guest').stack("normalize"),
            y=alt.Y('deposit_type', title='Deposit Type'),
            color=alt.Color('Cancellation' , scale=alt.Scale(range=colors)),
        ).properties(
            height=600, width=800
        ).configure_axis(
            grid=False   
        )
        st.altair_chart(c, use_container_width=False)
    
    with col3:
        cxl_leadtime = conn.sql("""SELECT * FROM cancel_leadtime""")
        cxl_leadtime_df = cxl_leadtime.df()

        st.subheader("Average Lead Time to Cancellation by Year")
        c = alt.Chart(cxl_leadtime_df).mark_bar().encode(
            x=alt.X('Cancellation:N', title='Cancellation'),
            y=alt.Y('Avg_lead_time:Q', title='Lead Time'),
            color=alt.Color('Cancellation:N', title='Cancellation', scale=alt.Scale(range=colors)),
            column=alt.Column('arrival_date_year:N', title='arrival_date_year')
        ).properties(
            height=400, width=250
        ).configure_axis(
            grid=False  
        )
        st.altair_chart(c, use_container_width=False)
    
    with col4:
        cxl_adr = conn.sql("""SELECT * FROM cancel_adr""")
        cxl_adr_df = cxl_adr.df()
        
        st.subheader("Average Monthly Room Rate Trends by Cancellation Status")
        c = alt.Chart(cxl_adr_df).mark_line().encode(
            x=alt.X("month", title='Month', sort=alt.SortField('numeric_arrival_date_month', order='ascending')),
            y=alt.Y('avg_daily_rate:Q', title='Average Monthly Rate', scale=alt.Scale(domain=[50, 150])),
            color=alt.Color('Cancellation', scale=alt.Scale(range=colors))
        ).properties(
            height=500, width=500
        ).configure_axis(
            grid=False  
        )
        st.altair_chart(c, use_container_width=True)

conn.close()