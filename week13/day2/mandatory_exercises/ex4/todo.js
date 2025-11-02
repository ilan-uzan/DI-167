export class TodoList {
  constructor() {
    this.todos = [];
  }

  add(task) {
    this.todos.push({ task, done: false });
  }

  complete(index) {
    if (this.todos[index]) this.todos[index].done = true;
  }

  list() {
    return this.todos;
  }
}
