/*猫眼演出模块埋点配置维度表*/
select
    mv_id,
    page_name_my,
    event_name_lv1,
    event_name_lv2,
    event_id,
    biz_par,
    biz_typ,
    cid_type,
    page_identifier,
    user_intention,
    biz_tag,
    page_loc,
    operation_flag
from
    mart_movie.dim_myshow_mv
where
    status=1
