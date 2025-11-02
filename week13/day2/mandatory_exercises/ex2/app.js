import { people } from "./data.js";

function averageAge(arr) {
  if (!Array.isArray(arr) || arr.length === 0) return 0;
  const total = arr.reduce((s, p) => s + (p && p.age ? p.age : 0), 0);
  return total / arr.length;
}

if (require.main === undefined) {
  // running as ES module -> print
  console.log("Average age:", averageAge(people));
}

export { averageAge };
