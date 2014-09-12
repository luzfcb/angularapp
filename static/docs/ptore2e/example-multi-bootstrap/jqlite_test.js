describe("module:ng.function:angular.bootstrap", function() {
  var rootEl;
  beforeEach(function() {
    rootEl = browser.rootEl;
    browser.get("./examples/example-multi-bootstrap/index.html");
  });
  
it('should only insert one table cell for each item in $scope.fillings', function() {
 expect(element.all(by.css('td')).count())
     .toBe(9);
});
});
