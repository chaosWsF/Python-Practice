-- Q1
SELECT a.GroupID, a.FirstName, a.LastName, a.Job, a.ExternalID, b.CompanyName, COUNT(*) AS "Count" 
FROM maintable_2RSJL AS a, cb_vendorinformation AS b 
WHERE a.GroupID=b.GroupID 
GROUP BY a.FirstName 
ORDER BY Count ASC, b.CompanyName ASC;
-- 

-- Q2
SELECT a.VENDOR_ID, a.PRODUCT_TYPE, 
       ROUND(AVG(b.GTAT), 2) AS "AVERAGE_GTAT", 
       ROUND(AVG(a.COST), 2) AS "AVERAGE_COST", 
       COUNT(*) AS "NUMBER_OF_ORDER" 
FROM Order_Summary AS a, 
     GTAT As b 
WHERE a.ORDER_ID = b.ORDER_ID 
AND a.STATUS_FLAG LIKE '%Complete' 
AND NOT a.PRODUCT_TYPE = 'AVM' 
AND (
     (AVERAGE_COST >= 150 AND a.PRODUCT_TYPE = 'Full Appraisal') 
     OR (AVERAGE_COST > 50 AND a.PRODUCT_TYPE = 'Drive-By') 
     OR (AVERAGE_COST > 30 AND a.PRODUCT_TYPE NOT IN ('Full Appraisal', 'Drive-By')) 
    ) 
GROUP BY a.VENDOR_ID, a.PRODUCT_TYPE 
ORDER BY a.VENDOR_ID, a.PRODUCT_TYPE;
-- 
