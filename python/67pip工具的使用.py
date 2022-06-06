# pip 是专门用来安装和卸载python相关拓展的工具
"""

pip - V  查看pip的版本信息


pip list 查看当前项目所有的python的扩展

python -m pip install --upgrade pip  更新pip版本

pip install some-package-name  安装某一个扩展 -i 国内镜像的名字
注意：在安装扩展的时候，一般我们会直接使用国内的镜像源提高我们的下载速度
    豆瓣的镜像源：https://pypi.doubanio.com/simple/

pip show 扩展名  查看扩展先关信息

pip uninstall 扩展名  卸载相关扩展
"""

# 第二种操作相关扩展的方式：
"""
通过编辑器实现：文件-设置-项目-python解释器
        + ：安装扩展包
        - ：卸载扩展包
"""