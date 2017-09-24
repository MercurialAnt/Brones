angular.module('RoommateApp', [])
  .controller('RoommateListController', function($scope, $http) {
    url = 'http://localhost:8080/'
    var ctrl = this;
    $http.get(url).then(function(response) {
      ctrl.floorList = response.data;
      
      ctrl.floor4S = ctrl.floorList[0];
      ctrl.floor3S = ctrl.floorList[1];
      ctrl.floor2S = ctrl.floorList[2];
      ctrl.floor2N = ctrl.floorList[3];
      ctrl.floor3N = ctrl.floorList[5];
      ctrl.floor4N = ctrl.floorList[4];
    });
    // todoList.todos = [
    //   {text:'learn AngularJS', done:true},
    //   {text:'build an AngularJS app', done:false}];
 
    // todoList.addTodo = function() {
    //   todoList.todos.push({text:todoList.todoText, done:false});
    //   todoList.todoText = '';
    // };
 
    // todoList.remaining = function() {
    //   var count = 0;
    //   angular.forEach(todoList.todos, function(todo) {
    //     count += todo.done ? 0 : 1;
    //   });
    //   return count;
    // };
 
    // todoList.archive = function() {
    //   var oldTodos = todoList.todos;
    //   todoList.todos = [];
    //   angular.forEach(oldTodos, function(todo) {
    //     if (!todo.done) todoList.todos.push(todo);
    //   });
    // };
  });