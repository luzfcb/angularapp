var app = angular.module("pizza", []);

app.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.useXDomain = true;
        delete $httpProvider.defaults.headers.common['X-Requested-With'];
        $httpProvider.defaults.timeout = 5000;
    }
]);
app.factory('pizza', ['$http', '$q', function(http, q) {
    var api_root = 'http://fratelli.herokuapp.com';
    var per_page = 100;

    return {
//        getUser: function(username) {
//            return http.get(api_root + '/users/' + username);
//        },
        getRepos: function(username) {
            var repos_p = q.defer();
            var url = api_root + '/pizzas/?format=json';
            var repos = [];
            console.log(url);

            http.get(url).success(function(data) {
                 console.log(data);
                repos = repos.concat(data);
            });

            repos_p.resolve(repos);
            console.log(repos);
            return repos_p.promise;
        }
        //,
//        getRepo: function(repo) {
//            return http.get(api_root + '/repos/' + repo);
//        }
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
    var config = document.body.dataset;

    var week_half_life  = 1.146 * Math.pow(10, -9);
    var push_weight = 1;
    var watcher_weight = 1.314 * Math.pow(10, 7);
    var now = new Date;

//    var hotness = function(repo) {
//        var push_delta = now - Date.parse(repo.pushed_at);
//        var create_delta = now - Date.parse(repo.created_at);
//
//        var hotness = push_weight * Math.pow(Math.E, -1 * week_half_life * push_delta) + watcher_weight * repo.stargazers_count / create_delta;
//        return hotness
//    };

    var valor_pizza = function(repo) {
        return repo.valor;
    };

//    github.getUser(config.username).success(function(data) {
//        scope.user = data;
//    });

    var repos = [];

    var got_repos = function(data) {
        repos = repos.concat(data);

//        scope.recent = _.chain(repos)
//            .sortBy(valor_pizza)
//            .slice(-3)
//            .reverse()
//            .value()

        scope.repos = _.chain(repos)
            .sortBy(valor_pizza)
            .reverse()
            .value();

//        scope.source_repos = _.filter(repos, function(repo) {
//            return !repo.fork;
//        }).length;
    };
    var got_repo = function(data) {
        got_repos([data]);
    };

    github.getRepos(config.username).then(got_repos);
//    if (config.additional) {
        console.log('adicional');
//        var extra = config.additional.split(',');
//        _.each(extra, function(repo) {
            github.getRepo(repo.trim()).success(got_repo);
//        });
//    }
}]);
