const fs = require('fs').promises;
const path = require('path');

async function copyLocal() {
	try {
		const source = path.resolve(__dirname, 'source.txt');
		const dest = path.resolve(__dirname, 'destination.txt');
		const data = await fs.readFile(source, 'utf8');
		await fs.writeFile(dest, data, 'utf8');
		console.log('File copied to', dest);
	} catch (err) {
		console.error('Copy failed:', err.message);
	}
}

if (require.main === module) copyLocal();

module.exports = { copyLocal };
