# RyoheyMeeting
遼平会のポータルサイト

# 目的
３か月に一回行われる遼平会を円滑に，かつ楽しく開催するのを補助すること

# 機能
- リアクション機能
  - WebSocketによって，リアクションをリアルタイムに共有する
- ユーザ登録
  - ユーザ登録し，当日の発表時にリアクションをもらう
- 会議の登録
  - 会議をデータベースで管理

# ページ例
## ホーム
![image](https://user-images.githubusercontent.com/26971566/122384007-44c1bb80-cfa6-11eb-9833-bbfd4f87459c.png)
## リアクションボタンページ
![image](https://user-images.githubusercontent.com/26971566/148137206-165085db-a184-4cbc-ac6b-65d8fcd7b8c2.png)  
このページで画像をタップするとリアクションが送信される
## リアクション受信ページ
![image](https://user-images.githubusercontent.com/26971566/148137341-25559093-ea73-49fc-91dc-f03624c5134d.png)
画像はリアクションスタンプが表示されてからフェードアウトする途中のもの

# 使用技術
- DJango (Python)
- ASGIによるWebSocket
- HTML
- JavaScript
- SCSS
- Bootstrap
