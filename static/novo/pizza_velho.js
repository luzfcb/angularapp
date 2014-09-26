var app = angular.module("pizza", []);

app.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.useXDomain = true;
        delete $httpProvider.defaults.headers.common['X-Requested-With'];
        $httpProvider.defaults.timeout = 5000;
    }
]);
app.factory('pizza', ['$http', '$q', function(http, q) {
    //var api_root = 'http://fratelli.herokuapp.com';
    var api_root = 'http://127.0.0.1:8000';


    return {
        getRepos: function() {
            var repos_p = q.defer();
            var url = api_root + '/pizzas/?format=json';
            var repos = [];
            console.log("url: " + url);

            http.get(url).success(function(data) {
                 console.log(data);
                repos = repos.concat(data);
            });

            repos_p.resolve(repos);
            console.log("repos: " + repos);
            console.log("repos_p.promise: " + repos_p.promise);
            scope.repos2 = repos_p.promise;
            return repos_p.promise;
        }

    };
}]);

app.directive('ghImg', function() {
    return {
        restrict: 'E',
        scope: {
            'src': '='
        },
        template: '<img src="{{ src }}" width="100">'
    };
});

app.filter('ago', function() {
    return function(value) {
        return moment(value).fromNow(true);
    };
});

app.controller("PizzaController", ['$scope', 'pizza', function(scope, github) {
    var valor_pizza = function(repo) {
        console.log(repo);
        return repo.valor;
    };

    var repos = [];

    var got_repos = function(data) {
        repos = repos.concat(data);

        scope.repos = _.chain(repos)
            .sortBy(valor_pizza)
            .reverse()
            .value();
    };
    var got_repo = function(data) {
        got_repos([data]);
    };

    github.getRepos().then(got_repos);
////    if (config.additional) {
//        console.log('adicional');
////        var extra = config.additional.split(',');
////        _.each(extra, function(repo) {
//            github.getRepo(repo.trim()).success(got_repo);

}]);
/**
 * Created by sutransdev on 26/09/14.
 */
