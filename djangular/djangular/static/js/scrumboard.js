(function(){
                'use strict';
                angular.module('scrumboard.demo', [])   //we are creating a module, that's y an extra parameter
                    .controller('ScrumboardController', [ '$scope', '$http',ScrumboardController]); //DEPENDENCIES - https and function

                function ScrumboardController($scope, $http){

                        $scope.add = function (list, title) {
                            var card = {
                                list: list.id,
                                title: title
                            };
                            $http.post('scrumboard/cards/', card).then(function(response){ //2nd arg is the card object created earlier
                                list.cards.push(response.data);
                            }, function(){
                                alert('Could not create Card');
                            });
                        };

                        $scope.login = function(){
                            $http.post('/auth_api/login/',
                                {username: 'reindert', password:'trednier'});
                        };

                        $scope.data = [];                                   //fill it with data from the database
                        $http.get('/scrumboard/lists').then(function(response){     //this is an asynchronous call, doesn't wait for data to return from the server
                            $scope.data = response.data;                    //it automatically takes a return in a promise form
                        });
                }

            }());