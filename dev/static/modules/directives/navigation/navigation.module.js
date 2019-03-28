var navigation = angular.module('navigation', [])
.directive('navigation', function () {
    return {
        link: function (scope, element, attrs) {
            scope.navigationHTML = function () {
                var path = {};
                path.url = "static/modules/directives/navigation/navigation.template.html";
                
                return path.url;
            }
        },
        restrict: 'A',
        template: '<div ng-include="navigationHTML()"></div>'
    };
});