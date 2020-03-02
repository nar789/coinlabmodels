const coin = require('./Coin')();

coin.mName = "testCoin";

coin.getPrice(null, ( prc ) => {
    console.log(`[${coin.mName}] : ${prc}BTC`);
});
/* expected output

    [testCoin] : 100BTC
    
*/