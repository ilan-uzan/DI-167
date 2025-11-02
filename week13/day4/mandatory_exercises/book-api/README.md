# Book API (Exercise 2)

Run:

```bash
node app.js
```

Endpoints:
- GET /api/books
- GET /api/books/:bookId
- POST /api/books { title, author, publishedYear }

Example curl:

```bash
curl http://localhost:5000/api/books
curl -X POST -H "Content-Type: application/json" -d '{"title":"New","author":"Me","publishedYear":2025}' http://localhost:5000/api/books
```
