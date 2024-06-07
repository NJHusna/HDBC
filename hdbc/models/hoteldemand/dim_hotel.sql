{{ config(materialized='table') }}

with guest as (
    select
        *
    from {{ ref("silver_guest") }}
),
booking as (
    select
        *
    from {{ ref("silver_booking") }} 
),
cancellation as (
    select
        *
    from {{ ref("silver_cancellations") }}
),
hotel as (
    select *
    from guest
    left join booking on guest.booking_id = booking.booking_id
    left join cancellation on guest.booking_id = cancellation.booking_id
)

select * 
from hotel