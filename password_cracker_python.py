#알파벳출력하기_string module =>문자 가져오기
import string

string.ascii_lowercase # 소문자 
string.ascii_uppercase # 대문자
string.ascii_letters #대소문자 모두
string.digits # 숫자


#sequence 멤버 하나로 이어붙이기_join
my_list= ['1','100','33']
answer=''.join(my_list)

#random.sample(pop,k): pop에서 랜덤하게 k개 뽑음
#random.shuffle:순서형 자료(sequence)를 뒤죽박죽으로 섞어놓는 함수

#append: 목록에서 원소추가
prime = [2, 3, 7, 11]
prime.append( 5 )
#sort: 리스트 내부에서 정렬(리스트형에만 가능)
prime.sort()
#sorted(list,key,reverse=True) :원래 값을 유지하면서 정렬된 결과를 반환
    #key 파라미터(비교를 하는 기준)  함수, 1입력값 1반환값 
#del: 원소제거
del prime[4] 



















    
        






