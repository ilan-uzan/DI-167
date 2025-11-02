const fs = require('fs').promises;
const path = require('path');

async function listFiles() {
	try {
		const dir = path.resolve(__dirname);
		const files = await fs.readdir(dir);
		console.log('Files in folder:', files);
		return files;
	} catch (err) {
		console.error('Read directory failed:', err.message);
		return [];
	}
}

if (require.main === module) listFiles();

module.exports = { listFiles };
