/* change submit btn background color with screen over 576px
    from https://stackoverflow.com/questions/31916275/toggle-behaviour-based-on-screen-width */

$(window).on("load resize", function() {
    //Assuming you consider anything >= 1240 as desktop
    $('.target').toggleClass('bg-mycolor', $(window).width() > 575);
});
