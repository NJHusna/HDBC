{{ config(materialized='table') }}

WITH hotel_counts AS (
    SELECT
        hotel,
        ROUND(COUNT(*) * 100 / SUM(COUNT(*)) OVER()) as percentage
    FROM {{ ref("dim_hotel") }}
    GROUP BY hotel
)
SELECT
    *
FROM hotel_counts