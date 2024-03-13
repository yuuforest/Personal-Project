
-- Level 1

-- 의사의 이름, ID, 진료과, 고용일자
    -- 진료과가 흉부외과(CS)거나 일반외과(GS)인 의자
    -- 고용일자를 기준으로 내림차순 정렬, 고용일자가 같다면 이름을 기준으로 오름차순 정렬

SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, "%Y-%m-%d") as HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC

SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, "%Y-%m-%d") as HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD IN ('CS', 'GS')
ORDER BY HIRE_YMD DESC, DR_NAME ASC