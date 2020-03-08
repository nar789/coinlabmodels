# CoinLab interface codes for bitmax
Need to fill todo codes using bitmax api.

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


