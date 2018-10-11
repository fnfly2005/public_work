#!/bin/bash
source ./my_code/fuc.sh
fpw=`fun detail_myshow_pv_wide_report.sql ut`
wpv=`fun my_code/sql/dim_myshow_pv.sql u`
mke=`fun my_code/sql/myshow_unused_key.sql`

fus() {
    echo "
    select
        pv_id,
        cp.page_identifier,
        case when biz_par is null then ck
        when length(biz_par)<2 then ck
        else (biz_par || '&' || ck) end as ck
    from (
        select
            fp.page_identifier,
            array_join(array_agg(fp.ck),'&','null') ck
        from (
            select distinct
                page_identifier,
                ck
            from (
                select
                    page_identifier,
                    map_keys(custom) as cus_key
                $fpw
                    and partition_biz_bg<2
                    and map_keys(custom) is not null
                    and map_keys(custom)<>array[]
                group by
                    1,2
                ) fpw
                CROSS JOIN UNNEST(cus_key) as t (ck)
            where
                ck is not null
            ) fp
            left join (
                $mke
                ) mke
                on mke.unused_key=fp.ck
            left join (
                select distinct
                    page_identifier,
                    ck
                from (
                    select
                        page_identifier,
                        split(biz_par,'&') cus_key
                    $wpv
                        and biz_par is not null
                    ) wpv
                    CROSS JOIN UNNEST(cus_key) as t (ck)
                where ck is not null
                ) wp
            on wp.page_identifier=fp.page_identifier
            and wp.ck=fp.ck
        where
            wp.ck is null 
            and mke.unused_key is null
        group by
            1
        ) as cp
        left join (
            select
                pv_id,
                page_identifier,
                biz_par
            $wpv
            ) pv
        on pv.page_identifier=cp.page_identifier
    ${lim-;}"
}

downloadsql_file $0
fuc $1
