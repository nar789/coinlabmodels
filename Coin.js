/** Coin.js
 * @author #f1xa11
 * @version 1.0.0
 * 2020.03.03
 */
;(module.exports = function(){

    
    var mName; // Coin's name.
    
    /**
    * @param   config  ; This is uniq setting keys of bitmax.
    * @param   callback  ; callback about realtime coin's price.
    * @return   void.
    * @usage
            getPrice(config, (prc)=>{
                //{prc} is realtime coin price;
            });
    */
    function getPrice (config, callback) {
        //todo.

        callback(100);//Just test code. Need to remove this line. 
    }

    return {
        mName : mName,
        getPrice : getPrice,
    }

})();



