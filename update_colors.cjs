const fs = require('fs');
const path = require('path');

const stylesDir = path.join(__dirname, 'src', 'components', 'styles');

const replaceInFile = (filePath) => {
  let content = fs.readFileSync(filePath, 'utf8');
  let originalContent = content;

  // Replace RGB values of the old purple theme
  content = content.replace(/194,\s*164,\s*255/g, '255, 42, 42');
  content = content.replace(/85,\s*0,\s*255/g, '255, 0, 0');
  content = content.replace(/84,\s*0,\s*255/g, '255, 0, 0');

  // Replace Hex values of the old purple theme with red shades
  const replacements = {
    '#c2a4ff': '#ff2a2a',
    '#c481ff': '#ff2a2a',
    '#7f40ff': '#ff2a2a',
    '#aa42ff': '#ff0000',
    '#d29bff': '#ff4d4d',
    '#d097ff': '#ff3333',
    '#f2c0ff': '#ffcccc',
    '#f59bf8': '#ff4d4d',
    '#fb8dff': '#ff4d4d',
    '#cbb1ff': '#ff4d4d',
    '#d8c4ff': '#ff6666',
    '#a87cff': '#cc0000',
    '#e6c3ff': '#ff9999',
    '#9a7be6': '#b30000',
  };

  for (const [oldHex, newHex] of Object.entries(replacements)) {
    const regex = new RegExp(oldHex, 'gi');
    content = content.replace(regex, newHex);
  }

  if (content !== originalContent) {
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Updated: ${filePath}`);
  }
};

const processDirectory = (dir) => {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      processDirectory(fullPath);
    } else if (fullPath.endsWith('.css') || fullPath.endsWith('.ts') || fullPath.endsWith('.tsx')) {
      replaceInFile(fullPath);
    }
  }
};

processDirectory(path.join(__dirname, 'src', 'components'));
processDirectory(path.join(__dirname, 'src'));
