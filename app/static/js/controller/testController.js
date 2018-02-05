app.controller('testController', function ($scope, DataService) {
	$scope.text = 'Hi';

	$scope.cmd_states = {
		mode: [{ val: 1, name: 'Exchange' }, { val: 2, name: 'Merge' }],
		exchange: [{ val: 1, name: 'Straight' }, { val: 2, name: 'Cross' }],
		merge: [{ val: 1, name: 'Left' }, { val: 2, name: 'Right' }]
	}

	$scope.devices = [
		{
			id: 0,
			name: 'One',
			model: {
				usage: 1,
				exchange: 1,
				merge: 1
			}
		},
		{
			id: 1,
			name: 'Two',
			model: {
				usage: 1,
				exchange: 1,
				merge: 1
			}
		}
	];

	$scope.imds = [
		{
			name: 'InputMuxDevice1',
			model: {
				usage: 1,
				exchange: 1,
				merge: 1
			}
		},
		{
			name: 'InputMuxDevice1',
			model: {
				usage: 1,
				exchange: 1,
				merge: 1
			}
		}
	];

	$scope.cmd_update = function(id) {
		console.log(id);
		console.log($scope.devices[id])
	}
});
