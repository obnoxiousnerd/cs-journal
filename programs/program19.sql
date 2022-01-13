-- The following two lines are to reset the tables and not a part of the 
-- original program.
drop table store;
drop table suppliers;

create table store(
    item_no integer primary key,
    item text,
    scode integer,
    qty integer,
    rate integer,
    last_buy text
);


insert into store values(101, "Sharpener", 25, 60, 5, "20-Nov-20");
insert into store values(102, "Pencil", 22, 100, 10, "14-Sep-20");
insert into store values(103, "Eraser", 24, 30, 5, "29-Jan-19");
insert into store values(104, "Scale 15cm", 21, 55, 15, "2-Oct-20");
insert into store values(105, "Ballpoint Pen Blue", 23, 200, 5, "9-Jan-21");

create table suppliers(
    scode integer primary key,
    sname text
);

insert into suppliers values(21, "Proveedores Elegantes") ;
insert into suppliers values(22, "Lime Plastics");
insert into suppliers values(23, "NotWalmart Sellers");
insert into suppliers values(24, "Fathom Supply");
insert into suppliers values(25, "SupplyLead") ;

-- Display details of all the items in the store table in ascending order of last_buy
select * from store order by last_buy;

-- Display item_no and itemname of those items from the store table whose rate
-- is more than 15 rupees
select item_no, item from store where rate > 15;

-- Display details of those items whose supplier code (scode) is 22 or quantity
-- in store is more than 110
select * from store where scode = 22 or qty > 110;

-- Display minimum rate of items where suppliers grouped by scode from store.
select scode, min(rate) from store group by scode;

-- Display itemname, qty from store s, suppliers p
select item, qty from store s, suppliers p where s.scode = p.scode and p.sname = "Lime Plastics";


-- Give output of the following SQL queries

select count(distinct scode) from store;
-- count(distinct scode)
-- 5

select rate * qty from store where item_no = 102;
-- rate * qty
-- 1000

select item, sname from store s, suppliers p where s.scode = p.scode and s.item_no = 102;
-- item    sname
-- Pencil  Lime Plastics

select max(last_buy) from store;
-- max(last_buy)
-- 9-Jan-21