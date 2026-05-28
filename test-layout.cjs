const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });
  
  try {
    await page.goto('http://localhost:5174', { waitUntil: 'networkidle' });
    
    const layoutInfo = await page.evaluate(async () => {
      const sleep = ms => new Promise(r => setTimeout(r, ms));
      
      const workSection = document.querySelector('.work-section');
      const certSection = document.querySelector('.cert-section');
      
      let report = `INITIAL STATE:\n`;
      report += `workSection top: ${workSection.getBoundingClientRect().top}\n`;
      report += `certSection top: ${certSection.getBoundingClientRect().top}\n`;
      
      window.scrollTo(0, 1000);
      await sleep(1000);
      
      report += `\nSCROLLED 1000px:\n`;
      report += `workSection top: ${workSection.getBoundingClientRect().top}\n`;
      report += `certSection top: ${certSection.getBoundingClientRect().top}\n`;
      
      return report;
    });
    
    console.log(layoutInfo);
    
  } catch (err) {
    console.error(err);
  } finally {
    await browser.close();
  }
})();
