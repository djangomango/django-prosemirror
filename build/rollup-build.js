const { execSync } = require('child_process');

const input = `src/index.js`;
const outputDir = `../django_prosemirror/static/prosemirror/js`;

try {
  execSync(`node_modules/.bin/rollup ${input} -f iife -o ${outputDir}/pm.js -p @rollup/plugin-node-resolve -p @rollup/plugin-commonjs`, { stdio: 'inherit' });
  execSync(`node_modules/.bin/rollup ${input} -f iife -o ${outputDir}/pm.min.js -p @rollup/plugin-node-resolve -p @rollup/plugin-commonjs -p rollup-plugin-terser`, { stdio: 'inherit' });
} catch (error) {
  console.error('Error occurred while building:', error);
  process.exit(1);
}
