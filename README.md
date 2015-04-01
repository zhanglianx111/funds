##命令行说明
<hr>
#### 删除数据库
>- ```funds delete-db db_name```

#### 删除数据库表
>- ```funds delete-tb -db db_name -t table_name```
>- ```funds delete-tb --database db_name --table table_name```

#### 清空数据库表内容
>- ```funds clear --database db_name --table table_name```
>- ```funds clear -db db_name -t table_name```

#### 计算所有基金在一段时间内的增长百分比，并支持指定数目按增序、降序排列基金，申购状态。
例如从time1---time2的增长百分比。
>- ```funds calculate --name fund_name --from time1 --to time2 --sort +/-```
>- ```funds calculate -n fund_name -f time1 -t time2 -s +/- -c 10```

- name：基金名。如果没有name参数，默认值为所有基金
- from：开始的时间点，默认值为当前时间点
- to：结束时间点，默认值为当前时间点之前的一周
- sort：输出的排列次序。“+”代表升序；“-”代表降序，默认值为降序
- count：显示计算后的基金个数

#### show已购买基金信息，包括：基金名、购买时间、购买金额、收益率、收益、持有份额，申购状态
>- ```funds list --sort +/-```
>- ```funds list -s +/-```

- list：列出购买基金信息
- sort：按收益率排序

