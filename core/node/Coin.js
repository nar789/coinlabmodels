/** Coin.js
 * @author #f1xa11
 * @version 1.0.0
 * 2020.03.03
 */
;(module.exports = function(){


    const exec = require('child_process').execSync;

    
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
        var prc = parseInt(exec('python ../py/Coin.py'));
        callback(prc);
    }

    return {
        mName : mName,
        getPrice : getPrice,
    }

})();



