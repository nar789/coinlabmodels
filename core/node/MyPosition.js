/** MyPosition.js
 * @author #f1xa11
 * @version 1.0.0
 * 2020.03.09
 */
;(module.exports = function () {

    /* public variables for fast view load */
    var mScale;
    var mProfit;
    var mLeverage;
    var marketPrice;
    var mTodayProfit;
    var mSumupProfit;

    /**
    * @param   config  ; This is uniq setting keys of bitmax.
    * @return   task is cool? "success" : "fail"
    */
    function loadPositon (config) {
      /*
      connect api server by using config 
      and just setter.
      mScale = loadData.scale;
      ...
       */
      return "success";  
    }

    return {
        /* public variables for fast view load*/
        mScale : mScale,
        mProfit : mProfit,
        mLeverage : mLeverage,
        marketPrice : marketPrice,
        mTodayProfit : mTodayProfit,
        mSumupProfit : mSumupProfit,

        loadPositon : loadPositon,
    }

})();



