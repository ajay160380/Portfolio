import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  page.on('console', msg => {
    if (msg.type() === 'error') {
      console.log(`[ERROR] ${msg.text()}`);
    } else {
      console.log(`[LOG] ${msg.text()}`);
    }
  });

  page.on('pageerror', exception => {
    console.log(`[PAGE ERROR] ${exception}`);
  });

  await page.goto('http://localhost:5173');
  await page.waitForTimeout(5000); // wait a bit for loading
  
  await browser.close();
})();
