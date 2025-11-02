const { greet } = require('./greeting');
const { colorful } = require('./colorful-message');
const { readData } = require('./read-file');

(async () => {
	try {
		console.log(greet('Ilan'));
		console.log(colorful('A colorful demo'));
		const data = await readData();
		console.log('Read data:\n', data);
	} catch (err) {
		console.error('App error:', err.message);
	}
})();
