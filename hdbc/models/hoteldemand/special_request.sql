{{ config(materialized='table') }}

WITH special_request AS (
    SELECT
        total_of_special_requests,
        count(*) as guest,
        hotel,
        arrival_date_year
    FROM 
        {{ ref("dim_hotel") }}
    WHERE is_canceled = 0
    GROUP BY total_of_special_requests, hotel, arrival_date_year
)
SELECT
    *
FROM 
    special_request
