/*微格项目维表*/
select
    performance_id,
    item_id,
    performance_name,
    category_id,
    category_name,
    city_id,
    city_name,
    province_id,
    province_name,
    area_1_level_id,
    area_1_level_name,
    area_2_level_id,
    area_2_level_name,
    venue_id,
    shop_name,
    type_id,
    type_lv2_name,
    venue_type
from
    upload_table.dim_wg_performance_s
where
    1=1
