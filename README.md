# 專案名稱: worktest
## 設定 
1. 導入com.mysql.jdbc.Driver
   * 更改 build.gradle(:app) 其中的專案位置
   > implementation fileTree(dir: '專案位置\\app\\libs',include: ['*.aar', '*.jar'], exclude: [])
   > implementation files('libs\\mysql-connector-java-5.1.49-bin')
   * 驅動包可從mysql官網下載
## code說明    
1. tool.MysqlCon: 接資料庫phpmyadmin
  * 資料庫在自己電腦上的話，開xampp連接
    > 解壓縮資料庫後點擊setup_xampp更新路徑
  * IP改成自己網路
    > (Windows)開啟命令提示字元,輸入 ipconfig 取得ip
  * 資料庫建user: test  密碼: 0123
  * 載入到手機的話要與資料庫在同一網路才可連線
2. tool.ListAdapter_Customer: 工具,顧客相關頁面滑動瀏覽list用
3. tool.ListAdapter_store: 工具,餐廳相關頁面滑動瀏覽list用
4. Object_storeInfo
5. GlobalVar: 當前使用者資訊暫存變數

## 頁面說明
各區域以一個Activity為主體,以navigate切換展示的Fragment

- 帳戶相關: Login(Activity)
1. Fragment_Login: 原MainActivity,登入註冊介面
2. Fragment_Register_customer: 顧客註冊,註冊完導引至 customer.Browse
3. Fragment_Register_store: 餐廳註冊,註冊完導引至 store.Store
4. ChangePassword:原MemberActivity,更改密碼
5. 登入後的上方標題欄點擊名字可察看註冊時填寫的訊息,右方有Menu選單(帳戶),可以切換到其他頁面
6. 可切換帳戶

- 餐廳方使用: Store(Activity)
1. Fragment_ShowMenu: 瀏覽菜單
2. Fragment_ShowComment: 後台數據
3. Fragment_EditMenu: 編輯菜單 
4. Fragment_BasicInfo_store:顯示餐廳註冊時的資訊
5. Fragment_EditInfo_store:修改餐廳資訊


- 消費者方使用: BrowsePage(Activity)
1. Fragment_Table: 原TableActivity餐桌功能(好友功能)
2. Fragment_Overview:餐廳總覽,根據點選的餐廳類型顯示居住地週邊的餐廳
3. Fragment_StoreInfo: 各店家的詳細資訊顯示頁
4. Fragment_BasicInfo_cus:顯示顧客註冊時的資訊
5. Fragment_EditInfo_cus:修改顧客資訊
6. Fragment_Recommend: 根據個人或是與選定朋友的偏好(註冊時填寫的資訊)進行推薦



  
