const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });
  
  try {
    await page.goto('http://localhost:5174', { waitUntil: 'networkidle' });
    console.log("Page loaded");
    
    // Scroll down 800px to trigger the issue
    await page.evaluate(() => window.scrollTo(0, 800));
    await page.waitForTimeout(1000); // wait for GSAP to process
    
    await page.screenshot({ path: 'screenshot1.png' });
    console.log("Saved screenshot1.png");

    await page.evaluate(() => window.scrollTo(0, 1600));
    await page.waitForTimeout(1000); 
    
    await page.screenshot({ path: 'screenshot2.png' });
    console.log("Saved screenshot2.png");
    
  } catch (err) {
    console.error(err);
  } finally {
    await browser.close();
  }
})();
