import { TodoList } from "./todo.js";

const todo = new TodoList();
todo.add("Buy groceries");
todo.add("Pay bills");
todo.add("Write code");
todo.complete(1);

console.log(todo.list());
