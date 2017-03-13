(function(){
    'use strict';

    angular.module('scrumboard.demo').config(['$routeProvider', config]).run(['$http', run]);      //any function in angular run will run when the application starts after loading all modules
    
    function  config($routeProvider) {
        $routeProvider.when('/', {templateUrl: '/static/html/scrumboard.html', controller: 'ScrumboardController',})
                      .when('/login', {templateUrl:'/static/html/login.html', controller: 'LoginController'})
                      .otherwise('/');
    }
    
    function run($http){
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName =  'csrftoken';
    }
})();