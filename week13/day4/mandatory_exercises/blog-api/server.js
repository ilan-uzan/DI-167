const express = require('express');
const { check, validationResult } = require('express-validator');
const app = express();
app.use(express.json());

let posts = [
  { id: 1, title: 'First Post', content: 'Hello world' },
  { id: 2, title: 'Second Post', content: 'Another post' }
];

// GET /posts
app.get('/posts', (req, res) => res.json(posts));

// GET /posts/:id
app.get('/posts/:id', (req, res) => {
  const id = Number(req.params.id);
  const post = posts.find(p => p.id === id);
  if (!post) return res.status(404).json({ error: 'Post not found' });
  res.json(post);
});

// POST /posts
app.post(
  '/posts',
  [check('title').notEmpty(), check('content').notEmpty()],
  (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) return res.status(400).json({ errors: errors.array() });
    const { title, content } = req.body;
    const newPost = { id: posts.length ? posts[posts.length - 1].id + 1 : 1, title, content };
    posts.push(newPost);
    res.status(201).json(newPost);
  }
);

// PUT /posts/:id
app.put(
  '/posts/:id',
  [check('title').optional().notEmpty(), check('content').optional().notEmpty()],
  (req, res) => {
    const id = Number(req.params.id);
    const post = posts.find(p => p.id === id);
    if (!post) return res.status(404).json({ error: 'Post not found' });
    const errors = validationResult(req);
    if (!errors.isEmpty()) return res.status(400).json({ errors: errors.array() });
    const { title, content } = req.body;
    post.title = title ?? post.title;
    post.content = content ?? post.content;
    res.json(post);
  }
);

// DELETE /posts/:id
app.delete('/posts/:id', (req, res) => {
  const id = Number(req.params.id);
  const idx = posts.findIndex(p => p.id === id);
  if (idx === -1) return res.status(404).json({ error: 'Post not found' });
  const deleted = posts.splice(idx, 1)[0];
  res.json(deleted);
});

// 404 handler
app.use((req, res) => res.status(404).json({ error: 'Not Found' }));

// Error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Server Error' });
});

const PORT = process.env.PORT || 3000;
if (require.main === module) {
  app.listen(PORT, () => console.log(`Blog API listening on port ${PORT}`));
}

module.exports = app;
