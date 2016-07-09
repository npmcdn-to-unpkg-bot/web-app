$(document).ready(function() {
	$("#write-a-review").click(function() {
		$("#write-a-review").hide();
		$("#post-review").show();
	})
})

// $('form#post-review').submit(function(evt) {
// 	alert("Heyyyy");
// });

function hookup() {
	company=$("#company-input").val();
	rating=$("#rating-input").val();
	review=$("#review-input").val();
	reason=$("#reason-input").val();

	dataToSend = {
		'company': company,
		'rating': rating,
		'review': review,
		'reason': reason
	}
	console.log(dataToSend)

	$.post( "post_review/", dataToSend)
		.done(function(returnedData) {
			// alert("Returned:" + returnedData);
			location.reload()
	});
}


