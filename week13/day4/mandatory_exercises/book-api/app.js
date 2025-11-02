const express = require('express');
const { check, validationResult } = require('express-validator');
const app = express();
app.use(express.json());

let books = [
  { id: 1, title: '1984', author: 'George Orwell', publishedYear: 1949 },
  { id: 2, title: 'The Hobbit', author: 'J.R.R. Tolkien', publishedYear: 1937 }
];

// Read all
app.get('/api/books', (req, res) => res.json(books));

// Read one
app.get('/api/books/:bookId', (req, res) => {
  const id = Number(req.params.bookId);
  const book = books.find(b => b.id === id);
  if (!book) return res.status(404).json({ error: 'Book not found' });
  res.json(book);
});

// Create
app.post(
  '/api/books',
  [check('title').notEmpty(), check('author').notEmpty(), check('publishedYear').isInt()],
  (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) return res.status(400).json({ errors: errors.array() });
    const { title, author, publishedYear } = req.body;
    const newBook = { id: books.length ? books[books.length - 1].id + 1 : 1, title, author, publishedYear };
    books.push(newBook);
    res.status(201).json(newBook);
  }
);

const PORT = process.env.PORT || 5000;
if (require.main === module) {
  app.listen(PORT, () => console.log(`Book API running on port ${PORT}`));
}

module.exports = app;
