const axios = require('axios');

async function fetchPosts() {
  const res = await axios.get('https://jsonplaceholder.typicode.com/posts');
  return res.data;
}

module.exports = { fetchPosts };
