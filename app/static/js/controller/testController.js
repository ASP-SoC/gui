app.controller('testController', function ($scope, DataService) {
	$scope.text = 'Hi';
	$scope.devices = [
		{
			name: 'One',
			states: ('Exchange Merge').split(' ').map(function (state) { return { abbrev: state }; }),
			model: {
				usage: 'Exchange'
			}
		},
		{
			name: 'Two',
			states: ('Exchange Merge').split(' ').map(function (state) { return { abbrev: state }; }),
			model: {
				usage: 'Exchange'
			}
		}];
});
