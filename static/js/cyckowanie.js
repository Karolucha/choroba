$(document).ready(function() {

    $('#reksio_pomocnik').autocomplete({
   	 	source: "/api/get_cycki",
         minLength: 2,
    }
    );
});