{{ config(materialized='table') }}

WITH cxl_leadtime AS (
    SELECT
        CASE
            WHEN is_canceled = '1' THEN 'Cancelled'
            ELSE 'Confirmed'
        END AS Cancellation,
        AVG(lead_time) AS Avg_lead_time,
        arrival_date_year
    FROM {{ ref("dim_hotel") }}
    GROUP BY arrival_date_year, is_canceled
)
SELECT
    *
FROM cxl_leadtime
