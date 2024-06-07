{{ config(materialized='table') }}

WITH room_price AS (
    SELECT 
        arrival_date_month AS month,
        hotel,
        ROUND(AVG(average_daily_rate), 2) AS average_monthly_rate,
        numeric_arrival_date_month
    FROM 
        {{ ref("dim_hotel") }}
    GROUP BY 
        arrival_date_month, hotel, numeric_arrival_date_month
)
SELECT 
    month,
    hotel,
    average_monthly_rate,
    numeric_arrival_date_month
FROM 
    room_price
ORDER BY numeric_arrival_date_month