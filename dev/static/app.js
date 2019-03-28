"use strict";

var myApp = angular.module('myApp', [
    'ngRoute',
    'login',
    'navigation',
    'authService',
    'loadingService'
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


myApp.controller('myAppCtrl', function ($scope, $rootScope, $location, loadingService, authService) {

    function init() {
        // loadingService.create_loader('loading...')
        authService.auth_user()
            .then(data => {
                console.log(data);
            })
    }

    init();
});