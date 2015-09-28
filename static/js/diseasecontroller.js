var diseaseApp = angular.module('diseaseApp', []);

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
});
