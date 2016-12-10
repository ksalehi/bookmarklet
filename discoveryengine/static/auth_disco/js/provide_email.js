function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            var csrftoken = Cookies.get('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function submitEmail() {
    var email = $('#email').val();
    $.post('/api/auth/emails/', {'email': email}, function(data, status, xhr) {
        if (status=="success") {
            window.location.href = "/";
        } else {
            // TODO: HANDLE ERROR
        }
    });
}