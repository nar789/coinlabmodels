# CoinLab interface codes 
hi hello this is Coinlab interface 

### todolist
    [200419]
    python core안되서 docker로 포팅하는게 안정적일 듯

    [200224]
    api_key와 api_secret을 python argument로 입력받을 수 있도록 해주세요.

    ```
        print("myorder: " + str(my_order.get_my_orders()))
        print("cancel: " + str(my_order.cancel_all()))
    ```
    print코드들 아래에 샘플 출력 예시를 주석으로 같이 달아주면 읽어들일때 도움될듯~


### Keyword map
    1. MyPosition
        - mScale; 규모 
        - mProfit; 이익
        - mLeverage; 레버리지?
        - marketPrice; 시장가격
        - mTodayProfit; 금일가격?
        - mSumupProfit; 총이익?

    2. Order
        - id; // primary key
        - type; // buy or sell
        - name; //coin name
        - count;
        - price; //btc
        - amount; // dollar $
        - state; //processed or not, {"req","doing","done"}

### Db scheme	

    1. 사용자	user
            - id int primary key auto_increment
            - email varchar(255)
            - name varchar(20)
            - password varchar(255) sha
            - api_key varchar(255)
            - api_secret varchar(255)

    2. 코인가격	coin
            - reg_datetime
            - market_price
            - ??
            - ??
            - ??
            - 체결가를따로?
    
    3. 주문내역	order
            - id
            - uid
            - ??
            - ??
            - ??
            - ??
            - ??

### BaseClasses
    1. Coin
        ```
        [Coin]

        /*attribute*/
        + String name;

        /*method*/
        + void getPriceCallback (price)
        + void getPrice ( config, getPriceCallback )
        ```

    2. Order
        ```
        [Order]

        /*method*/
        + Response Buy(config, price, count)
        + Response Sell(config, price, count)
        ```

    3. MyOrders
        ```
        [MyOrders]

        /*inner class*/
        + Order : Order

        /*method*/
        + loadMyOrders (config)
        + getMyOrders ()
        + cancelOrder (config, id)
        ```

    4. MyPosition
        ```
        [MyPosition]

        /*attribute*/
        + var mScale;
        + var mProfit;
        + var mLeverage;
        + var marketPrice;
        + var mTodayProfit;
        + var mSumupProfit;

        /*method*/
        + loadPositon (config)
        ```

