# 과제 사람의 얼굴을 인식하여 얼굴부분 모자이크 처리하여 이미지를 저장하세요
# 소스와 이미지 제출
import cv2
import matplotlib.pyplot as plt

# 처리할 이미지 지정
filename = 'monkey.jpg'
savename = filename[:filename.find('.')]

# mosaic 함수 정의
def mosaic(img, rect, size):   
    x1,y1,x2,y2 = rect         
    r1 = img[y1:y2,x1:x2]
    r1 = cv2.resize(r1,(size,size)) 
    r1 = cv2.resize(r1,(x2-x1,y2-y1),interpolation=cv2.INTER_AREA)
    img[y1:y2,x1:x2] = r1
    return img

# 이미지 읽어 얼굴인식
img = cv2.imread('img\\{}'.format(filename))
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cascadefile = 'face.xml'
cascade = cv2.CascadeClassifier(cascadefile)
faces = cascade.detectMultiScale(img2, minSize=(13,13))
print('인식된 얼굴의 수:',len(faces))

# 인식된 좌표에 모자이크 함수 적용 후 저장
for x,y,w,h in faces:
    print('얼굴좌표=',x,y,w,h)
    img = mosaic(img,(x,y,x+w,y+h),10)
cv2.imwrite('img\\{}_mosaiced.jpg'.format(savename), img) 
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()