WITH guest AS (
    SELECT *
    FROM {{ source('hdbc_stag', 'stag_guest') }}
),
rename_cast AS (
    SELECT 
        booking_id,
        name,
        email,
        "phone-number" AS phone_number,
        credit_card,
        adults,
        CASE 
            WHEN children IS NULL THEN CAST(AVG(children) OVER() AS INTEGER)  -- Replace NULL with mean
            ELSE CAST(children AS INTEGER)
        END AS children,
        babies,
        customer_type,
        is_repeated_guest,
        country
    FROM guest
)
SELECT 
    *
FROM rename_cast