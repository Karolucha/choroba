var diseaseApp = angular.module('diseaseApp', []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
}).config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

diseaseApp.controller('DiseaseListCtrl', function ($scope) {
console.log("działa");

 var values_duration = {};
values_duration['Dni'] = [];
for (i = 1; i < 31; i++) {
   values_duration['Dni'].push(i);
        }
values_duration['Tygodni'] = ['1', '2', '3', '4'];
values_duration['Miesięcy'] = [];
for (i = 1; i < 13; i++) {
   values_duration['Miesięcy'].push(i);
        }
values_duration['Miesięcy'].push('Powyżej roku');
console.log(values_duration);
$('#unit_duration').on('change', function() {
    console.log(values_duration);
    var carList = document.getElementById("unit_duration");
    var modelList = document.getElementById("value_duration");
    var selCar = carList.options[carList.selectedIndex].value;
    console.log(selCar);
    while (modelList.options.length) {
        modelList.remove(0);
    }
    var cars = values_duration[selCar];
    if (cars) {
        var i;
        for (i = 0; i < cars.length; i++) {
            var car = new Option(cars[i], i);
            modelList.options.add(car);
        }
    }
});
  $(function() {
    $( "#leave_comment" ).tabs();
  });
if($('#still_disease').prop('checked', true)) {

}
  $('#dsc_disease_short').hide();
      $scope.more_dsc = function(){
        console.log("na ja");
        $('#dsc_disease_short').hide();
        $('#dsc_disease').show();
    }

    $scope.less_dsc = function(){
        console.log("na ja");
        $('#dsc_disease_short').show();
        $('#dsc_disease').hide();
    }

    $scope.add_friend = function(friend_id){
        console.log("na ja");
         $.ajaxSetup({
  data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
});
        $.ajax({
            url: '127.0.0.1:8000/add_friend',
            type: 'post',
            data: {friend_id:friend_id,
            csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(data) {
                alert(data);
            },
            failure: function(data) {
                alert('Got an error dude');
            }
        });
    }
    $scope.save_new_comment = function (text, userId, diseaseId) {
         console.log("guten tag");
         var commentDict={};
         commentDict['text']=text;
         commentDict['user_id']=userId;
         commentDict['disease_id']=diseaseId;
         console.log(commentDict);
        $.ajax({
            url: '127.0.0.1:8000/added_comment',
            type: 'post', //this is the default though, you don't actually need to always mention it
            data: {comment_dict:commentDict},
            success: function(data) {
                alert(data);
            },
            failure: function(data) {
                alert('Got an error dude');
            }
        });
    }
    $scope.myActivity = function(){
        console.log("na ja");
        $('#jeden').val('lala');
    }
console.log("TU DZIALA CONTROLER");
//    $( ".selector" ).autocomplete({
//         source: [ "c++", "java", "php", "coldfusion", "javascript", "asp", "ruby" ]
//    });
//    $( ".search-people" ).keypress(function() {
//  console.log( "Handler for .keypress() called." );
//  if($(this).val().length>3){
//  console.log($(this).val().length);
//console.log($(this).val());
//  $.ajax({
//    type: "get",
//    url: '/',
//  //  data: $(this).val(),
//    context: this,
//    success: function(data) {
//            console.log(data);
////       $('#LoginModal').html(data);
//    }
//    });
//    return false;
//    }else{
//console.log($(this).val().length);
//}
//});

$(document).on('focus', '.search-people', function(){
 $(this).css("background-color", "#cccccc");
});
    $(document).on('blur', '.search-people', function(){
        $(this).css("background-color", "#ffffff");
    });
});
