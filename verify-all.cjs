const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });
  
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
  
  try {
    await page.goto('http://localhost:5174', { waitUntil: 'networkidle' });
    console.log("✅ Page loaded without errors");
    
    // Check all sections exist
    const sections = await page.evaluate(() => {
      const checks = {};
      checks.landing = !!document.querySelector('.landing-section');
      checks.about = !!document.querySelector('#about');
      checks.work = !!document.querySelector('.work-section');
      checks.certificates = !!document.querySelector('.cert-section');
      checks.certFeatured = !!document.querySelector('.cert-featured');
      checks.certGrid = !!document.querySelector('.cert-grid');
      checks.certCards = document.querySelectorAll('.cert-card').length;
      checks.contact = !!document.querySelector('.contact-section');
      checks.contactForm = !!document.querySelector('.contact-form');
      checks.nameInput = !!document.querySelector('#name');
      checks.emailInput = !!document.querySelector('#email');
      checks.messageInput = !!document.querySelector('#message');
      checks.sendBtn = !!document.querySelector('.form-btn');
      checks.techstack = !!document.querySelector('.techstack');
      return checks;
    });
    
    console.log("\n📋 SECTION CHECK:");
    for (const [key, val] of Object.entries(sections)) {
      console.log(`  ${val ? '✅' : '❌'} ${key}: ${val}`);
    }
    
    // Check project images
    const images = await page.evaluate(() => {
      const imgs = document.querySelectorAll('.work-image img');
      return Array.from(imgs).map(img => ({
        src: img.getAttribute('src'),
        loaded: img.naturalWidth > 0
      }));
    });
    console.log("\n🖼️  PROJECT IMAGES:");
    images.forEach((img, i) => {
      console.log(`  ${img.loaded ? '✅' : '❌'} Project ${i+1}: ${img.src} (loaded: ${img.loaded})`);
    });
    
    // Take full page screenshot
    await page.screenshot({ path: 'full-page.png', fullPage: true });
    console.log("\n📸 Full page screenshot saved!");
    
  } catch (err) {
    console.error("❌ ERROR:", err.message);
  } finally {
    await browser.close();
  }
})();
