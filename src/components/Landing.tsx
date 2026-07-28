import { PropsWithChildren, useEffect, useRef } from "react";
import "./styles/Landing.css";

const Landing = ({ children }: PropsWithChildren) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  // Floating particles background
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animId: number;
    const particles: { x: number; y: number; vx: number; vy: number; size: number; opacity: number }[] = [];

    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };
    resize();
    window.addEventListener("resize", resize);

    // Create particles
    for (let i = 0; i < 25; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: (Math.random() - 0.5) * 0.3,
        vy: (Math.random() - 0.5) * 0.3,
        size: Math.random() * 2 + 0.5,
        opacity: Math.random() * 0.4 + 0.1,
      });
    }

    let frameCount = 0;
    // Cache the RGB value and only update it every 60 frames
    let cachedRGB = getComputedStyle(document.body).getPropertyValue("--accentRGB").trim() || "255, 42, 42";

    let isVisible = true;
    let isTabActive = !document.hidden;

    const handleVisibilityChange = () => {
      isTabActive = !document.hidden;
    };
    document.addEventListener("visibilitychange", handleVisibilityChange);

    const observer = new IntersectionObserver(([entry]) => {
      isVisible = entry.isIntersecting;
    }, { threshold: 0.05 });
    observer.observe(canvas);

    const animate = () => {
      animId = requestAnimationFrame(animate);
      if (!isVisible || !isTabActive) return;

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      frameCount++;

      if (frameCount % 60 === 0) {
        cachedRGB = getComputedStyle(document.body).getPropertyValue("--accentRGB").trim() || "255, 42, 42";
      }

      particles.forEach((p) => {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${cachedRGB}, ${p.opacity})`;
        ctx.fill();
      });

      // Batch stroke calls for connection lines
      ctx.beginPath();
      ctx.strokeStyle = `rgba(${cachedRGB}, 0.04)`;
      ctx.lineWidth = 0.5;

      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const dx = particles[i].x - particles[j].x;
          const dy = particles[i].y - particles[j].y;
          if (dx * dx + dy * dy < 8100) { // 90^2
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
          }
        }
      }
      ctx.stroke();
    };
    animate();

    return () => {
      cancelAnimationFrame(animId);
      observer.disconnect();
      document.removeEventListener("visibilitychange", handleVisibilityChange);
      window.removeEventListener("resize", resize);
    };
  }, []);

  return (
    <>
      <div className="landing-section" id="landingDiv">
        <canvas ref={canvasRef} className="landing-particles" />
        <div className="landing-container">
          <div className="landing-intro">
            <div className="landing-greeting">
              <span className="greeting-line"></span>
              <h2>Hello! I'm</h2>
            </div>
            <h1>
              AJAY
              <br />
              <span>VISHWAKARMA</span>
            </h1>
            <div className="landing-status">
              <span className="status-dot"></span>
              Available for work
            </div>
          </div>
          <div className="landing-info">
            <h3>A Passionate</h3>
            <h2 className="landing-info-h2">
              <div className="landing-h2-1">AI/ML Dev</div>
              <div className="landing-h2-2">Full Stack</div>
            </h2>
            <h2>
              <div className="landing-h2-info">AI/ML Dev</div>
              <div className="landing-h2-info-1">Full Stack</div>
            </h2>
          </div>
          <div className="landing-scroll-indicator">
            <div className="scroll-mouse">
              <div className="scroll-wheel"></div>
            </div>
            <span>Scroll Down</span>
          </div>
        </div>
        {children}
      </div>
    </>
  );
};

export default Landing;
