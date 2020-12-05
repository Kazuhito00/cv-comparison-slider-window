# cv-comparison-slider-window
2枚の画像を重ね合わせて、マウススライドで比較するウィンドウのサンプルです。<br>
![bu19j-mplzq](https://user-images.githubusercontent.com/37477845/99143014-9cf5af80-269d-11eb-9eb0-c872d5a5f74c.gif)

# Requirement 
* OpenCV 3.4.2 or later

# Demo
デモの実行方法は以下です。
```bash
python sample.py
```

# How to use
以下の流れで呼び出してください。<br>
CvComparisonSliderWindowクラス作成時には、ウィンドウ名、スライダー上のライン色、ライン太さを指定出来ます。<br>
省略した場合は、それぞれ'debug'、(255, 255, 255)、1になります。

```python
from cv_comparison_slider_window import CvComparisonSliderWindow

cvwindow = CvComparisonSliderWindow(
    window_name='debug',
    line_color=(255, 255, 255),
    line_thickness=1,
)
# [省略]

while True:
    # [省略]

    cvwindow.imshow(image1, image2)
    key = cv.waitKey(1)
```

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
cv-comparison-slider-window is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
