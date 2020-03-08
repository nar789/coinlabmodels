const order = require('../Order')();

const buyingResponse = order.buy(null,2000,30);
console.log("buying response : " + buyingResponse);

const sellingResponse = order.sell(null,3000,30);
console.log("selling response : " + sellingResponse);

/* expected output

    buying response : success
    selling response : success
    
*/