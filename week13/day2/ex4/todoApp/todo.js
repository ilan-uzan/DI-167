export class TodoList {
  constructor() {
    this.tasks = [];
  }

  add(task) {
    this.tasks.push({ text: task, complete: false });
  }

  complete(index) {
    if (index >= 0 && index < this.tasks.length) {
      this.tasks[index].complete = true;
    }
  }

  list() {
    return this.tasks.map((t, i) => ({
      index: i,
      text: t.text,
      complete: t.complete
    }));
  }
}
