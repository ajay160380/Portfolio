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

  page.on('requestfailed', request => {
    console.log(`[FAILED REQUEST] ${request.url()} - ${request.failure()?.errorText}`);
  });
  
  page.on('response', response => {
    if (response.status() >= 400) {
      console.log(`[HTTP ERROR] ${response.status()} ${response.url()}`);
    }
  });

  page.on('pageerror', exception => {
    console.log(`[PAGE ERROR] ${exception}`);
  });

  await page.goto('https://ajay-portfolio-r176.onrender.com');
  await page.waitForTimeout(5000); // wait a bit for loading
  
  await browser.close();
})();
