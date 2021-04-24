/* change submit btn background color with screen over 576px
    from https://stackoverflow.com/questions/31916275/toggle-behaviour-based-on-screen-width */

$(window).on("load resize", function() {
    //register and login btn change color with screen > 575px
    $('.target').toggleClass('bg-mycolor', $(window).width() > 575);
    $('.btn2').toggleClass('mt-5', $(window).width() < 767);
});

