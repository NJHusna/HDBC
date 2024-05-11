WITH booking AS (
    SELECT *
    FROM {{ source('hdbc_stag', 'stag_booking') }}
),
rename_cast AS (
    SELECT 
        booking_id,
        hotel,
        lead_time,
        arrival_date_year,
        arrival_date_month,
        arrival_date_week_number,
        arrival_date_day_of_month,
        stays_in_weekend_nights,
        stays_in_week_nights,
        meal,
        market_segment,
        distribution_channel,
        reserved_room_type,
        assigned_room_type,
        booking_changes,
        deposit_type,
        days_in_waiting_list,
        adr as "average_daily_rate",
        required_car_parking_spaces,
        total_of_special_requests,
        CAST(company AS VARCHAR) AS company,
        CAST(agent AS VARCHAR) AS agent,
    FROM booking
    WHERE market_segment <> 'Undefined'
)
SELECT 
    *
FROM rename_cast