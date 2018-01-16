var app = angular.module('AspApp', ['ui.router', 'Services']);

app.config(function ($stateProvider, $urlRouterProvider) {
	$stateProvider
		.state('/', {
			url: '/',
			templateUrl: '/html/home.htm'
		})
		.state('/test', {
			url: '/test',
			templateUrl: '/html/test.htm',
			controller: 'testController'
		})
	$urlRouterProvider.otherwise('/');
});

app.controller('mainctrl', function ($scope, $rootScope, $state, $stateParams) {

	$scope.init = function () {

	};

});

app.run(function ($state, $rootScope) {
	$rootScope.$state = $state;
})
