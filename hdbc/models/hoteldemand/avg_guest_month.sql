{{ config(materialized='table') }}

WITH 
guest_monthly AS (
    SELECT
        hotel,
        arrival_date_month AS month,
        SUM(adults + children + babies) AS guests,
        numeric_arrival_date_month
    FROM {{ ref("dim_hotel") }}
    WHERE is_canceled = 0
    GROUP BY hotel, month, numeric_arrival_date_month
    ORDER BY hotel
)
SELECT 
    *
FROM guest_monthly