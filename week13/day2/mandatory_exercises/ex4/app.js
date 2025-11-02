import { TodoList } from "./todo.js";

function demo() {
	const todo = new TodoList();
	todo.add("Learn Node modules");
	todo.add("Write tests");
	todo.complete(0);
	return todo.list();
}

if (require.main === undefined) {
	console.log(demo());
}

export { demo };
