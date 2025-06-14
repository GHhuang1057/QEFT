# QEFT(基于开源项目edl的GUI高通刷机程序)

# 目前处于开发阶段，可能无法使用

## 本项目基于[edl](https://github.com/bkerler/edl)开源项目开发，遵守GPL-V3开源协议

## ZH_CN/[English](EN_README.md)

### 项目简介

#### QEFT是一个基于开源项目edl的GUI高通刷机程序，旨在简化高通设备的刷机过程。QEFT使用Python编写，使用PyQt5作为GUI框架，提供了一个直观的用户界面，方便用户进行刷机操作。
#### 结构（开发说明）
- main.py：主程序，负责启动GUI界面
- core文件夹:核心逻辑（待编写）
- ui文件夹：存放GUI界面的设计文件
- - qeft_main_window.py：主窗口的设计文件
- - qeft_start_window.py：启动窗口的设计文件
- res文件夹：存放资源文件
- - edl文件夹：存放edl项目文件

### 开发说明
可以参考API文档
[BK_EDLClient_API文档](BK_EDLVLIENT_API_README.md)
~~~
注意：本项目基于开源项目edl开发，项目代码中未包含edl项目的代码，刷机前请先下载/克隆edl项目并将其放入edl文件夹中。

cd res
git clone https://github.com/bkerler/edl.git
pip3 install -r requriements.txt
~~~

## 开发目标：2025/6/14更新
### 本次开发目标
#### 完善设备识别和加载逻辑（可以参考edl仓库readme和api文档）
#### 完善主界面（qeft_menu_window.py/menu.ui）
### 截至到7/05日
---

### 食用说明
[BK_EDLClient_API文档](BK_EDLVLIENT_API_README.md)

### 贡献
#### *630*
#### *kirin7098*
#### *huang1057*
~~~
+ 基于https://github.com/bkerler/edl的开源项目开发，遵守GPL-V3开源协议
~~~
#### 欢迎贡献代码