# Blog API (Exercise 1)

Simple REST API for posts. Run:

```bash
node server.js
```

Endpoints:
- GET /posts
- GET /posts/:id
- POST /posts { title, content }
- PUT /posts/:id { title?, content? }
- DELETE /posts/:id

Example curl:

```bash
curl http://localhost:3000/posts
curl -X POST -H "Content-Type: application/json" -d '{"title":"New","content":"Hi"}' http://localhost:3000/posts
```
