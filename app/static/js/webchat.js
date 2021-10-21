    $(document).ready(function() {
        var socket = io.connect();
        socket.on('connect', function() {
            socket.emit('connected');
            $('#myName').val('');
            $('#myMessage').val('');
        });

        socket.on('message', function(msg) {
            var name = msg.json_data.name;
            var message = msg.json_data.content;
            var date = msg.json_data.date;
            if (name == '') {
                name = 'Anonymous';
            }
            if (message == '') {
                message = 'I forgot to add a message.';
            }

            $("#messagesContainer").prepend("<div class=\"card mb-2\">\n" +
                "<div class=\"card-header\">\n" +
                "<h5 class=\"card-title\">"+name+"</h5><h6 class=\"card-subtitle mb-2 text-muted\">"+date+"</h6>\n" +
                "</div>\n" +
                "<div class=\"card-body\">\n" +
                ""+message+"\n" +
                "</div>\n" +
                "</div>");
            console.log('Received message');
        });

        $('#sendButton').on('click', function() {

            var name = $('#myName').val();
            var message = $('#myMessage').val();
            socket.send({name : name, message : message});
	    $('#myMessage').val('');
            //$("#toggleFieldset").children().attr("disabled", "disabled");
	    //$('#myMessage').attr('disabled', 'disabled');
            //$('#myName').attr('disabled', 'disabled');
        });

        socket.on('page_view_increase', function(count) {
        	console.log('ping');
			var total_count = count.page_views;
			console.log(total_count + ' views');
        	$("#pageViews").text(total_count);
		})
    });
