with HighEarnerSalary as (
    select * from (
        select 
            distinct salary, 
            DENSE_RANK() OVER(partition by departmentId ORDER BY salary desc) as 'rank',
            departmentId
        from Employee
    ) hes
    where hes.rank <=3
)

select 
    d.name as "Department", 
    e.name as "Employee", 
    e.salary as "Salary"
from Employee as e 
    join Department as d on e.departmentId = d.id
    join HighEarnerSalary as hes 
        on hes.departmentId = e.departmentId and e.salary = hes.salary
