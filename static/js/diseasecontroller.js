var diseaseApp = angular.module('diseaseApp', []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
}).config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

diseaseApp.controller('DiseaseListCtrl', function ($scope) {

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
