/** MyOrders.js
 * @author #f1xa11
 * @version 1.0.0
 * 2020.03.09
 */
;(module.exports = function () {

    var mOrders = [];

    function Order () {
        var id; // primary key
        var type; // buy or sell
        var name; //coin name
        var count;
        var price; //btc
        var amount; // dollar $
        var state; //processed or not, {"req","doing","done"}
    }

    /**
    * @param   config  ; This is uniq setting keys of bitmax.
    * @return   task is cool? "success" : "fail"
    */
    function loadMyOrders (config){
        // todo
        /*
         connect using config
         and for(o1 in loadedOrders) { 
            var o2 = new MyOrders.Order();
            o2.id = o1.id;
            o2.type = o1.type;
            o2.name = o1.name;
            o2.count = o1.count;
            o2.price = o1.price;
            o2.amount = o1.amount;
            o2.state = o1.state;
            mOrders.push(o2);
        }
        */
        /* usage
            var res = loadMyOrders(config);
         */
        return "success";
    }

    function getMyOrders () { //need it for more fast load.
        return mOrders;
    }

    /**
    * @param   config  ; This is uniq setting keys of bitmax.
    * @param   id  ; Order primary key.
    * @return   task is cool? "success" : "fail"
    */
    function cancelOrder (config, id) {
        //todo
        //cancel order by using id.
        return "success";
    }

    return {
        Order : Order,
        loadMyOrders : loadMyOrders,
        getMyOrders : getMyOrders,
        cancelOrder : cancelOrder,
    }

})();



