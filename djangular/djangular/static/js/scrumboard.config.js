(function(){
    'use strict';

    angular.module('scrumboard.demo').run(['$http', run]);      //any function in angular run will run when the application starts after loading all modules

    function run($http){
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.default.xsrfCookieName =  'csrftoken';
    }
})();