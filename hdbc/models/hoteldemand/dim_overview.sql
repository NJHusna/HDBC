-- with guest as (
--     select
--         booking_id,
--         is_repeated_guest,
--         customer_type
--     from {{ ref('silver_guest') }}

-- ),

-- booking as (
--     select
--         booking_id,
--         hotel,
--         lead_time,
--         meal,
--         market_segment
--     from {{ ref('silver_booking') }}

-- ),

-- cancellation as (

--     select
--         booking_id,
--         is_canceled
--     from {{ ref('silver_cancellations') }}

-- ),

-- joined as (
--     left join booking
--         on guest.booking_id = booking.booking_id

-- )

-- select * from joined

with guest as (
    select
        booking_id,
        is_repeated_guest,
        customer_type,
    from silver_guest
),
booking as (
    select
        booking_id,
        hotel,
        lead_time,
        meal,
        market_segment
    from silver_booking
),
cancellation as (
    select
        booking_id,
        is_canceled
    from silver_cancellations
),
joined as (
    select *
    from guest
    left join booking on guest.booking_id = booking.booking_id
    left join cancellation on guest.booking_id = cancellation.booking_id
)

select * 
from joined
