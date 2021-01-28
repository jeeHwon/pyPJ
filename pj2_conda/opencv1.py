# pip install opencv-python
import cv2
import matplotlib.pyplot as plt

# 이미지 데이터 핸들링
# img = cv2.imread('img\\suzy.jpg')                # 이미지 읽기
# print(img)
# print(type(img))                                 # numpy 배열
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # matplotlib 색순서 RGB => opencv 색순서 BGR
# plt.axis('off')                                  # 축 제거
# plt.show()
# cv2.imwrite('img\\suzy2.png', img)               # 이미지 저장 
# img2 = cv2.resize(img,(350,500))                 # 이미지 크기 변경
# cv2.imwrite('img\\suzy3.png', img2)
# plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
# plt.show()

# 이미지 자르기
# img3 = img[300:1100, 400:1200]
# img3 = cv2.resize(img3,(800,800))
# plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
# plt.show()

# https://github.com/opencv/opencv/tree/master/data/haarcascades -> face database
# cascadefile = 'face.xml'
# cascade = cv2.CascadeClassifier(cascadefile)
# img = cv2.imread('img\\suzy.jpg')
# # img = cv2.imread('img\\son.jpg')
# img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   # 그레이스케일로 변환: 이미지 내부의 명암을 기반으로 얼굴인식
# faces = cascade.detectMultiScale(img2, minSize=(700,700))
# faces = cascade.detectMultiScale(img2, minSize=(13,13))
# print(type(faces))  # 넘파이 배열
# print(len(faces))   # 인식한 얼굴의 수
# if len(faces)==0:
#     print('얼굴인식 실패')
#     quit()
# print(faces)

# 얼굴인식 부분 표시
# for x,y,w,h in faces:
#     print('얼굴좌표=',x,y,w,h)
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=5) # 이미지, 시작좌표, 끝좌표, 선색깔, 선두께
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()

# 모자이크 처리
def mosaic(img, rect, size):    # 이미지, (시작좌표, 끝좌표), 축소시킬 픽셀
    x1,y1,x2,y2 = rect          # 시작좌표(x1,y1), 끝좌표(x2,y2)
    r1 = img[y1:y2,x1:x2]
    r1 = cv2.resize(r1,(size,size)) # 이미지 축소
    r1 = cv2.resize(r1,(x2-x1,y2-y1),interpolation=cv2.INTER_AREA)  # 원래 사이즈로 조정
    img[y1:y2,x1:x2] = r1
    return img

img = cv2.imread('img\\snsd2.jpg')
cascadefile = 'face.xml'
cascade = cv2.CascadeClassifier(cascadefile)
faces = cascade.detectMultiScale(img, minSize=(13,13))
for x,y,w,h in faces:
    print('얼굴좌표=',x,y,w,h)
    img = mosaic(img,(x,y,x+w,y+h),10 )
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()