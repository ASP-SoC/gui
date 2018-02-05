app.controller('testController', function ($scope, DataService) {
	$scope.text = 'Hi';

	$scope.cmd_states = {
		mode: [{ val: 1, name: 'Exchange' }, { val: 2, name: 'Merge' }],
		exchange: [{ val: 1, name: 'Straight' }, { val: 2, name: 'Cross' }],
		merge: [{ val: 1, name: 'Left' }, { val: 2, name: 'Right' }]
	}

	/* ----------------------------------------------------
	 *	GET FUNCTIONS
	 * ----------------------------------------------------
	 */


	$scope.cmd_get = function () {
		DataService.get_cmd()
			.then(function (data) {
				$scope.cmd_devices = data;
			})
			.catch(function (data) {

			});
	}

	$scope.cmd_get();

	/* ----------------------------------------------------
	 *	UPDATE FUNCTIONS
	 * ----------------------------------------------------
	 */

	$scope.cmd_update = function(id) {
		console.log(id);
		console.log($scope.devices[id])
		DataService.update_cmd({ id: id, model: $scope.devices[id].model})
		.then(function (data) {

		})
		.catch(function (data) {

		});
	}
});
