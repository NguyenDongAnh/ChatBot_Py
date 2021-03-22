(function () {
  var Message;
  var Tag = "";
  var N = 0;
  var count = 0;
  var graph = [];
  Message = function (arg) {
    (this.text = arg.text), (this.message_side = arg.message_side);
    this.draw = (function (_this) {
      return function () {
        var $message;
        $message = $($(".message_template").clone().html());
        $message.addClass(_this.message_side).find(".text").html(_this.text);
        $(".messages").append($message);
        return setTimeout(function () {
          return $message.addClass("appeared");
        }, 0);
      };
    })(this);
    return this;
  };
  $(function () {
    var getMessageText, message_side, sendMessage;
    message_side = "right";
    getMessageText = function () {
      var $message_input;
      $message_input = $(".message_input");
      return $message_input.val();
    };
    sendMessage = function (text, message_side = "right") {
      var $messages, message;
      if (text.trim() === "") {
        return;
      }
      $(".message_input").val("");
      $messages = $(".messages");
      // message_side = message_side === 'left' ? 'right' : 'left';
      message = new Message({
        text: text,
        message_side: message_side,
      });
      message.draw();
      return $messages.animate(
        {
          scrollTop: $messages.prop("scrollHeight"),
        },
        300
      );
    };
    var fetchData = async function () {
      url = "/api/chat/" + getMessageText();
      await sendMessage(getMessageText());
      $.ajax({
        type: "POST",
        url: url,
        success: async function (result) {
          console.log(result);
          if (result.records.length != 0) {
            await sendMessage((result.name_company + " " + result.message), "left")
            var html = "";
            result.records.forEach((element) => {
              var d = new Date(element[0]);
              dateString =
                d.getDate() +
                "/" +
                (d.getMonth() + 1) +
                "/" +
                d.getFullYear();
              // console.log(Date(Date.parse(element[0])).getMonth());
              html += `<tr><td>${dateString}</td>
                              <td>${element[1]}</td>
                              <td>${element[2]}</td></tr>`;
            });
            return sendMessage(`
              <table>
                <thead>
                  <tr>
                    <th>NGAY</th>
                    <th>GIA DIEU CHINH</th>
                    <th>GIA DONG CUA</th>
                  </tr>
                </thead>
                <tbody>
                ${html}
                </tbody>
              </table>`,
              "left"
            );
          }
          return sendMessage("Không có dữ liệu", "left");
        },
      });
    }
    $(".send_message").click(async function (e) {
      if (getMessageText() !== "") {
        return fetchData()
      }
    });
    $(".message_input").keyup(async function (e) {
      if (e.which === 13 && getMessageText() !== "") {
        return fetchData()
      }
    });
    /* -------------------------------------- */
  });
}.call(this));
