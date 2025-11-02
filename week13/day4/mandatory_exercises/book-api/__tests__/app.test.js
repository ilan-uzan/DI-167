const request = require('supertest');
const app = require('../app');

describe('Book API', () => {
  test('GET /api/books returns books', async () => {
    const res = await request(app).get('/api/books');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  test('POST /api/books requires fields', async () => {
    const res = await request(app).post('/api/books').send({ title: 'x' });
    expect(res.statusCode).toBe(400);
  });
});
