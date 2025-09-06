$(document).ready(function () {
    // Display Speak Message
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $(".siri-message").text(message); // ✅ fixed
        $(".siri-message").textillate("start");
    }

    // Display hood
    eel.expose(ShowHood);
    function ShowHood() {
        console.log(" ShowHood() triggered"); // Add this line
        $("#oval").attr("hidden", false);
        $("#siriwave").attr("hidden", true);
    }

});
