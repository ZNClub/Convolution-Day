
var countryApp = angular.module('countryApp', []);
      countryApp.controller('CountryCtrl', function ($scope, $http){
        $http.get('https://raw.githubusercontent.com/ZNClub/Convolution-Day/master/circular.json').success(function(data) {
          $scope.con = data;
        });
      });
