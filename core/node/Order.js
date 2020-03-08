/** Order.js
 * @author #f1xa11
 * @version 1.0.0
 * 2020.03.03
 */
;(module.exports = function(){

    /**
    * @param   config  ; This is uniq setting keys of bitmax.
    * @param   prcie  ; buying price
    * @param   count  ; buying count
    * @return   task is cool? "success" : "fail"
    */
    function buy (config, price, count) {
        //todo

        return "success";//Just test code. Need to remove this line. 
    }


    /**
    * @param   config  ; This is uniq setting keys of bitmax.
    * @param   prcie  ; selling price
    * @param   count  ; selling count
    * @return   task is cool? "success" : "fail"
    */
    function sell (config, price, count) {
        //todo

        return "success";//Just test code. Need to remove this line. 
    }

    

    return {
        buy : buy,
        sell : sell,
    }

})();



