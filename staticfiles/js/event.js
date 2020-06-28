$('.news').click(function (e) {
    document.querySelector('.modal-bg').classList.add('bg-active');
    $('#pop-up').html("");
    var event_id = $(this).data('event-id');
    var urlap = $('#name').data('event-type');
    if (urlap === "Upcoming Events") {
        urlap = 'upcoming_events';
    } else if (urlap == "Events Today") {
        urlap = 'today_events';
    } else {
        urlap = 'past_events';
    }
    var url = "/events/" + urlap;
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            id: event_id,
        },
        success: function (data) {
            var html_to_write = "";
            html_to_write += '<div class="modal-close" id="close">+</div><p id= "eve_name" >' + data['event']['name'] + '</p> <p id="eve_desc">' + data['event']['description'] + '</p> <p id="eve_date">' + data['event']['date'] + '</p>';
            html_to_write += '<p id= "rd">Registration Date : ' + data['event']['registration_date'] + '</p>'
            if (data['event']['can_register']) {
                html_to_write += '<p id="rl">&#128073 &nbsp &nbsp Register Now : <a href="' + data['event']['registration_link'] + '" id="rl">' + data['event']['registration_link'] + '</a></p>';
            }
            if (data['event']['feedback_link']) {
                html_to_write += '<p id="fl">&#129309 &nbsp &nbsp Give Feedback : <a href="' + data['event']['feedback_link'] + '" id="fl">' + data['event']['feedback_link'] + '</a></p>';
            }
            if (data['event']['photos_link']) {
                html_to_write += '<p id="pl">&#9996 &nbsp &nbsp Photo Gallery : <a href="' + data['event']['photos_link'] + '" id="pl">' + data['event']['photos_link'] + '</a></p>';
            }
            document.getElementById("pop-up").innerHTML = html_to_write;
            var close = document.querySelector('#close');
            close.addEventListener('click', () => {
                document.querySelector('.modal-bg').classList.remove('bg-active');
            });
        }
    });
});
