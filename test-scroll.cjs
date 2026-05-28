const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  try {
    // Go to the running dev server
    await page.goto('http://localhost:5174', { waitUntil: 'networkidle' });
    console.log("Page loaded");
    
    // Evaluate layout dimensions and scroll positions
    const layoutInfo = await page.evaluate(async () => {
      // Helper to scroll
      const sleep = ms => new Promise(r => setTimeout(r, ms));
      
      const workSection = document.querySelector('.work-section');
      const workFlex = document.querySelector('.work-flex');
      const certSection = document.querySelector('.cert-section');
      
      if (!workSection || !certSection) return "Sections not found!";
      
      // Initial state
      let report = `INITIAL STATE:\n`;
      report += `workFlex scrollWidth: ${workFlex.scrollWidth}\n`;
      report += `workFlex clientWidth: ${workFlex.clientWidth}\n`;
      
      let boxes = document.querySelectorAll('.work-box');
      if (boxes.length > 0) {
        report += `Box 0 width: ${boxes[0].getBoundingClientRect().width}\n`;
      }
      
      // Scroll down gradually
      window.scrollTo(0, workSection.offsetTop);
      await sleep(500);
      
      report += `\nSCROLLED TO WORK SECTION:\n`;
      report += `workFlex transform: ${getComputedStyle(workFlex).transform}\n`;
      report += `certSection top: ${certSection.getBoundingClientRect().top}\n`;
      
      // Scroll down more to trigger GSAP horizontal scroll
      window.scrollTo(0, workSection.offsetTop + 1000);
      await sleep(500);
      
      report += `\nSCROLLED 1000px DEEP:\n`;
      report += `workFlex transform: ${getComputedStyle(workFlex).transform}\n`;
      report += `certSection top: ${certSection.getBoundingClientRect().top}\n`;
      
      // Scroll down to the end of the pin spacer
      let pinSpacer = document.querySelector('.pin-spacer');
      let spacerHeight = pinSpacer ? parseFloat(getComputedStyle(pinSpacer).paddingBottom) : 0;
      report += `\nPIN SPACER padding-bottom: ${spacerHeight}px\n`;
      
      window.scrollTo(0, workSection.offsetTop + spacerHeight + 100);
      await sleep(500);
      
      report += `\nSCROLLED PAST WORK SECTION:\n`;
      report += `workFlex transform: ${getComputedStyle(workFlex).transform}\n`;
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
