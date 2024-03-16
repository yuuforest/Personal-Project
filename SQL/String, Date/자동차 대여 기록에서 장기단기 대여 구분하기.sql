
-- Level 1

-- 대여 기록에 대한 모든 정보 및 대여 상태
    -- 대여 시작일이 2022년 9월에 속하는 대여 기록
    -- 대여 기간이 30일 이상이면 "장기 대여" 그렇지 않으면 "단기 대여"
    -- 대여 기록 ID를 기준으로 내림차순

SELECT HISTORY_ID, CAR_ID, 
        DATE_FORMAT(START_DATE, "%Y-%m-%d") AS START_DATE, 
        DATE_FORMAT(END_DATE, "%Y-%m-%d") AS END_DATE,
        IF((DATEDIFF(END_DATE, START_DATE)+1) >= 30, "장기 대여", "단기 대여") AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE "2022-09-__"
ORDER BY HISTORY_ID DESC