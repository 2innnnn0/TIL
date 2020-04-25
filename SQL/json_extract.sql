SELECT
 JSON_EXTRACT_SCALAR("{'id' : 'b21'}", '$.id'),
 JSON_EXTRACT_SCALAR('{"acdnt_dt":“20180831"}', '$.acdnt_dt')
)