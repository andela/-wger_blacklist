var app = angular.module('wger', []);


app.controller('UserList', function() {
  this.status = 'all';
  this.seleted = document.getElementById("mySelect").value;
})

function Appconfig ($interpolateProvider) {
  $interpolateProvider.startSymbol('${');
  $interpolateProvider.endSymbol('}');
}

app.config(['$interpolateProvider', Appconfig])


angular.element(function() {
     angular.bootstrap(document, ['wger']);
});
