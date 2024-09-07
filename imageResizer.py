import cv2

source="image_anime_girl.jpg"
destination="new_anime.jpg"
percent=20

image=cv2.imread(source)
width=int(image.shape[1]*(1+(percent/100)))
height=int(image.shape[0]*(1+(percent/100)))
dsize=(width,height)
output=cv2.resize(image,dsize)
cv2.imwrite(destination,output)
cv2.imshow("new_anime",image)
cv2.waitKey(0)
cv2.destroyAllWindows() 