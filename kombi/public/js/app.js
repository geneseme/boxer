/* Javascript Usage: */

var ws = new WebSocket('ws://'+window.location.host+'/ws');
var app = (function($) {
    var config = $('#config');
    var app = JSON.parse(config.text());
    $(document).ready(function() {
        var router = new app.router();
        var navbar = new app.views.NavbarView();
        ws.onopen = function(event){ console.log('socket open'); };
        ws.onclose = function(event){ console.log('socket closed'); };
        ws.onerror = function(error){ console.log('error:', error); };
        ws.onmessage = function(event){ console.log('message:', event.data); };
    });
    return app;
})(jQuery);
