# CoinLab interface codes for bitmax
Need to fill todo codes using bitmax api.

====0224======
todolist

api_key와 api_secret을 python argument로 입력받을 수 있도록 해주세요.

```
    print("myorder: " + str(my_order.get_my_orders()))
    print("cancel: " + str(my_order.cancel_all()))
```

print코드들 아래에 샘플 출력 예시를 주석으로 같이 달아주면 읽어들일때 도움될듯~



==========
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


