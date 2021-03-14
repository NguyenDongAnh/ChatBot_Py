(function () {
    var Message;
    var Tag = "";
    var N = 0;
    var count = 0;
    var graph = [];
    Message = function (arg) {
        this.text = arg.text, this.message_side = arg.message_side;
        this.draw = function (_this) {
            return function () {
                var $message;
                $message = $($('.message_template').clone().html());
                $message.addClass(_this.message_side).find('.text').html(_this.text);
                $('.messages').append($message);
                return setTimeout(function () {
                    return $message.addClass('appeared');
                }, 0);
            };
        }(this);
        return this;
    };
    $(function () {
        var getMessageText, message_side, sendMessage;
        message_side = 'right';
        getMessageText = function () {
            var $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };
        sendMessage = function (text, message_side = "right") {
            var $messages, message;
            if (text.trim() === '') {
                return;
            }
            $('.message_input').val('');
            $messages = $('.messages');
            // message_side = message_side === 'left' ? 'right' : 'left';
            message = new Message({
                text: text,
                message_side: message_side
            });
            message.draw();
            return $messages.animate({
                scrollTop: $messages.prop('scrollHeight')
            }, 300);
        };
        $('.send_message').click(function (e) {
            if (getMessageText() !== '') {
                if (Tag === "max_flow") {
                    socket.emit('input_N', {
                        data: `${getMessageText()}`
                    });
                } else if (Tag === "input_N") {
                    socket.emit('input_row', {
                        data: `${getMessageText()}`
                    });
                } else if (Tag === "input_row") {
                    socket.emit('input_row', {
                        data: `${getMessageText()}`,
                        graph: graph,
                        count: count,
                        N: N
                    });
                } else {
                    socket.emit('input', {
                        data: `${getMessageText()}`
                    });
                }
            }
            return sendMessage(getMessageText());
        });
        $('.message_input').keyup(function (e) {
            if (e.which === 13 && getMessageText() !== '') {
                if (Tag === "max_flow") {
                    socket.emit('input_N', {
                        data: `${getMessageText()}`
                    });
                } else if (Tag === "input_N") {
                    socket.emit('input_row', {
                        data: `${getMessageText()}`
                    });
                } else if (Tag === "input_row") {
                    socket.emit('input_row', {
                        data: `${getMessageText()}`,
                        graph: graph,
                        count: count,
                        N: N
                    });
                } else {
                    socket.emit('input', {
                        data: `${getMessageText()}`
                    });
                }
                return sendMessage(getMessageText());
            }
        });
        /* -------------------------------------- */
        var socket = io();
        socket.on('connect', function () {
            socket.emit('my event', {
                data: `${socket.id}`
            });
        });
        socket.on('new message', function (data) {
            Tag = data.tag
            return sendMessage(data.message, "left")
        });
        socket.on('input_N', function (data) {
            Tag = data.tag
            if (data.N) N = data.N
            return sendMessage(data.message, "left")
        });
        socket.on('input_row', function (data) {
            Tag = data.tag
            if (data.row) {
                graph = $.merge(graph, data.row)
            }
            if (data.count) {
                count = count + 1;
                if (count == N) {
                    socket.emit('input_row', {
                        data: "",
                        graph: graph,
                        count: count,
                        N: N
                    });
                    count = 0;
                    N = 0;
                    graph = [];
                }
            }
            return sendMessage(data.message, "left")
        });
    });
}.call(this));