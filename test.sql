SELECT selected_column1 AS selected_column1_alias
      ,selected_column2
      ,selected_column3 AS selected_column3_alias
  FROM table_name
 WHERE where_column1 = 'where_column1_value'
   AND where_column2 = 'where_column2_value'
    OR where_column3 = 'where_column3_value'
 GROUP
    BY group_by_column1
      ,group_by_column2
 ORDER
    BY order_by_column1
      ,order_by_column2
;

