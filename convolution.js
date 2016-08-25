
var countryApp = angular.module('countryApp', []);
countryApp.controller('CountryCtrl', function ($scope){
  $scope.countries = [
    {"name": "China", "population": 1359821000},
    {"name": "India", "population": 1205625000},
    {"name": "United States of America","population": 312247000}
  ];
});

