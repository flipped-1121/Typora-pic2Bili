<center><h1>Typora-pic2Bili</h1></center>

回归到了Typora的怀抱，jsd国内的体验感下降，使用哔哩哔哩的图片服务作为~~图床~~。

## 🐍Python编写

python编写，结合Typora的costume command，使用简单的请求完成图片的上传并返回图床链接。

## 📑使用方法

下载：

+ [python版](https://github.com/flipped-1121/Typora-pic2Bili/raw/main/pic2Bili.py)
+ [Windows](https://github.com/flipped-1121/Typora-pic2Bili/releases)

使用：

+ 浏览器登陆哔哩哔哩，F12打开开发人员工具，点击应用程序、Cookie，获取SESSDATA。

  ![image-20220601203933135](https://i0.hdslb.com/bfs/album/a111cf2e90040b158c8d0cf51d102564b0e44bf3.png)

+ 配置Typora，点击“文件”--->“偏好设置”，设置图像。配置命令：

  + Python版本：

    ```she
    python <pic2Bili.py文件所在位置> <SESSDATA>
    ```

    例如：

    ```shell
    python ‪F:\Python\Pic2Bili\pic2Bili.py gfdsgsdfgsartewrr******
    ```

  + Windows：

    ```she
    <pic2Bili.exe文件所在位置> <SESSDATA>
    ```

    例如：

    ```she
    F:\Python\Pic2Bili\pic2Bili.exe gfdsgsdfgsartewrr******
    ```

    

  ![image-20220601204306720](https://i0.hdslb.com/bfs/album/9de8de05b31c0a6ab202039f28800c3de9ffe8c4.png)

## ✨Enjoy