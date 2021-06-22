$(".date-container").click(function() {
    var select = $(this);

    select.addClass("open").next(".date-dropdown").slideDown(100).addClass("open");

    $(document).mouseup(function(e){
        var seting = $(".date-dropdown");
        if(seting.hs(e.target).length === 0) {
            seting.removeClass("open").slideUp(100);
            select.removeClass("open")
        }
    })
})