$('.name').click(function (e) {
    $("#challenge").html("");
    var respid = $(this).attr('id');
    $.ajax({
        type: 'POST',
        url: '/cp/',
        data: {
            id: respid,
            choose: 'contests',
        },
        success: function (data) {
            console.log(data['contest'].length);
            for (let i = 0; i < data['contest'].length; i++) {
                var name = data['contest'][i]['name'];
                var start = data['contest'][i]['start'];
                var end = data['contest'][i]['end'];
                var duration = data['contest'][i]['duration'];
                var link = data['contest'][i]['link'];


                $('#challenge').append('<div class="contest">\n <div class="timer">\n <p class ="countdown" data-countdown="' + start + '"></p>\n<p>to go</p>\n</div>\n<div class="other">\n <div class="title">\n' + name + '\n</div>\n<div class="sed">\n<div class="sd">\n<p>Start</p>\n<p>' + start + '</p>\n</div>\n<div class="sd">\n<p >End</p>\n<p>' + end + '</p>\n</div>\n<div class="sd">\n<p>Duration</p>\n<p>' + duration + '</p>\n</div>\n</div>\n<div class="link">\n<a href="' + link + '" target="_blank">' + link + '</a>\n</div>\n</div>\n</div>');
            }
            if (data['contest'].length == 0) {
                if(respid==3){
                    $('#challenge').append('<div class="no-contest"> <p> No contests/Contest is going so cannot fetch </p> </div>');
                }
                else{
                    $('#challenge').append('<div class="no-contest"> <p> No contests / Network Error </p> </div>');
                }
            }
            $('[data-countdown]').each(function () {
                var $this = $(this), finalDate = $(this).data('countdown');
                $this.countdown(finalDate, function (event) {
                    $this.html(event.strftime('%D days %H:%M:%S'));
                });
            });
        },
        failure: function () {
            alert('Connection Error');
        }
    });
});


var mb = document.querySelector('.modal-btn');
var md = document.querySelector('.modal-bg');
var mc = document.querySelector('.modal-close');

mb.addEventListener('click', function () {
    md.classList.add('bg-active');
});

mc.addEventListener('click', function () {
    md.classList.remove('bg-active');
});

$('#sub_id').click(function (e) {
    if (document.getElementById('min').value.length == 0 || document.getElementById('max').value.length == 0 || document.getElementById('max').value.length == 0) {
        alert('Please fill the empty feilds');
    }
    else {
        $.ajax({
            type: 'POST',
            url: "/cp/",
            data: {
                min: $('#min').val(),
                max: $('#max').val(),
                username: $('#username').val(),
                tag: $('#tag').val(),
                choose: "prob"
            },
            beforeSend: function () {
                loadingShow();
            },
            success: function (data) {
                $('#loading').hide();
                if (data['prob'].length == 0) {
                    alert("No Questions Found/Connection Error Occured !");
                }
                else {
                    for (let i = 0; i < data['prob'].length; i++) {
                        window.open(data['prob'][i], '_blank');
                    }
                }
                document.getElementById('min').value = '';
                document.getElementById('max').value = '';
                document.getElementById('username').value = '';
                document.getElementById('tag').value = '';
            },
            failure: function () {
                alert("Error in your request, Try Agian !!");
            }
        });
    }
});
function loadingShow() {
    $('#loading').show();
}