# <식품 유통기한 관리 O2O 서비스 플랫폼>
**data**
- 레시피 : https://kadx.co.kr/product/detail/0c5ec800-4fc2-11eb-8b6e-e776ccea3964
- 바코드 : 
http://www.foodsafetykorea.go.kr/api/openApiInfo.do?menu_grp=MENU_GRP31&menu_no=661&show_cnt=10&start_idx=1&svc_no=C005
https://www.foodsafetykorea.go.kr/api/openApiInfo.do?menu_grp=MENU_GRP31&menu_no=656&show_cnt=10&start_idx=1&svc_no=I2570&svc_type_cd=API_TYPE06


## 팀원 및 역할
<img width="344" alt="image" src="https://user-images.githubusercontent.com/99347825/204076260-889c5274-51bb-49b3-a3e7-6be1409e3364.png">

## 구현 기능
1. 구매 식자재 **등록 및 관리**
    - 등록한 식자재의 남은 유통기한, 소비기한을 실시간으로 확인 가능
2. 냉장고 속 식재료를 이용한 레시피 추천

## Why, 프로젝트를 기획하게 되었는지?
1. 식품 소비기한 표시제 도입
    - 2023년 1월 1일자로 유통기한이 폐지되고 소비기한으로 바뀜(유제품 제외)
2. 환경오염의 주범: 음식물쓰레기 과다배출
3. 인플레이션에 따른 **식자재 구매비용 증가**
4. 유통기한 관리 소홀로 인해 식품 폐기 비용 증가

## How, 프로젝트를 구현하였는지?
- 데이터 수집
    - 공공데이터포털, 식약처 공공데이터 API를 이용하여 데이터 수집
- SQL DB에 적재 후 파이썬을 이용한 데이터 전처리
    - DB 적재 과정
    - 파이썬을 이용하여 Raw Data 전처리
- 구매 식자재 등록 및 관리
    - 등록한 식자재의 남은 유통기한, 소비기한을 실시간으로 확인 가능
    - 키워드 추출을 이용한 레시피 추천
- 유통기한이 임박한 식재료에 대한 레시피 추천 서비스

## What, 프로젝트를 통해 기대 할 수 있는지?
1. 2023년 1월 1일 자로 바뀌는 **식품 소비 기한 표시 제도 안내**
2. 유통기한이 짧은 식재료의 유통기한을 관리하여 **식품 폐기 비용 감소 효과**를 얻을 수 있음
3. **음식물 폐기를 줄여** 탄소 배출량 절감 및 소각, 매립 비용 절감
4. **폐기율이 높은 식재료를 파악**하여 **구매량 조절**
5. 무분별한 지출을 줄여, 식자재 가격 급등에 대비한 **비용 절감**

## 프로젝트 파이프라인
![image](https://user-images.githubusercontent.com/99347825/204075991-9710a6c8-2d6f-4238-9cc6-c511fd0e17c3.png)

## DB 관계도
![image](https://user-images.githubusercontent.com/99347825/204076036-8f0b14b7-24d5-4b7d-be0d-b99b663e6c13.png)
