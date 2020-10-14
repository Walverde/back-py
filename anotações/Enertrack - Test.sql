
use exemplo;
select * from exemplo;

describe table exemplo;

desc Pew;

insert into TabelaTest values (
'10','11','12','13');

	create database exemplo
    
	default character set utf8
	default collate utf8_general_ci;
#++++++++++++++++++++++++++++++++++++++++++++++++++++
use nodered;
select * from DD1;
create table DD1 (
data1 int, 
data2 int,
TTime int 
);
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++
drop database temperature; 
drop table BIN;

create table BIN (
VARMS Int, 
VBRMS Int,
VCRMS Int,
IARMS Int,
IBRMS Int,
ICRMS Int,
VABRMS Int,
VBCRMS Int,
VCARMS Int,
VABCTRMS Int,
PA Int,
PB Int,
PC Int,
PT Int,
QA Int,
QB Int,
QC Int,
QT Int,
SA Int,
SB Int,
SC Int,
ST Int,
FPA Int,
FPB Int,
FPC Int,
FPT Int,
KVARHA Int,
KVARHB Int,
KVARHC Int,
KVARHT Int,
KWHA Int,
KWHB Int,
KWHC Int,
KWHT Int,
FREQ Int,
TEMP Int,
SERRS Int,
WRSSI Int,
UPTIME Int
);   

use Test;
 desc BIN;
select * from BIN;
alter table BIN

alter table BIN(
modify column VARMS SmalInt );
modify column VBRMS TinyInt;
modify column VCRMS TinyInt,
modify column IARMS TinyInt,
modify column IBRMS TinyInt,
modify column ICRMS TinyInt,
modify column VABRMS TinyInt,
modify column VBCRMS TinyInt,
modify column VCARMS TinyInt,
modify column VABCTRMS TinyInt,
modify column PA TinyInt,
modify column PB TinyInt,
modify column PC TinyInt,
modify column PT TinyInt,
modify column QA TinyInt,
modify column QB TinyInt,
modify column QC TinyInt,
modify column QT TinyInt,
modify column SA TinyInt,
modify column SB TinyInt,
modify column SC TinyInt,
modify column ST TinyInt,
modify column FPA TinyInt,
modify column FPB TinyInt,
modify column FPC TinyInt,
modify column FPT TinyInt,
modify column KVARHA TinyInt,
modify column KVARHB TinyInt,
modify column KVARHC TinyInt,
modify column KVARHT TinyInt,
modify column KWHA TinyInt,
modify column KWHB TinyInt,
modify column KWHC TinyInt,
modify column KWHT TinyInt,
modify column FREQ TinyInt,
modify column TEMP TinyInt,
modify column SERRS TinyInt,
modify column WRSSI TinyInt,
modify column UPTIME TinyInt);
  
modify column VARMS TinyInt,
VBRMS varchar(20),
VCRMS varchar(20),
IARMS varchar(20),
IBRMS varchar(20),
ICRMS varchar(20),
VABRMS varchar(20),
VBCRMS varchar(20),
VCARMS varchar(20),
VABCTRMS varchar(20),
PA varchar(20),
PB varchar(20),
PC varchar(20),
PT varchar(20),
QA varchar(20),
QB varchar(20),
QC varchar(20),
QT varchar(20),
SA varchar(20),
SB varchar(20),
SC varchar(20),
ST varchar(20),
FPA varchar(20),
FPB varchar(20),
FPC varchar(20),
FPT varchar(20),
KVARHA varchar(20),
KVARHB varchar(20),
KVARHC varchar(20),
KVARHT varchar(20),
KWHA varchar(20),
KWHB varchar(20),
KWHC varchar(20),
KWHT varchar(20),
FREQ varchar(20),
TEMP varchar(20),
SERRS varchar(20),
WRSSI varchar(20),
UPTIME varchar(20)
desc BIN;


drop table BIN;
truncate table BIN;
