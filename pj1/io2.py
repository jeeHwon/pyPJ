# def f1(n):
#     return n * 10
#
#
# a = f1
# # print(type(a))
# # print(a(7))
#
# # 람다함수 : 메모리절약, 가독성 향상, 코드 간결
# # lambda 매개변수 : 반환값
# b = lambda n: n * 10
# # print(b(1))
# def f2(x, y, f):
#     print(x*y*f(x+y))
# f2(2, 3, lambda n: n+1)
# print('\n'*40)
#
# # a = [1, 2, 3, 4 ,5] => [3, 6 ,9 ,12, 15]
# def f3(x):
#     result = []
#     for i in x:
#         result.append(i*3)
#     return result
#
#
# a = [1, 2, 3, 4, 5]
# print(f3(a))
# print(f3([2, 3, 4]))
# print('\n'*40)
#
# # map(함수명, 반복가능객체) : 매개변수로 함수와 반복가능 객체를 입력
# def f4(x):
#     return x*3
# print(f4(7))
# print(f4([4, 5, 6]))  # [4, 5, 6, 4, 5, 6, 4, 5, 6]
# print(map(f4, [4, 5, 6]))   # <map object at 0x0000004F31C85BB0>
# print(list(map(f4, [4, 5, 6]))) # [12, 15, 18]
# print(list(map(lambda n: n*3, [4, 5, 6])))  # [12, 15, 18]
# print('\n'*40)
#
# # 파일경로 : 리눅스 맥에서는/ 윈도우는 \
# # os 모듈 : 디렉토리, 파일등의 os 자원제어
# # glob 모듈
# import os
# print('현재 작업디렉토리', os.getcwd())
# print('현재 작업디렉토리의 목록', os.listdir())    #반환형 리스트
# print('D:\목록', os.listdir('d:\\'))
# print(os.listdir('D:\\down\\erd'))
# print(os.path.join('..', 'test1'))  # 경로 생성
# print(os.listdir(os.path.join('..', 'test1')))
# print(os.listdir(os.path.join('..', 'test1','Scripts')))
# with open('data\\webtoon.csv','w', encoding='utf-8') as f:
#     pass    #이렇게 쓰면 리눅스나 맥에선 오류나니까 밑에처럼 쓰면 다 쓸수 있다는이야기
# with open(os.path.join('data','webtoon.csv'),'w', encoding='utf-8') as f:
#     pass
# print('\n'*40)
#
# import glob
# print(glob.glob('*'))   #현재위치 모든파일 반환
# print(glob.glob('*.py'))    #현재위치 .py 파일 반환
# print('\n'*40)
# f1 = 'D:\\study\\pj1\\data\\Beauty.smi'
# print(os.path.dirname(f1))
# print(os.path.basename(f1)) #가장 마지막에 있는 이름(파일이든 디렉토리든)
# print('\n'*40)
# f = open(os.path.join('data', 'Beauty.smi'))
# # print(f.read())
# # print(f.readline())
# # print(f.readlines())
# # while True:
# #     line = f.readline()
# #     if not line:
# #         break
# #     print(line, end='')
# # f.close()
# # print('\n'*40)
#
# # data 폴더의 모든 파일 내용 출력
# filelist = glob.glob(os.path.join('data', '*'))
# print(filelist)
# for file in filelist:
#     with open(file, encoding='utf-8') as f:
#         if os.path.basename(file) != 'io2.py':
#             print(f.read())
#             print('-'*30)

# 'Beauty.smi' --[자막만]--> 'Beauty.txt'
def makeTxt(inputFile):
    f = open(inputFile, encoding='utf-8')
    result = []
    for line in f:
        line = line.replace('\n','')
        if len(line)<4:
            continue
        elif line.count('<')>1:
            continue
        line = line.replace('<b>','')
        line = line.replace('</b>', '')
        line = line.replace('<i>', '')
        line = line.replace('</i>', '')
        result.append(line)
    f.close()
    return result

def makeFile(inputFile, temp):
    fileName = inputFile[:-3] + 'txt'
    with open(fileName, 'w', encoding='utf-8') as fw:
        for t in temp:
            fw.write(t + '\n')


def main():
    inputFile = 'data\\The+Lord+Of+The+Rings+The+Fellowship+Of+The+Ring+2001+EXTENDED+1080p+BluRay+H264+AAC-RARBG.smi'
    # inputFile ='data\\Beauty.smi'
    temp = makeTxt(inputFile)
    makeFile(inputFile, temp)


if __name__=='__main__':
    main()






