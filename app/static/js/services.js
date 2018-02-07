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
			.then(function (response) {
				if (response.status === 200 && response.data.success) {
					deferred.resolve(response.data.data);
				}
				else {
					deferred.reject(response.data.msg);
				}
			}, function (response) {
				deferred.reject(response.data);
			});

		return deferred.promise;
	}

	this.update_cmd = function (data) {
		var deferred = $q.defer();

		$http.post('/api/v0.1/cmd/update', data)
		.then(function (response) {
			if (response.status === 200 && response.data.success) {
				deferred.resolve();
			}
			else {
				deferred.reject(response.data.msg);
			}
		}, function (response) {
			deferred.reject(response.data);
		});

		return deferred.promise;
	}

	this.get_cmd = function () {
		var deferred = $q.defer();

		$http.post('/api/v0.1/cmd/get')
		.then(function (response) {
			if (response.status === 200 && response.data.success) {
				deferred.resolve(response.data.data);
			}
			else {
				deferred.reject(response.data.msg);
			}
		}, function (response) {
			deferred.reject(response.data);
		});

		return deferred.promise;
	}

	this.update_imd = function (data) {
		var deferred = $q.defer();

		$http.post('/api/v0.1/imd/update', data)
			.then(function (response) {
				if (response.status === 200 && response.data.success) {
					deferred.resolve();
				}
				else {
					deferred.reject(response.data.msg);
				}
			}, function (response) {
				deferred.reject(response.data);
			});

		return deferred.promise;
	}

	this.get_imd = function () {
		var deferred = $q.defer();

		$http.post('/api/v0.1/imd/get')
			.then(function (response) {
				if (response.status === 200 && response.data.success) {
					deferred.resolve(response.data.data);
				}
				else {
					deferred.reject(response.data.msg);
				}
			}, function (response) {
				deferred.reject(response.data);
			});

		return deferred.promise;
	}
});
