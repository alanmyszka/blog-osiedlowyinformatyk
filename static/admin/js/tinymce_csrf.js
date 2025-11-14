(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    document.addEventListener('DOMContentLoaded', function () {
        if (typeof tinymce !== 'undefined') {
            tinymce.on('AddEditor', function (e) {
                e.editor.on('init', function () {
                    var csrftoken = getCookie('csrftoken') ||
                        document.querySelector('[name=csrfmiddlewaretoken]')?.value;

                    var originalXHR = window.XMLHttpRequest;
                    window.XMLHttpRequest = function () {
                        var xhr = new originalXHR();
                        var originalOpen = xhr.open;
                        xhr.open = function (method, url) {
                            originalOpen.apply(xhr, arguments);
                            if (url.indexOf('/upload-image/') !== -1) {
                                xhr.setRequestHeader('X-CSRFToken', csrftoken);
                            }
                        };
                        return xhr;
                    };
                });
            });
        }
    });
})();