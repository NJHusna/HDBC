{{ config(materialized='table') }}

WITH repeat_guest AS (
SELECT
    CASE 
        WHEN is_repeated_guest ='1'
        THEN 'Repeated Guest'
        ELSE 'First-Time Guest'
    END AS "Guest_Type",
    COUNT(*) as "Guest",
    distribution_channel as "Distribution_Channel"

    FROM {{ ref("dim_hotel") }}   
    GROUP BY is_repeated_guest, distribution_channel
)
SELECT
    "Guest_Type",
    "Guest",
    "Distribution_Channel"
FROM repeat_guest