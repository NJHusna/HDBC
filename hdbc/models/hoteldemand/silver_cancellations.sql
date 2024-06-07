{{ config(materialized='view') }}

WITH cancellation AS (
    SELECT *
    FROM {{ source('hdbc_stag', 'stag_cancellation') }}
),
rename_cast AS (
    SELECT 
        booking_id,
        is_canceled,
        reservation_status,
        reservation_status_date AS reservation_status_datetime,
        previous_cancellations, 
        previous_bookings_not_canceled
    FROM cancellation
)
SELECT * FROM rename_cast