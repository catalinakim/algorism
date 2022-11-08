-- SELECT CART_ID,
--     CASE
--         WHEN AGE BETWEEN 14 AND 16 THEN 1

--         WHEN AGE BETWEEN 17 AND 19 THEN 0

--     END "ABUSED"

-- FROM COUPONS AS CP
-- JOIN CART_PRODUCTS AS PR
-- ON CP.CART_ID = PR.CART_ID;

SELECT PR.CART_ID,
    CASE
        WHEN (MINIMUM_REQUIREMENT > CART_SUM) THEN 1
        WHEN (MINIMUM_REQUIREMENT <= CART_SUM) THEN 0
    END "ABUSED"

FROM COUPONS AS CP
JOIN (select ID, CART_ID, sum(price)
    as CART_SUM from CART_PRODUCTS
    group by CART_ID) AS PR
ON CP.CART_ID = PR.CART_ID
ORDER BY PR.ID;

-- select CART_ID, sum(price) as 'sum' from CART_PRODUCTS group by CART_ID;

-- select * from COUPONS

/*
참고

FROM 구에서 서브쿼리 사용하기 : https://velog.io/@dongsagi90/MYSQL-집계함수-서브쿼리
SELECT * FROM (SELECT * FROM sample) AS sq;

SQL 조건에 따라 값 정해주기 - CASE : https://lcs1245.tistory.com/entry/SQL-조건에-따라-값-정해주기-CASE
SELECT *, CASE WHEN AGE BETWEEN 14 AND 16 THEN '중학생'
         WHEN AGE BETWEEN 17 AND 19 THEN '고등학생'
         WHEN AGE >= 20 THEN '성인'
         ELSE '어린이'
     END "IDENTITY"
FROM TABLE
*/