const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });
  
  page.on('pageerror', err => console.log('❌ PAGE ERROR:', err.message));
  
  try {
    await page.goto('http://localhost:5174', { waitUntil: 'networkidle', timeout: 15000 });
    console.log("✅ Page loaded");
    
    const checks = await page.evaluate(() => {
      const r = {};
      // Landing unique elements
      r.particles = !!document.querySelector('.landing-particles');
      r.greetingLine = !!document.querySelector('.greeting-line');
      r.statusDot = !!document.querySelector('.status-dot');
      r.scrollIndicator = !!document.querySelector('.landing-scroll-indicator');
      
      // About unique elements
      r.aboutLabel = !!document.querySelector('.about-label');
      r.aboutLine = !!document.querySelector('.about-line');
      r.statCards = document.querySelectorAll('.stat-card').length;
      
      // Certificates animations
      r.certSection = !!document.querySelector('.cert-section');
      r.certBadge = !!document.querySelector('.cert-badge');
      r.certCardNumbers = document.querySelectorAll('.cert-card-number').length;
      
      // Contact form
      r.contactForm = !!document.querySelector('.contact-form');
      r.contactHeading = !!document.querySelector('.contact-heading');
      r.contactInfoBoxes = document.querySelectorAll('.contact-info-box').length;
      
      // Projects
      r.projectImages = document.querySelectorAll('.work-image img').length;
      
      return r;
    });
    
    console.log("\n📋 UNIQUE ELEMENTS CHECK:");
    for (const [key, val] of Object.entries(checks)) {
      console.log(`  ${val ? '✅' : '❌'} ${key}: ${val}`);
    }
    
  } catch (err) {
    console.error("❌ ERROR:", err.message);
  } finally {
    await browser.close();
  }
})();
