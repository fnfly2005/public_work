/*andriod,push*/
select
	user_id babytree_user_id,
	clientid
from
	(select
		user_id,
		clientid,
		row_number() over (partition by user_id order by update_ts desc) row_number
	from
		babytree.userappclientidmaptotal
	where
		app_id=11)
where
	row_number=1
