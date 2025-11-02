let greet = (n) => `Hello, ${n}`;
let colorful = (s) => s;
let readData = async () => '';

try {
	greet = require('./greeting').greet;
} catch (e) {
	console.warn('greeting module missing:', e.message);
}

try {
	colorful = require('./colorful-message').colorful;
} catch (e) {
	console.warn('colorful-message module missing:', e.message);
}

try {
	readData = require('./read-file').readData;
} catch (e) {
	console.warn('read-file module missing:', e.message);
}

(async () => {
	try {
		console.log(greet('Ilan'));
		console.log(colorful('This is colorful!'));
		const data = await readData();
		console.log('File contents:\n', data);
	} catch (err) {
		console.error('Error in challenge:', err.message);
	}
})();
