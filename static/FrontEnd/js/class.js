// JavaScript source code
$(document).ready(function () {
    var m = 60; // Phút
    var s = 0; // Giây
    var timeout = null; // Timeout
    var check = 0;
    $('#start-clock').click(function start() {
        if (s === -1) {
            m -= 1;
            s = 59;
        }
        if (m == 0 && s == 0) {
            clearTimeout(timeout);
            alert('Hết giờ');
            return false;
        }
        document.getElementById('m').innerText = m.toString();
        document.getElementById('s').innerText = s.toString();

        timeout = setTimeout(function () {
            s--;
            start();
        }, 1000);
    });
    $('#start-clock').click(function () {
        $('#start-clock').hide();
    });
    function stop() {
        clearTimeout(timeout);
    }
});
