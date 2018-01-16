var app = angular.module('AspApp', ['ui.router', 'Services']);

app.config(function ($stateProvider, $urlRouterProvider) {
	$stateProvider
		.state('/', {
			url: '/',
			templateUrl: '/html/home.htm'
		})
		/*.state('/tmp', {
			url: '/tmp',
			templateUrl: '/html/tmp.htm',
			controller: 'tmpController'
		})*/
	$urlRouterProvider.otherwise('/');
});

app.controller('mainctrl', function ($scope, $rootScope, $state, $stateParams) {

	$scope.init = function () {

	};

});

app.run(function ($state, $rootScope) {
	$rootScope.$state = $state;
})
