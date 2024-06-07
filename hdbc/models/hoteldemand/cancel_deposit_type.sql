{{ config(materialized='table') }}

WITH cancel_deposit_type AS (
SELECT
    CASE 
        WHEN is_canceled ='1'
        THEN 'Cancelled'
        ELSE 'Confirmed'
    END AS Cancellation,
    deposit_type,
    COUNT(*) as "Number_of_Guest"

    FROM {{ ref("dim_hotel") }}  
    GROUP BY Cancellation,
    deposit_type
)
SELECT
    *
FROM cancel_deposit_type