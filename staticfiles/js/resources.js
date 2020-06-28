
function more() {
    $('.more').click(function () {
        var topic_name = $(this).data('name');
        document.querySelector('.modal-bg').classList.add('bg-active');
        document.getElementById('topic_name').innerHTML = "";
        document.getElementById('res-content').innerHTML = "";
        document.body.style.overflow = "hidden";
        $.ajax({
            type: "POST",
            url: "/resources/",
            data: {
                name: topic_name,
            },
            success: function (data) {
                document.getElementById('topic_name').append(topic_name);
                var close = document.querySelector('.less');
                for (let i = 0; i < data['links'].length; i++) {
                    var type = data['links'][i].type;
                    var link = data['links'][i].link;
                    var desc = data['links'][i].desc;

                    $('#res-content').append('<div class="res-card">\n<div class="descp">\n<p>' + desc + '</p></div><div class="side"><a href = "' + link + '" target=_blank><p>' + type + '</p></a></div>');
                }
                close.addEventListener('click', () => {
                    document.body.style.overflow = "auto";
                    document.querySelector('.modal-bg').classList.remove('bg-active');

                });

                var modal = document.querySelector('.modal-bg');
                modal.addEventListener('transitionend', () => {
                    if ($(this).hasClass('bg-active')) return;
                })
            }
        });
    });
}
$(function () {
    more();
});
var search = document.getElementById('search');
var button = document.getElementById('button');
var input = document.getElementById('input');

String.prototype.format = function () {
    var i = 0, args = arguments;
    return this.replace(/{}/g, function () {
        return typeof args[i] != 'undefined' ? args[i++] : '';
    });
};

button.addEventListener('click', ajaxCall);

input.addEventListener('keydown', function () {
    if (event.keyCode == 13) ajaxCall();
});

function ajaxCall() {
    var value = document.getElementById('input').value;
    $.ajax({
        type: 'POST',
        url: '/resources/search/',
        data: {
            topic: value,
        },
        beforeSend: function () {
            search.classList.add('loading');
        },
        success: function (data) {
            search.classList.remove('loading');
            var ret = document.getElementById('top');
            document.querySelector('.naming').innerHTML = "<p>< All Resource topics ></p>";
            ret.innerHTML = "";
            html_to_append = '';
            var dt = data.topic;
            for (let i = 0; i < data.topic.length; i++) {
                html_to_append += '<div class="ind-topic">\n<div class="topic-name" id="{}">\n{}\n</div>\n<div class="more" data-name="{}">\n<p>&#10094</p>\n</div>\n</div>\n'.format(dt[i][1], dt[i][0], dt[i][0]);
            }
            ret.innerHTML = html_to_append;
            if(data.topic.length==0){
                document.querySelector('.naming').innerHTML = "<p>< No Topics Found ></p>";
            }
            more();
            console.log(data.topic);
        }
    });
}

$('#input').on('keyup', function () {
    var value = $(this).val();
    $.ajax({
        url: "/resources/autocomplete/",
        data: {
            'type': 'auto',
            'search': value
        },
        success: function (data) {
            list = data.list;
            $('#input').autocomplete({
                source: list,
                minLength: 2
            });
        }
    });
});