const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
  
  try {
    await page.goto('http://localhost:5173', { waitUntil: 'networkidle' });
    console.log("Page loaded");
    
    // Check initial state
    let workFlexWidth = await page.evaluate(() => {
      let flex = document.querySelector('.work-flex');
      return flex ? flex.scrollWidth : null;
    });
    console.log("Initial workFlex scrollWidth:", workFlexWidth);
    
    let translateX = await page.evaluate(() => {
      let boxes = document.querySelectorAll(".work-box");
      if (boxes.length > 0) {
        let boxWidth = boxes[0].getBoundingClientRect().width;
        return boxWidth * boxes.length - window.innerWidth + 200;
      }
      return 0;
    });
    console.log("Calculated getTranslateX:", translateX);
    
    // Check pin-spacer padding
    let pinSpacer = await page.evaluate(() => {
      let spacer = document.querySelector('.pin-spacer');
      return spacer ? getComputedStyle(spacer).paddingBottom : 'No spacer';
    });
    console.log("Pin spacer padding bottom:", pinSpacer);
    
  } catch (err) {
    console.error(err);
  } finally {
    await browser.close();
  }
})();
