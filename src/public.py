from datetime import datetime
import pandas as pd



def seoul_active_pop():
    
    """
    서울시 생활인구 데이터와 행정동 코드 와 지명이 
    
    매핑된 테이블을 각각 가공하여 새로운 데이터프레임을 저장하는 함수
    
    """
    

    # data path
    data_path = '/Users/jeongseok/Documents/데이터/서울시생활인구데이터'

    # Loading
    seoul = pd.read_csv(f'{data_path}/서울시 생활인구데이터.csv',index_col=0)
    mapping = pd.read_csv(f'{data_path}/행정동 코드 매핑 테이블.csv',index_col=0)
    
    
    # 컬럼 에러 처리
    seoul = seoul.reset_index()
    col_lst = list(seoul.columns)[1:]
    col_lst.append('삭제')
    seoul.columns = col_lst
    new_lst = list(seoul.columns)[:-1]
    seoul = seoul[new_lst]
    
    # 데이터 타입 수정
    seoul[['기준일ID', '행정동코드']] = seoul[['기준일ID', '행정동코드']].astype(str)
    seoul['기준일ID'] = seoul['기준일ID'].apply(lambda x: datetime.strptime(x,'%Y%m%d'))
    
    # 지명 풀네임 컬럼 만들기
    mapping['sigunguName'] = mapping['sigunguName'].fillna('')
    mapping['hdongName'] = mapping['hdongName'].fillna('')
    mapping['totalName'] = mapping['sidoName'] +' '+ mapping['sigunguName'] + ' ' + mapping['hdongName']
    
    # 타입 변경
    mapping[['hdongCode', 'sigunguCode']] = mapping[['hdongCode', 'sigunguCode']].astype(str)
    
    # 서울시 데이터와 행정동 코드 맞추기
    mapping['hdongCode'] = mapping['hdongCode'].apply(lambda x: x[:-2])

    # 서울시데이터 최근날짜로 데이터 줄이기
    seoul = seoul[seoul['기준일ID']=='2022-03-31']
    seoul = seoul.reset_index(drop =True)
    
    # 필요한 컬럼만 분리
    mapping = mapping[['hdongCode','totalName']]
    
    # 데이터 합치기
    data = pd.merge(seoul, mapping, left_on ='행정동코드', right_on = 'hdongCode', how ='left' )
    
    # 컬럼재배치
    col1 = data.columns[0:2].to_list()
    col2 = data.columns[-2:].to_list()
    col3 = data.columns[3:-2].to_list()
    new_cols = col1+col2+col3
    data = data[new_cols]

    # 컬럼명 변경
    columns = {'hdongCode':'행정동코드', 'totalName':'지명'}
    data = data.rename(columns = columns)
    
    # 새로만든 데이터 저장
    data.to_csv(f'{data_path}/서울시 생활인구 매핑.csv')
