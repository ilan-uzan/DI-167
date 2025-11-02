const express = require('express');
const { fetchPosts } = require('./data/dataService');
const app = express();

app.get('/posts', async (req, res) => {
  try {
    const posts = await fetchPosts();
    console.log('Fetched posts from JSONPlaceholder');
    res.json(posts);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to fetch posts' });
  }
});

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => console.log(`CRUD API listening on ${PORT}`));
