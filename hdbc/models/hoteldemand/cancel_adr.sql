{{ config(materialized='table') }}

WITH cxl_adr AS (
    SELECT
        CASE 
            WHEN is_canceled ='1'
            THEN 'Cancelled'
            ELSE 'Confirmed'
        END AS Cancellation,
        arrival_date_month AS month,
        ROUND(avg(average_daily_rate)) as avg_daily_rate,
        numeric_arrival_date_month
    FROM {{ ref("dim_hotel") }}
    GROUP BY month, numeric_arrival_date_month, Cancellation
    ORDER BY numeric_arrival_date_month, cancellation
)
SELECT 
    *
FROM cxl_adr
ORDER BY month, Cancellation DESC