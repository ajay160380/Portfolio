import { useState, useEffect } from "react";
import { FaArrowUp } from "react-icons/fa";
import "./styles/ScrollToTop.css";

const ScrollToTop = () => {
  const [isVisible, setIsVisible] = useState(false);
  const [scrollProgress, setScrollProgress] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      // In GSAP ScrollSmoother, we might need to check if body scrolled or wrapper
      // Fallback to window scroll
      const scrollY = window.scrollY || document.documentElement.scrollTop;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollY / docHeight) * 100 : 0;
      
      setScrollProgress(progress);
      
      if (scrollY > 400) {
        setIsVisible(true);
      } else {
        setIsVisible(false);
      }
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  };

  const radius = 22;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (scrollProgress / 100) * circumference;

  return (
    <button 
      className={`scroll-to-top ${isVisible ? "visible" : ""}`}
      onClick={scrollToTop}
      aria-label="Scroll to top"
    >
      <div className="progress-ring-container">
        <svg className="progress-ring" width="50" height="50">
          <circle 
            className="progress-ring-circle-bg" 
            strokeWidth="3" 
            stroke="rgba(255, 255, 255, 0.1)" 
            fill="transparent" 
            r={radius} 
            cx="25" 
            cy="25"
          />
          <circle 
            className="progress-ring-circle" 
            strokeWidth="3" 
            stroke="var(--accentColor)" 
            fill="transparent" 
            r={radius} 
            cx="25" 
            cy="25"
            style={{
              strokeDasharray: circumference,
              strokeDashoffset: strokeDashoffset
            }}
          />
        </svg>
      </div>
      <FaArrowUp className="arrow-icon" />
    </button>
  );
};

export default ScrollToTop;
