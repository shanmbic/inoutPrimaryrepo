
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

});
