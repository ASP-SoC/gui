var app = angular.module('AspApp', ['ngMaterial', 'ui.router', 'Services']);

app.config(function ($stateProvider, $urlRouterProvider, $locationProvider) {
	$stateProvider
		.state('/', {
			url: '/',
			templateUrl: '/html/home.htm'
		})
		.state('test', {
			url: '/test',
			templateUrl: '/html/test.htm',
			controller: 'testController'
		})
	$urlRouterProvider.otherwise('/');

	$locationProvider.html5Mode(true);
	$locationProvider.hashPrefix('');
});

app.controller('mainctrl', function ($scope, $mdSidenav) {

	$scope.init = function () {
		console.info("init");
	};

	$scope.navigation = [
		{ name: 'Home', link: '/'},
		{ name: 'Test', link: 'test' }];

	$scope.toggleSidenav = function (menuId) {
		$mdSidenav(menuId).toggle();
	};


});

app.run(function ($state, $rootScope) {
	console.log('statechange')
	$rootScope.$state = $state;
})
