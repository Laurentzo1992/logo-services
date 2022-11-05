var bg = $("#particles-js");
$(document).keydown(function() {
    $(bg).css("background-color", getRandomColor);
});

$(".img").on("click", function() {

    //Action une

    var name = $(this).attr("name");
    const initial = name.charAt(0).toUpperCase();
    const nameCapitalized = initial + name.slice(1);

    $("#titre").text(nameCapitalized);

    //Action deux

    $(this).toggleClass("flash");

    //Action trois

    var music = $(this).attr("name");
    music += ".mp3";
    playMusic(music);


});

$("#btn").click(function() {
    var artiste = $("#input").val();
    var music = artiste + ".mp3";
    playMusic(music);
});

function playMusic(music) {
    var audio = new Audio(music);
    audio.play();

}


function getRandomColor() {
    var letters = "0123456789ABCDEF";
    var color = "#";
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * letters.length)];
    }
    return color;
}