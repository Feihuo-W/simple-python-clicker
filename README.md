<img width="1186" height="1030" alt="011ed4d71fbca857020e1d3ce974eb03" src="https://github.com/user-attachments/assets/d254188e-34e8-4560-a210-377a5d35eacf" /># simple-python-clicker
My first Python tool, inspired by MouseClick  
# Simple Python Auto Clicker (简易 Python 连点器) 🖱️

这是一个基于 Python 编写的轻量级鼠标连点器。它也是我的第一个 GitHub 开源项目！🚀
<img width="1186" height="1030" alt="011ed4d71fbca857020e1d3ce974eb03" src="https://github.com/user-attachments/assets/7d4dfb64-6c2d-42cb-8f0a-8b8d4cd5d016" />


## ✨ 功能特点

这个仓库包含两个版本的连点器：

1.  **普通版 (`clicker.py`)**:
    *   基于 `pyautogui` 库。
    *   简单稳定，适合日常使用。
    *   代码逻辑清晰，适合新手学习。
2.  **极速版 (`fast_clicker.py`)**:
    *   基于 Windows 底层 API (`ctypes`)。
    *   **速度极快**（可达 500+ CPS），适合压力测试。
    *   占用资源更少。

## 🛠️ 安装依赖 (Prerequisites)

在运行代码之前，你需要安装 Python，并安装以下依赖库：

```bash
pip install keyboard pyautogui
