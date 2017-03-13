(function(){
    'use strict';

    angular.module('scrumboard.demo').directive('scrumboardCard', CardDirective);   //we are not creating a module,we are retriving it

    function CardDirective(){
        return {
            templateUrl: '/static/scrumboard/card.html',
            restrict: 'E',
            controller: ['$scope', '$http', function($scope, $http) {
                var url ='/scrumboard/cards/' + $scope.card.id + '/';
                $scope.update = function(){
                    $http.put(
                        url,
                        $scope.card
                    );
                };

                $scope.delete = function(){
                    $http.delete(url).then(function(){
                        var cards = $scope.list.cards;
                        cards.splice(cards.indexOf($scope.card),       //splice because js doesn't provide a mechanism to remove an element form an array
                         1
                        );
                    }, function(){
                        alert('Could not delete Card');
                    });
                };
            }]
        };
    }
})();