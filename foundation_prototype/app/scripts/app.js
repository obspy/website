var app = angular.module('ObsPyApp', []);

app.controller('TopBarController',
    function ($scope) {
        'use strict';
        $scope.menuItems = [
            'View on Github',
            'File a Bug',
            'Contribute',
            'Join the Mailinglist',
            'Gallery',
          ];
        $scope.menuItems.reverse();
      });
