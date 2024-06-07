{{ config(materialized='table') }}

WITH percent AS (
    SELECT 
        market_segment as "Market Segment",
        ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(),2) as "Percentage(%)"
    FROM {{ ref("dim_hotel") }}
    GROUP BY market_segment
)
SELECT 
    "Market Segment",
    "Percentage(%)"
FROM percent