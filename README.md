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


