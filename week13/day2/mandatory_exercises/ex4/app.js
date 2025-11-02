import { TodoList } from "./todo.js";

const todo = new TodoList();
todo.add("Learn Node modules");
todo.add("Write tests");

todo.complete(0);

console.log(todo.list());
