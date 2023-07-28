import multiprocessing

def pro1(ml ,pn):
    ml.append('p1')
    print(f"{pn} 현재 리스트의 값: {ml}")
def pro2(ml ,pn):
    ml.append('p2')
    print(f"{pn} pro2함수에서 리스트의 값을 추가했습니다. {ml}")

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    manager_list = manager.list() # create emtpy list []
    # manager_dict = manager.dict()

    print(f"manager_list의 초기값: {manager_list}")

    p1= multiprocessing.Process(target=pro1, args=(manager_list,'p1'))# 함수명 , 함수의 매개변수 -> 여기서는 manager_list ,즉 emtpy list [] 
    p2= multiprocessing.Process(target=pro2, args=(manager_list,'p2'))# 함수명 , 함수의 매개변수
    p1.start()
    p2.start()
    p1.join()
    p2.join()

# manager_list의 초기값: []
# p1 현재 리스트의 값: ['p1']
# p2 pro2함수에서 리스트의 값을 추가했습니다. ['p1', 'p2']