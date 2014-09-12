var app = angular.module('Funcionarios', ['ngRoute']);

app.config(
    function($routeProvider){
        $routeProvider.when('/',{
                templateUrl: 'partial/bem-vindo.tpl.html'
            }
        );

        $routeProvider.when('/funcionarios',{
                templateUrl: 'partial/funcionarios.tpl.html'
            }
        );

        $routeProvider.otherwise({
                redirectTo: '/'
            }
        );
    }
);