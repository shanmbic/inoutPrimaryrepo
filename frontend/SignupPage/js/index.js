$(document).ready(function(){
	$('.form').find('input, textarea').on('keyup blur focus', function (e) {
  
	  var $this = $(this),
	      label = $this.prev('label');

		  if (e.type === 'keyup') {
				if ($this.val() === '') {
	          label.removeClass('active highlight');
	        } else {
	          label.addClass('active highlight');
	        }
	    } else if (e.type === 'blur') {
	    	if( $this.val() === '' ) {
	    		label.removeClass('active highlight'); 
				} else {
			    label.removeClass('highlight');   
				}   
	    } else if (e.type === 'focus') {
	      
	      if( $this.val() === '' ) {
	    		label.removeClass('highlight'); 
				} 
	      else if( $this.val() !== '' ) {
			    label.addClass('highlight');
				}
	    }

	});

	$('.tab a').on('click', function (e) {
  
	  e.preventDefault();
	  
	  $(this).parent().addClass('active');
	  $(this).parent().siblings().removeClass('active');
	  
	  target = $(this).attr('href');

	  $('.tab-content > div').not(target).hide();
	  
	  $(target).fadeIn(600);
  
	});


//________________testing
	window.onload = function() {
		var lat, lon;
		if (navigator.geolocation) {
			console.log('Success');
			navigator.geolocation.getCurrentPosition(function(position) {
				lat = position.coords.latitude;
				lon = position.coords.longitude;
				console.log(lat, lon);
				$("#inputlat").val(lat.toString());
				$("#inputlon").val(lon.toString());
				$("#signinputlat").val(lat.toString());
				$("#signinputlon").val(lon.toString());

			});
		} else {
	  // Print out a message to the user.
	  	console.log('Your browser does not support GeoLocation');
		}
		

		
	}


});

