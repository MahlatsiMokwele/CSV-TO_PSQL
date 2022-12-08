CREATE SCHEMA IF NOT EXISTS road_segments;

CREATE TABLE IF NOT EXISTS road_segments.202212000_road_segments as (
    feat_id uuid,
    geom public.geometry,
    pos_azimuth double precision,
    neg_azimuth double precision,
    pos_passenger numeric,
    pos_truck numeric,
    pos_private_bus numeric,
    pos_public_bus numeric,
    pos_other numeric,
    neg_passenger numeric,
    neg_truck numeric,
    neg_private_bus numeric,
    neg_public_bus numeric,
    neg_other numeric
) 
