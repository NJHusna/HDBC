{{ config(materialized='table') }}

WITH cancel AS (
    SELECT
        CASE
            WHEN is_canceled = '1'
            THEN 'Cancelled Guest'
        ELSE 'Confirmed Guest'
        END AS Cancellation,
        ROUND(COUNT(*) * 100/ SUM(COUNT(*)) OVER(),2) As Percentage
        FROM {{ ref("dim_hotel") }}
        GROUP BY is_canceled
)
SELECT
    Cancellation,
    Percentage
FROM cancel