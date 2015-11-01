
$(document).ready(function() {

    $("body").addClass("loaded");

    $(function () {
        $('a[rel="lightbox"]').fluidbox();
    })
    $("#feedButton").hover(
        function(){
            $(this).css({"background-color":"#f05451"});
        },
        function(){
            $(this).css({"background-color":"white"});
        }
    );
    $("#distressButton").hover(
        function(){
            $(this).css({"background-color":"#f05451"});
        },
        function(){
            $(this).css({"background-color":"white"});
        }
    );

    $("#ques").hover(
        function(){
            $(this).css({"background-color":"#f05451"});
        },
        function(){
            $(this).css({"background-color":"white"});
        }
    );

    $("#recordButton").hover(
        function(){
            $(this).css({"background-color":"#f05451"});
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
$("#ques").click(function(){
        
        var ques = $('#questxt').val();
        console.log(ques);
        var BaseUrl="http://virtualdoctor.mybluemix.net/query/";
        $.post( "http://virtualdoctor.mybluemix.net/query/", { 'question': ques })
  .done(function( data ) {
    alert( "Data Loaded: " + data );
    var ans=$('#postanswer');
    var ansdiv = $('<div>'+data+'</div>');
    ans.append(ansdiv);
  });
});


});
