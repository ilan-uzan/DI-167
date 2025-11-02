import { people } from "./data.js";

function averageAge(arr) {
  if (!arr.length) return 0;
  const total = arr.reduce((s, p) => s + p.age, 0);
  return total / arr.length;
}

console.log("Average age:", averageAge(people));
