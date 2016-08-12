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
	company=$("#company-input").val();
	rating=$("#rating-input").val();
	review=$("#review-input").val();
	reason=$("#reason-input").val();
	tag=$("#tag-input").val();

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


