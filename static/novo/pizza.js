$('.ui.selection.dropdown').dropdown();
$('.foto.image')
  .transition('fade up')
;

function capitaliseFirstLetter(string)
{
    return string.charAt(0).toUpperCase() + string.slice(1);
}

var pizza_app = angular.module('pizza_app', []);
pizza_app.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.headers.common['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept";
        $httpProvider.defaults.useXDomain = true;
        delete $httpProvider.defaults.headers.common['X-Requested-With'];
        $httpProvider.defaults.timeout = 5000;
    }
]);

pizza_app.controller('PizzaController2', function($scope, $http) {
    //var base_url_api = 'http://fratelli.herokuapp.com';
    var base_url_api = 'http://127.0.0.1:8000';
    $http.get(base_url_api +'/pizzas/?format=json')
       .then(function(res){
          $scope.pizzas_data = res.data;
            res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        });

});

pizza_app.filter('primeiraMaiuscula', function() {
        return function(string_qualquer) {
            return string_qualquer.charAt(0).toUpperCase() + string_qualquer.slice(1);
        };
});

pizza_app.filter('monetario', function() {
        return function(string_qualquer) {
            return "R$ " + string_qualquer.replace('.', ',');
        };
});

pizza_app.directive('pizzaImg', function() {
    return {
        restrict: 'E',
        scope: {
            'src': '='
        },
        template: '<img class="foto image" src="{{ src }}" width="130">'
    };
});