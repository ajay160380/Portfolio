const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });
  
  page.on('pageerror', err => console.log('❌ PAGE ERROR:', err.message));
  
  try {
    await page.goto('http://localhost:5174', { waitUntil: 'networkidle', timeout: 15000 });
    console.log("✅ Page loaded");
    
    // Check loading screen styles
    const loadingStyles = await page.evaluate(() => {
      const el = document.querySelector('.loading-screen');
      if (!el) return null;
      return window.getComputedStyle(el).backgroundColor;
    });
    console.log(`Loading background color: ${loadingStyles}`);
    
    // Take screenshot of the dark loading screen right away
    await page.reload();
    await page.waitForTimeout(500); // Wait for loading screen to render
    await page.screenshot({ path: 'dark-loading.png' });
    console.log("\n📸 Dark loading screenshot saved!");
    
  } catch (err) {
    console.error("❌ ERROR:", err.message);
  } finally {
    await browser.close();
  }
})();
