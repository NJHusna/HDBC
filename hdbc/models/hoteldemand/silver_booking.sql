{{ config(materialized='view') }}

WITH booking AS (
    SELECT *
    FROM {{ source('hdbc_stag', 'stag_booking') }}
),
rename_cast AS (
    SELECT 
        booking_id,
        hotel,
        lead_time,
        arrival_date_year,
        arrival_date_month,
        arrival_date_week_number,
        arrival_date_day_of_month,
        stays_in_weekend_nights,
        stays_in_week_nights,
        meal,
        CASE 
            WHEN market_segment = 'Undefined' THEN 'Online TA' 
            ELSE market_segment 
        END AS market_segment,
        CASE 
            WHEN distribution_channel = 'Undefined' THEN 'TA/TO' 
            ELSE distribution_channel 
        END AS distribution_channel,
        reserved_room_type,
        assigned_room_type,
        booking_changes,
        deposit_type,
        days_in_waiting_list,
        CASE 
            WHEN adr < 0 THEN (SELECT AVG(adr) FROM booking WHERE adr >= 0)
            WHEN adr > 5000 THEN (SELECT AVG(adr) FROM booking WHERE adr >= 0)
            ELSE adr
        END AS average_daily_rate,
        required_car_parking_spaces,
        total_of_special_requests,
        CAST(company AS VARCHAR) AS company,
        CAST(agent AS VARCHAR) AS agent,
        CASE
            WHEN arrival_date_month = 'January' THEN 1
            WHEN arrival_date_month = 'February' THEN 2
            WHEN arrival_date_month = 'March' THEN 3
            WHEN arrival_date_month = 'April' THEN 4
            WHEN arrival_date_month = 'May' THEN 5
            WHEN arrival_date_month = 'June' THEN 6
            WHEN arrival_date_month = 'July' THEN 7
            WHEN arrival_date_month = 'August' THEN 8
            WHEN arrival_date_month = 'September' THEN 9
            WHEN arrival_date_month = 'October' THEN 10
            WHEN arrival_date_month = 'November' THEN 11
            WHEN arrival_date_month = 'December' THEN 12
        END AS numeric_arrival_date_month
    FROM booking
)
SELECT 
    *
FROM rename_cast
ORDER BY average_daily_rate DESC