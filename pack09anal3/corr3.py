# data.go.kr 제공 관광정보 자료로 상관관계 분석
# 미국, 중국, 일본 관광객이 국내 유료관광지(5대 궁)방문

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

# 그래프 작성용 함수
def makeGraph(tour_table, all_table, tourPoint):
    # 계산할 관광지명에 해당하는 자료만 뽑아 외국인 관광객 자료와 합치기
    tour = tour_table[tour_table['resNm']==tourPoint]
    # print(tour)
    
    merge_table =pd.merge(tour, all_table, left_index=True, right_index=True)
    print(merge_table)
    
    #        resNm  ForNum   china   japan    usa
    # yyyymm                                     
    # 201101   창덕궁   14137   91252  209184  43065
    # 201102   창덕궁   18114  140571  230362  41077
    # 201103   창덕궁   28749  141457  306126  54610

    # 상관계수를 구하고 3개국 산포도 시각화 
    fig = plt.figure()
    fig.suptitle(tourPoint + '상관관계 분석')
    plt.subplot(1, 3, 1) # 1행 3열 첫번째 열
    plt.xlabel('중국인 입국자 수')
    plt.ylabel('중국인 입장객 수')
    lamb1 = lambda p:merge_table['china'].corr(merge_table['ForNum'])
    r1 = lamb1(merge_table)
    # print('r1 : ', r1)  # r1 :  -0.5834  - 음의 상관관계
    plt.title('r={:.5f}'.format(r1))
    plt.scatter(merge_table['china'], merge_table['ForNum'], alpha=0.8, s=6, c='red') # alpha 는 투명도
    
    plt.subplot(1, 3, 2) # 1행 3열 첫번째 열
    plt.xlabel('일본인 입국자 수')
    plt.ylabel('일본인 입장객 수')
    lamb2 = lambda p:merge_table['japan'].corr(merge_table['ForNum'])
    r2 = lamb2(merge_table)
    plt.title('r={:.5f}'.format(r2))
    plt.scatter(merge_table['japan'], merge_table['ForNum'], alpha=0.8, s=6, c='green') # alpha 는 투명도
    
    plt.subplot(1, 3, 3) # 1행 3열 첫번째 열
    plt.xlabel('미국인 입국자 수')
    plt.ylabel('미국인 입장객 수')
    lamb3 = lambda p:merge_table['usa'].corr(merge_table['ForNum'])
    r3 = lamb3(merge_table)
    plt.title('r={:.5f}'.format(r3))
    plt.scatter(merge_table['usa'], merge_table['ForNum'], alpha=0.8, s=6, c='blue') # alpha 는 투명도
   
    plt.tight_layout()
    plt.show()
    
    return[tourPoint, r1,r2,r3]
    
    

def goGo():
    # json 자료를 읽어 DataFrame에 담기
    fname = "서울특별시_관광지입장정보_2011_2016.json"
    jsonTP = json.loads(open(fname, mode='r', encoding='utf-8').read())  # json decoding - str을 -> dict로
    # print(jsonTP)
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm', 'resNm', 'ForNum')) # 년월, 관광지명, 입장객수
    tour_table = tour_table.set_index('yyyymm') # 연도를 기준으로 바꿈
    # print(tour_table)
    #             resNm  ForNum
    # yyyymm                   
    # 201101      창덕궁   14137
                
    resNm = tour_table.resNm.unique()
    # print('resNm(관광지명)', resNm)
    print('resNm(관광지명)', resNm[:5])  # ['창덕궁' '운현궁' '경복궁' '창경궁' '종묘']
    
    # 중국인 관광객 정보를 DataFrame에 담기
    cdf = '중국인방문객.json'
    cdata = json.loads(open(cdf, mode='r', encoding='utf-8').read())
    china_table = pd.DataFrame(cdata, columns=('yyyymm', 'visit_cnt'))
    china_table = china_table.rename(columns={'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    print(china_table)
    #         china
    # yyyymm        
    # 201101   91252
    # 201102  140571
    
    # 일본인 관광객 정보를 DataFrame에 담기
    jdf = '일본인방문객.json'
    jdata = json.loads(open(jdf, mode='r', encoding='utf-8').read())
    japan_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    japan_table = japan_table.rename(columns={'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
    print(japan_table)
    
    # 미국인 관광객 정보를 DataFrame에 담기
    udf = '미국인방문객.json'
    udata = json.loads(open(udf, mode='r', encoding='utf-8').read())
    usa_table = pd.DataFrame(udata, columns=('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns={'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
    print(usa_table)
    
    # 중국, 일본, 미국 DataFrame merge
    all_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    all_table = pd.merge(all_table, usa_table, left_index=True, right_index=True)
    # print(all_table[:5], '', len(all_table))
    
    r_list =[]
    for tourPoint in resNm[:5]:
        r_list.append(makeGraph(tour_table, all_table, tourPoint))

    r_df = pd.DataFrame(r_list, columns=('고궁명', '중국', '일본', '미국'))
    r_df = r_df.set_index('고궁명')
    
    print(r_df)
    
    # 고궁명별 3개국 상관계수로 시각화
    r_df.plot(kind='bar', rot=60)
    plt.show()
    
if __name__ == '__main__':
    goGo()

