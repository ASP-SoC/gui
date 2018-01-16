var services = angular.module('Services', []);

services.service('DataService', function ($q, $timeout, $http) {

	this.addTest = function (tmp_data) {
		var deferred = $q.defer();

		$http.post('/api/v0.1/test/add', { test: tmp_data })
			.success(function (data, status, headers, config) {
				if (status === 200 && data.success) {
					deferred.resolve();
				}
				else {
					user = false;
					deferred.reject(data.msg);
				}
			})
			.error(function (data, status, headers, config) {
				user = false;
				deferred.reject(data);
			});

		return deferred.promise;
	}

	this.getTest = function () {
		var deferred = $q.defer();

		$http.post('/api/v0.1/test/get')
			.success(function (data, status, headers, config) {
				if (status === 200 && data.success) {
					deferred.resolve(data.data);
				} else if (!data.success) {
					deferred.reject(data.msg)
				}
			})
			.error(function (data, status, headers, config) {
				deferred.reject(data);
			});

		return deferred.promise;
	}
});
