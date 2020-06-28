$(".carousel").swipe({

    swipe: function (event, direction, distance, duration, fingerCount, fingerData) {

        if (direction == 'left') $(this).carousel('next');
        if (direction == 'right') $(this).carousel('prev');

    },
    allowPageScroll: "vertical"

});


$('#show-answer').click(() => {
    var anss = document.querySelector('.ans');
    if (anss.style.display == "none") {
        anss.style.display = "flex";
        $('#show-answer').html("Now You Know");
    }
    else {
        $('#show-answer').html("IDK");
        anss.style.display = "none";
    }
});