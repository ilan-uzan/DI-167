const request = require('supertest');
const app = require('../app');

describe('CRUD API', () => {
  test('GET /posts proxies JSONPlaceholder', async () => {
    const res = await request(app).get('/posts');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  }, 10000);
});
