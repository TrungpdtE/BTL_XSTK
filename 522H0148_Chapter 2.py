import matplotlib.image as mpimg
import pylab as plt
import numpy as np

#ĐỔI ẢNH MÀU SANG XÁM
def ConvertToGray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

#BIỂU ĐỒ CHUẨN HOÁ
def HISTOGRAM(im):
    m, n = im.shape
    h = [0.0] * 256
    for i in range(m):
        for j in range(n):
            h[int(im[i, j])] += 1
    return np.array(h) / (m * n)

 # tìm tổng tích lũy
def cumulative_sum(h):
    return [sum(h[:i + 1]) for i in range(len(h))]

# Hàm phân phối tích lũy: CDF
def EQUALIZATION(photo):
    #check ảnh xám
    if len(photo.shape) == 3:
        photo = ConvertToGray(photo)
    d, r = photo.shape
    h = HISTOGRAM(photo)
    cdf = np.array(cumulative_sum(h))  
    img = np.uint8(255 * cdf)  
    Y = np.zeros_like(photo)
    for i in range(0, d):
        for j in range(0, r):
            Y[i, j] = img[int(photo[i, j])]
    H = HISTOGRAM(Y)
    return Y, h, H, img

#Chuyển sang kdl Unit8
img = np.uint8(mpimg.imread('abc.png') * 255.0)
gray_img = img

new_img, h, new_h, img = EQUALIZATION(gray_img)

#print
plt.subplot(121)
plt.imshow(gray_img, cmap='gray')
plt.title('ẢNH GỐC')

plt.subplot(122)
plt.imshow(new_img, cmap='gray')
plt.title('ẢNH KHI CÂN BẰNG')

plt.show()

fig = plt.figure()
fig.add_subplot(221)
plt.plot(h)
plt.title('BIỂU ĐỒ GỐC')

fig.add_subplot(222)
plt.plot(new_h)
plt.title('HISTOGRAM EQUALIZATION') 

plt.show()