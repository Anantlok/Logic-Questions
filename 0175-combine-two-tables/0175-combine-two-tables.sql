# Write your MySQL query statement below
select p.FirstName, p.lastname, a.city, a.state
from person p
left join address a
on p.personid=a.personid;