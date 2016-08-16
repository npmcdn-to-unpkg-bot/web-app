$(document).ready(function() {
	$("#write-a-review").click(function() {
		$("#write-a-review").hide();
		$("#post-review").show();
	})

	$(".js-example-placeholder-multiple").select2({
	  placeholder: "Select a company"
	});


	// flash message disappear
	setTimeout((function() {
	  return $('.flash-messages').fadeOut('slow');
	}), 3000);



})

// $('form#post-review').submit(function(evt) {
// 	alert("Heyyyy");
// });

function hookup() {
	// company=$("#company-input").val();
	company=$("#company-autoform").val();
	// rating=$("#rating-input").val();
	rating = $( "#slider" ).slider( "option", "value" );
	review=$("#review-input").val();
	reason=$("#reason-input").val();
	tag=$("#tag-input").val();

	console.log(company);

	dataToSend = {
		'company': company,
		'rating': rating,
		'review': review,
		'reason': reason,
		'tag': tag
	}
	console.log(dataToSend)

	$.post( "api/post_review/", dataToSend)
		.done(function(returnedData) {
			// alert("Returned:" + returnedData);
			location.reload()
	});
}


// function showVolume(shoutVolume) {
//   if (shoutVolume < 0) {
//     $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:red;font-size:28px;"></span>'.repeat(Math.abs(shoutVolume)))
//   }
//   if (shoutVolume == 0) {
//     $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:cyan;font-size:28px;"></span>')
//   }
//   if (shoutVolume > 0) {
//     $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:#05cc47;font-size:28px;"></span>'.repeat(shoutVolume))
//   }
// }


function showVolume(shoutVolume) {
  // if (shoutVolume < 0) {
  //   $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:28px;"></span>'.repeat(Math.abs(shoutVolume)));
  // }

  if (shoutVolume == 0) {
    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:cyan;font-size:28px;"></span>');
	$('#rating-description').text("don't care one way or the other")
  }

  if (shoutVolume > 0) {
    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:28px;"></span>'.repeat(shoutVolume));

    if (shoutVolume == 1) {
	    $("#post-review").css("background-color", "#d1ffd3");
	    $(".jumbotron").css("background-color", "#d1ffd3");
	    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:30px;"></span>'.repeat(Math.abs(shoutVolume)));
		$('#rating-description').text("it's ok")
    } 

    if (shoutVolume == 2) {
	    $("#post-review").css("background-color", "#abf0ae");
	    $(".jumbotron").css("background-color", "#abf0ae");
	    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:36px;"></span>'.repeat(Math.abs(shoutVolume)));
		$('#rating-description').text("they're kind of cool")
    } 

    if (shoutVolume == 3) {
	    $("#post-review").css("background-color", "#8cdc90");
	    $(".jumbotron").css("background-color", "#8cdc90");
	    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:42px;"></span>'.repeat(Math.abs(shoutVolume)));
		$('#rating-description').text("i really like them!")
    } 

    if (shoutVolume == 4) {
	    $("#post-review").css("background-color", "#73cd77");
	    $(".jumbotron").css("background-color", "#73cd77");
	    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:48px;"></span>'.repeat(Math.abs(shoutVolume)));
		$('#rating-description').text("i would absolutely recommend using this company")
    } 

    if (shoutVolume == 5) {
	    $("#post-review").css("background-color", "#5fc264");
	    $(".jumbotron").css("background-color", "#5fc264");
	    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:58px;"></span>'.repeat(Math.abs(shoutVolume)));
		$('#rating-description').text("i fucking love this company")
    }
  }

  if (shoutVolume < 0) {
    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:28px;"></span>'.repeat(Math.abs(shoutVolume)));

    if (shoutVolume == -1) {
	    $("#post-review").css("background-color", "#ffd3c6");
	    $(".jumbotron").css("background-color", "#ffd3c6");
	    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:30px;"></span>'.repeat(Math.abs(shoutVolume)));
		$('#rating-description').text("it's not ok")
    } 

    if (shoutVolume == -2) {
	    $("#post-review").css("background-color", "#ffbaa6");
	    $(".jumbotron").css("background-color", "#ffbaa6");
	    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:36px;"></span>'.repeat(Math.abs(shoutVolume)));
		$('#rating-description').text("i don't like using them")
    } 

    if (shoutVolume == -3) {
	    $("#post-review").css("background-color", "#ff825d");
	    $(".jumbotron").css("background-color", "#ff825d");
	    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:42px;"></span>'.repeat(Math.abs(shoutVolume)));
		$('#rating-description').text("i haven't had very good experiences...")
    } 

    if (shoutVolume == -4) {
	    $("#post-review").css("background-color", "#ff754d");
	    $(".jumbotron").css("background-color", "#ff754d");
	    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:48px;"></span>'.repeat(Math.abs(shoutVolume)));
		$('#rating-description').text("i definitely would NOT recommend")
    } 

    if (shoutVolume == -5) {
	    $("#post-review").css("background-color", "#ff3a00");
	    $(".jumbotron").css("background-color", "#ff3a00");
	    $("#slider-img").html('<span class="glyphicon glyphicon-volume-up" aria-hidden="true" style="color:white;font-size:58px;"></span>'.repeat(Math.abs(shoutVolume)));
		$('#rating-description').text("i fucking hate this company.")
    }
  }

}

// good colors:
// #d1ffd3
// #abf0ae
// #8cdc90
// #73cd77
// #5fc264


// bad colors:
// #ffd3c6
// #ffbaa6
// #1008764
// #ff754d
// #ff3a00
