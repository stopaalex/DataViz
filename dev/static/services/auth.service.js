var authService = angular.module('authService', [])
    .service('authService', function ($rootScope) {

        var authService = this;

        authService.auth_user = function() {
            var authAjax = $.ajax({
                method: 'POST',
                url: '/test',
                contentType: 'application/json; charset=utf-8',
                success: data => {
                    return data;
                },
                error: err => { }
            });

            return authAjax;
        }

    });