
$(document).ready(function () {
    // Text animation
    $(".tlt").textillate({
        loop: true,
        in: { effect: "bounceIn" },
        out: { effect: "bounceOut" }
    });

    // Siri wave
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 200,
        style: "ios9"
    });

    // Mic click
    $("#MicBtn").click(function () {
        eel.playAssistantSound();
        $("#oval").attr("hidden", true);
        $("#siriwave").removeAttr("hidden");
        eel.start_listening();  //  continuous listening start hoga
    });


    $("#StopBtn").click(async function () {
        await eel.stop_listening()();  //  stop continuous listening
        $("#MicBtn").removeClass("active");
        $("#StopBtn").attr("hidden", true);
        $("#chatbox").val("");
        $("#oval").removeAttr("hidden");
        $("#siriwave").attr("hidden", true);
        $(".siri-message").text("Assistant stopped.").textillate("start");
    });


    function doc_keyUp(e) {
        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound();
            $("#oval").attr("hidden", true);
            $("#siriwave").removeAttr("hidden");
            eel.allCommands(); // ✅ fixed double ()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // Update message from Python
    eel.expose(DisplayMessage);
    function DisplayMessage(msg) {
        $(".siri-message").text(msg);
        $(".siri-message").textillate("start");
    }

    // Show UI after response
    eel.expose(ShowHood);
    function ShowHood() {
        $("#oval").removeAttr("hidden");
        $("#siriwave").attr("hidden", true); // Fixed syntax error: removed extra quotation
    }

    // --- Text Command ---
    function PlayAssistant(message) {
        if (message !== "") {
            $("#oval").attr("hidden", true);
            $("#siriwave").removeAttr("hidden");
            DisplayMessage(message); // Display typed input
            eel.allCommands(message); // ✅ sends text command to Python
            $("#chatbox").val("");
            $("#MicBtn").removeAttr("hidden");
            $("#SendBtn").attr("hidden", true);
        }
    }

    // --- Show/Hide Buttons Based on Input ---
    function ShowHideButton(message) {
        if (message.length === 0) {
            $("#MicBtn").removeAttr("hidden");
            $("#SendBtn").attr("hidden", true);
        } else {
            $("#MicBtn").attr("hidden", true);
            $("#SendBtn").removeAttr("hidden");
        }
    }

    // Keyup on chatbox
    $("#chatbox").keyup(function (e) {
        let message = $("#chatbox").val();
        ShowHideButton(message);

        //  Press Enter to send
        if (e.key === "Enter" || e.keyCode === 13) {
            PlayAssistant(message);
        }
    });

    //  Click send button
    $("#SendBtn").click(function () {
        let message = $("#chatbox").val();
        PlayAssistant(message);
    });

    // Notify Python when the tab is closed
    window.onbeforeunload = function () {
        eel.on_close()();
    };

});