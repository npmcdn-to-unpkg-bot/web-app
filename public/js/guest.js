$(document).ready(function() {

})



function create_user() {
	new_user = {
	first_name : $("#first-name").val(),
	last_name : $("#last-name").val(),
	email : $("#email").val(),
	password : $("#password").val(),
	password_confirm : $("#password-confirm").val()
	}

	$.post('/api/create_user/', new_user)
	    .done(function(response) {
	      console.log("success")
	      window.location.href = "/"
	});
}


function login_user() {
	user = {
		email : $("#email").val(),
		password : $("#password").val(),
	}


	$.post('/api/login_user/', user)
	    .done(function(response) {
	      console.log("calling login_user")
	      // window.location.href = "/"
	});
}


