var diseaseApp = angular.module('diseaseApp', []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
}).config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

diseaseApp.controller('DiseaseListCtrl', function ($scope) {
$scope.hello="OOOOOOOOURANGUTAN";
  $scope.phones = [
    {'name': 'Nexus S',
     'snippet': 'Fast just got faster with Nexus S.'},
    {'name': 'Motorola XOOM™ with Wi-Fi',
     'snippet': 'The Next, Next Generation tablet.'},
    {'name': 'MOTOROLA XOOM™',
     'snippet': 'The Next, Next Generation tablet.'}
  ];
  console.log($scope.phones);
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


});
