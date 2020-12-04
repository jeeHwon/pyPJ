1. Analyzer 못 찾을때
    Analyzer.py 파일을 가상환경 라이브러리에 Investar 폴더에 넣어놓자


2. plt 에서 한글 font깨질때
    >>> import matplotlib
    >>> matplotlib.__file__
    로 경로 알아낸 후 mpl-data에 matplotlibrc 파일 노트패드로 연 후 
    #font.family:  {} 이 부분에 사용가능한 폰트 입력

