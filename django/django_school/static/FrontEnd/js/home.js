// JavaScript source code
$(document).ready(function () {
    //xử lí submit email
    $('#email-submit').find('img').click(function () {
        var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if (!filter.test($('#email-submit').find('input').val())) {
            alert('Hay nhap dia chi email hop le.\nExample@gmail.com');
            return false;
        }
        else {
            alert('OK roi day, Email nay hop le.');
        }
    });
    //xử lí get date tự động
    var date = new Date;
    var month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    var maxDate = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    var day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saruday"]
    var dayName = "";
    var stt = date.getDate();
    var j = 0;
    for (var i = 0; i < 7; i++) {
        dayName = "<option>" + day[(date.getDay() + i) % 7] + " " + month[date.getMonth() + j] + " " + stt++ + "th</option>";
        $('#date').append(dayName);
        $('#date-2').append(dayName);
        if (maxDate[date.getMonth()] < stt) { j++; stt = 1;}
    }

    //xử lí feedback
    $('#feedback').slideToggle(0);
    $('#feedback-button').click(function () {
        $('#feedback').slideToggle(500);
    });

    //xử lý reponsive menu
    $('#reponsive-menu-container').hide();
    $('#reponsive-header-bars').click(function () {
        $('#reponsive-menu-container').show();
    });
    $('#reponsive-menu-1-close').click(function () {
        $('#reponsive-menu-container').hide();
    });

    //back-next
    $('#reponsive-menu-main-birthday').hide();
    $('#next-birthday').click(function () {
        $('#reponsive-menu-main-home').hide();
        $('#reponsive-menu-main-birthday').show();
    });
    $('.back-home').click(function () {
        $('#reponsive-menu-main-birthday').hide();
        $('#reponsive-menu-main-home').show();
    });

    $('#reponsive-menu-main-sympathy').hide();
    $('#next-sympathy').click(function () {
        $('#reponsive-menu-main-home').hide();
        $('#reponsive-menu-main-sympathy').show();
    });
    $('.back-home').click(function () {
        $('#reponsive-menu-main-sympathy').hide();
        $('#reponsive-menu-main-home').show();
    });

    $('#reponsive-menu-main-occasions').hide();
    $('#next-occasions').click(function () {
        $('#reponsive-menu-main-home').hide();
        $('#reponsive-menu-main-occasions').show();
    });
    $('.back-home').click(function () {
        $('#reponsive-menu-main-occasions').hide();
        $('#reponsive-menu-main-home').show();
    });

    $('#reponsive-menu-main-flowers').hide();
    $('#next-flowers').click(function () {
        $('#reponsive-menu-main-home').hide();
        $('#reponsive-menu-main-flowers').show();
    });
    $('.back-home').click(function () {
        $('#reponsive-menu-main-flowers').hide();
        $('#reponsive-menu-main-home').show();
    });

    $('#reponsive-menu-main-plants').hide();
    $('#next-plants').click(function () {
        $('#reponsive-menu-main-home').hide();
        $('#reponsive-menu-main-plants').show();
    });
    $('.back-home').click(function () {
        $('#reponsive-menu-main-plants').hide();
        $('#reponsive-menu-main-home').show();
    });

    $('#reponsive-menu-main-gift').hide();
    $('#next-gift').click(function () {
        $('#reponsive-menu-main-home').hide();
        $('#reponsive-menu-main-gift').show();
    });
    $('.back-home').click(function () {
        $('#reponsive-menu-main-gift').hide();
        $('#reponsive-menu-main-home').show();
    });

    $('#reponsive-menu-main-same-day').hide();
    $('#next-same-day').click(function () {
        $('#reponsive-menu-main-home').hide();
        $('#reponsive-menu-main-same-day').show();
    });
    $('.back-home').click(function () {
        $('#reponsive-menu-main-same-day').hide();
        $('#reponsive-menu-main-home').show();
    });

    $('#reponsive-menu-main-sale').hide();
    $('#next-sale').click(function () {
        $('#reponsive-menu-main-home').hide();
        $('#reponsive-menu-main-sale').show();
    });
    $('.back-home').click(function () {
        $('#reponsive-menu-main-sale').hide();
        $('#reponsive-menu-main-home').show();
    });
    //feedback  
    var check = 0;
    $('#feedback-button').click(function () {
        if (check == 0) {
            $('#feedback-button').animate({ bottom:'326px'},500);
            check = 1;
        }
        else {
            $('#feedback-button').animate({ bottom: '30px' }, 500);
            check = 0;
        }
    });
});
