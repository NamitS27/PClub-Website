var observe;
if (window.attachEvent) {
    observe = function (element, event, handler) {
        element.attachEvent("on" + event, handler);
    };
} else {
    observe = function (element, event, handler) {
        element.addEventListener(event, handler, false);
    };
}
function init() {
    var text = document.getElementById("message");
    function resize() {
        text.style.height = "auto";
        text.style.height = text.scrollHeight + "px";
    }
    function delayedResize() {
        window.setTimeout(resize, 0);
    }
    observe(text, "change", resize);
    observe(text, "cut", delayedResize);
    observe(text, "paste", delayedResize);
    observe(text, "drop", delayedResize);
    observe(text, "keydown", delayedResize);

    text.focus();
    text.select();
    resize();
}


$('.contact-form-btn').click(async function () {
    var name = $('#name').val();
    var email = $('#email').val();
    var subject = $('#subject').val();
    var message = $('#message').val();
    var check = "No";
    var valid = "";
    if ($('#jw').prop("checked") == true) {
        check = "Yes";
    }
    valid = await checkEmail(email);
    if (document.getElementById('name').value.length == 0 || document.getElementById('email').value.length == 0 || document.getElementById('subject').value.length == 0 || document.getElementById('message').value.length == 0) {
        alert('Please fill the empty feilds');
    }
    else if (valid === "No") {
        alert("Enter Valid Email ID");
    }
    else {
        $.ajax({
            type: 'POST',
            url: '/contact_us/',
            data: {
                name: name,
                email: email,
                subject: subject,
                message: message,
                jw: check,
            },
            success: function (data) {
                if (data['done'] == "Send") {
                    alert('Message Sent');
                    document.getElementById('name').value = "";
                    document.getElementById('email').value = "";
                    document.getElementById('subject').value = "";
                    document.getElementById('message').value = "";
                    $('#jw').prop("checked", false);
                }
                else {
                    alert('Connection error ! Try Again :(');
                }
            },
            failure: function () {
                alert('Error Occurred Try Again !!');
            }
        });
    }
});

async function checkEmail(email) {
    var check = "No";
    await $.get("https://isitarealemail.com/api/email/validate?email=" +
        email,
        function responseHandler(data) {
            if (data.status === 'valid') {
                check = "Yes";
            } else {
            }
        });
    return check;
}