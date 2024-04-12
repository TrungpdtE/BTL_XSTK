import pylab as plt
import matplotlib.image as mpimg
import numpy as np

#Chuyển đổi ảnh xám
def ConvertToGray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

 #Histogram
def HISTOGRAM(im):
    m, n = im.shape
    h = [0.0] * 256
    for i in range(m):
        for j in range(n):
            h[int(im[i, j] * 255 - 1e-5)] += 1
    return np.array(h) / (m * n)

# cumulative sum
def cumulative_sum(h):
    return [sum(h[:i + 1]) for i in range(len(h))]


def histmatch(photo, template):
    photo = photo / np.max(photo)
    template = template / np.max(template)
    h = HISTOGRAM(photo)
    h_template = HISTOGRAM(template)
    
    cdf = np.array(cumulative_sum(h))  
    cdf_template = np.array(cumulative_sum(h_template))
    photosecond = np.interp(photo, np.arange(256)/255.0, cdf_template)
    H = HISTOGRAM(photosecond)
    
    return photosecond, h, H, cdf

#lấy ảnh lên
img = mpimg.imread('b1.png')
template = mpimg.imread('b2.png')

#dùng hàm đổi ảnh sang xám
AnhgocGray = ConvertToGray(img)
gray_template = ConvertToGray(template)

#Cân bằng bd
anhmoi, _, _, _ = histmatch(AnhgocGray, gray_template)

# Thiết lập trong khoảng 0-1:
anhmoi = (anhmoi - np.min(anhmoi)) / (np.max(anhmoi) - np.min(anhmoi))


# hiển thị hình ảnh cũ và mới
plt.figure(figsize=(10, 10))

#HIỂN THỊ ẢNH
plt.subplot(231)
plt.imshow(AnhgocGray, cmap='gray')
plt.title('ẢNH CŨ')

plt.subplot(233)
plt.imshow(anhmoi, cmap='gray')
plt.title('ẢNH MỚI')

plt.subplot(232)
plt.imshow(gray_template, cmap='gray')
plt.title('ẢNH MẪU')


plt.show()

#HIỂN THỊ BIỂU ĐỒ HISTOGRAM

plt.subplot(231)
plt.hist(AnhgocGray.ravel(), bins=255, color='gray')
plt.title('BIỂU ĐỒ ẢNH GỐC')

plt.subplot(232)
plt.hist(gray_template.ravel(), bins=255, color='gray')
plt.title('BIỂU ĐỒ ẢNH MẪU')

plt.subplot(233)
plt.hist(anhmoi.ravel(), bins=255, color='gray')
plt.title('BIỂU ĐỒ ẢNH MỚI')

plt.show()