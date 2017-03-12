(function(){
    'use strict';

    angular.module('scrumboard.demo').directive('scrumboardCard', CardDirective);   //we are not creating a module,we are retriving it

    function CardDirective(){
        return {
            templateUrl: '/static/scrumboard/card.html',
            restrict: 'E'
        };
    }
})();