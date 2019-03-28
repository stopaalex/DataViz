"use strict";

var myApp = angular.module('myApp', [
    'ngRoute',
    'login',
    'navigation'
]);

myApp.config(function ($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: '../static/modules/views/login/login.template.html'
        })
        .when('/login', {
            templateUrl: '../static/modules/views/login/login.template.html'
        })
        .otherwise('/');
});


myApp.controller('myAppCtrl', function ($scope, $rootScope, $location) {

    function init() {
    }

    init();
});