const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  const htmlPath = 'file://' + path.resolve(__dirname, 'public/resume.html');
  await page.goto(htmlPath, {waitUntil: 'networkidle0'});
  await page.pdf({
    path: 'public/Ajay_Vishwakarma_Resume.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '0', right: '0', bottom: '0', left: '0' }
  });
  await browser.close();
  console.log("PDF generated successfully at public/Ajay_Vishwakarma_Resume.pdf");
})();
