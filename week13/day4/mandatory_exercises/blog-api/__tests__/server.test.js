const request = require('supertest');
const app = require('../server');

describe('Blog API', () => {
  test('GET /posts returns posts', async () => {
    const res = await request(app).get('/posts');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  test('POST /posts validates input', async () => {
    const res = await request(app).post('/posts').send({ title: '', content: '' });
    expect(res.statusCode).toBe(400);
  });
});
