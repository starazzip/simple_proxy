# Simple Proxy

基於 proxy.py 的 HTTP Proxy，使用 Basic 認證機制保護連線安全。

## 功能
* 基於 proxy.py 的 HTTP Proxy
* 支援 Basic Authentication（帳號密碼驗證）
* 可自訂帳號密碼，透過 .env 檔管理

## 安裝需求
```
poetry shell
poetry install
```

## .env 設定
複製.env.example重新命名為.env，內容如下：
PROXY_USERNAME=xxxx
PROXY_PASSWORD=xxxx


## 啟動方式
在專案根目錄下執行以下指令：
```
python -m proxy --hostname 0.0.0.0 --port 8899 --plugins  auth_plugin.AuthPlugin
```

其中：
* --hostname 0.0.0.0 允許外部設備連線
* --port 8899 指定 Proxy 使用的通訊埠
* --plugins  auth_plugin.AuthPlugin 簡單的帳密驗證插件


## curl 測試：
```
curl -x http://localhost:8899 https://httpbin.org/ip --proxy-user username:password
```