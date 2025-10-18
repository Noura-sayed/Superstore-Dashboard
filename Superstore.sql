select top 10* from dbo.Orders$;
select top 10* from dbo.People$;
select top 10* from dbo.Returns$;

select City, sum(sales)
from dbo.Orders$
group by City
order by sum(sales) desc;

select distinct [Customer Name],country , city , state
from dbo.Orders$;

select [Sub-Category], sum(sales) , sum(profit)
from dbo.Orders$
group by [Sub-Category];

select category , 
       round(sum(sales),2)
	   ,round(sum(profit),2)
from dbo.Orders$
group by Category
order by sum(Sales) desc , sum(profit) desc;

select [customer name], count(distinct [Order ID])
from dbo.Orders$
group by [Customer Name];

SELECT 
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT [Order ID]) AS Total_Orders
FROM dbo.Orders$;

SELECT 
    ROUND(SUM(Profit) / COUNT(DISTINCT [Order ID]), 2) AS Avg_Profit_Per_Order
FROM dbo.Orders$;

CREATE VIEW SalesSummary AS
SELECT 
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM dbo.Orders$
GROUP BY Category;




