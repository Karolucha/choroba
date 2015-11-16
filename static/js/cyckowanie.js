$(document).ready(function() {

    $('#reksio_pomocnik').autocomplete({
   	 	source: "/api/get_cycki",
         minChars: 2,
    }
    );
});