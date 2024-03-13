
-- Level 1

-- 환자 이름, 번호, 성별코드, 나이, 전화번호
    -- 12세 이하인 여자 환자
    -- 전화번호가 없는 경우 'NONE' 출력
    -- 나이를 기준으로 내림차순 정렬, 나이가 같다면 환자이름을 기준으로 오름차순 정렬

SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE')
FROM PATIENT
WHERE GEND_CD = 'W' 
    AND AGE <= 12
ORDER BY AGE DESC, PT_NAME ASC