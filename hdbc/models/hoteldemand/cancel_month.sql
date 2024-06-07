{{ config(materialized='table') }}

WITH cxl_month AS (
    SELECT
        CASE
            WHEN is_canceled = '1'
            THEN 'Cancelled'
        ELSE 'Confirmed'
        END AS Cancellation,
        ROUND(COUNT(*) * 100/ SUM(COUNT(*)) OVER(),2) As Percentage,
        arrival_date_month, numeric_arrival_date_month
        FROM {{ ref("dim_hotel") }}
        GROUP BY is_canceled, arrival_date_month, numeric_arrival_date_month
)
SELECT
    Cancellation,
    Percentage,
    arrival_date_month, 
    numeric_arrival_date_month
FROM cxl_month