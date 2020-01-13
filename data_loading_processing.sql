CREATE TABLE public_griv_complaints (

registration_no string,
ministry_dept string,
country_name string,
state_name string,
distname string,
subject_content string,
diary_date string,
closing_date string,
source_name string,
rating string,
comments string,
rating_date string)

ROW FORMAT DELIMITED
FIELDS TERMINATED BY ‘,’
LINES TERMINATED BY ‘\n’

CREATE TABLE public_griv_movements (

registration_no string,
action_srno string,
action_name string,
date_of_action string,
org_name string,
org_name2 string,
remarks string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ‘,’
LINES TERMINATED BY ‘\n’

LOAD DATA INPATH "" INTO TABLE public_griv_complaints

LOAD DATA INPATH "" INTO TABLE public_griv_movements

CREATE TABLE public_griv_complete_set
AS
SELECT 
A.registration_no,
A.subject_content,
B.action_name,
B.date_of_action,
B.org_name,
B.org_name2,
B.remarks

from pg_complaints A inner join public_griv_movements B on rtrim(ltrim(A.registration_no))=rtrim(ltrim(B.registration_no));