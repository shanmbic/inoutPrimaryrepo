
$(document).ready(function() {

    $("body").addClass("loaded");

    $(function () {
        $('a[rel="lightbox"]').fluidbox();
    })
    $("#feedButton").hover(
        function(){
            $(this).css({"background-color":"red"});
        },
        function(){
            $(this).css({"background-color":"white"});
        }
    );
    $("#distressButton").hover(
        function(){
            $(this).css({"background-color":"red"});
        },
        function(){
            $(this).css({"background-color":"white"});
        }
    );

    $("#feedButton").click(function(){
        
        var stories = $('#stories');
        var title="Title";
        var body="Content";
        var head = $(title);
        var body = $(content);
        var feedDiv = $('<div class="col-full"> <h2>'+head+'</h2>  <p>'+body+'</p> </div>');
        stories.append(feedDiv);

    });

});
