import React, { useEffect, useRef } from "react";
import { useTheme } from "../context/ThemeProvider";

const AnimatedBackground: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const { theme } = useTheme();

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    // Use low-power rendering hints
    const ctx = canvas.getContext("2d", { alpha: true, desynchronized: true });
    if (!ctx) return;

    // Drastically reduced particle count for smooth performance
    const isMobile = window.innerWidth < 768;
    const particleCount = isMobile ? 8 : 14;

    const getAccentRGB = (t: string) => {
      switch (t) {
        case "cyan":    return "0, 242, 254";
        case "emerald": return "0, 255, 157";
        case "crimson": return "255, 60, 60";
        case "purple":
        default:        return "180, 140, 255";
      }
    };
    const accentColor = getAccentRGB(theme);

    // Pre-compute styles once (avoid string concat every frame)
    const particleFill = `rgba(${accentColor}, 0.4)`;
    const lineStroke = `rgba(${accentColor}, 0.06)`;

    let animationFrameId: number;

    // Simple particle data (no class overhead)
    const px: number[] = [];
    const py: number[] = [];
    const pvx: number[] = [];
    const pvy: number[] = [];
    const psize: number[] = [];

    const init = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      px.length = 0; py.length = 0; pvx.length = 0; pvy.length = 0; psize.length = 0;
      for (let i = 0; i < particleCount; i++) {
        px.push(Math.random() * canvas.width);
        py.push(Math.random() * canvas.height);
        pvx.push((Math.random() - 0.5) * 0.35);
        pvy.push((Math.random() - 0.5) * 0.35);
        psize.push(Math.random() * 1.5 + 0.8);
      }
    };

    let isPageVisible = !document.hidden;
    let isScrolling = false;
    let scrollTimeout: ReturnType<typeof setTimeout>;
    let lastFrameTime = 0;
    const FRAME_INTERVAL = 1000 / 24; // Cap at 24fps — smooth enough, saves GPU

    const handleVisibilityChange = () => { isPageVisible = !document.hidden; };
    const handleScroll = () => {
      isScrolling = true;
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(() => { isScrolling = false; }, 250);
    };

    document.addEventListener("visibilitychange", handleVisibilityChange);
    window.addEventListener("scroll", handleScroll, { passive: true });

    const CONNECTION_DIST_SQ = 8100; // 90^2

    const animate = (timestamp: number) => {
      animationFrameId = requestAnimationFrame(animate);

      // Skip frames to maintain target FPS
      if (timestamp - lastFrameTime < FRAME_INTERVAL) return;
      lastFrameTime = timestamp;

      // Don't render when page hidden or during scroll
      if (!isPageVisible || isScrolling) return;

      const cw = canvas.width;
      const ch = canvas.height;
      ctx.clearRect(0, 0, cw, ch);

      // Update & draw particles in one pass
      ctx.fillStyle = particleFill;
      for (let i = 0; i < particleCount; i++) {
        px[i] += pvx[i];
        py[i] += pvy[i];
        if (px[i] < 0 || px[i] > cw) pvx[i] = -pvx[i];
        if (py[i] < 0 || py[i] > ch) pvy[i] = -pvy[i];

        ctx.beginPath();
        ctx.arc(px[i], py[i], psize[i], 0, 6.283185);
        ctx.fill();
      }

      // Draw connections — single batched path
      ctx.beginPath();
      ctx.strokeStyle = lineStroke;
      ctx.lineWidth = 0.5;
      for (let i = 0; i < particleCount; i++) {
        for (let j = i + 1; j < particleCount; j++) {
          const dx = px[i] - px[j];
          const dy = py[i] - py[j];
          if (dx * dx + dy * dy < CONNECTION_DIST_SQ) {
            ctx.moveTo(px[i], py[i]);
            ctx.lineTo(px[j], py[j]);
          }
        }
      }
      ctx.stroke();
    };

    // Debounced resize
    let resizeTimeout: ReturnType<typeof setTimeout>;
    const handleResize = () => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(init, 300);
    };

    init();
    animationFrameId = requestAnimationFrame(animate);

    window.addEventListener("resize", handleResize);

    return () => {
      document.removeEventListener("visibilitychange", handleVisibilityChange);
      window.removeEventListener("scroll", handleScroll);
      window.removeEventListener("resize", handleResize);
      cancelAnimationFrame(animationFrameId);
      clearTimeout(scrollTimeout);
      clearTimeout(resizeTimeout);
    };
  }, [theme]);

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        width: "100vw",
        height: "100vh",
        zIndex: 0,
        pointerEvents: "none",
      }}
    />
  );
};

export default AnimatedBackground;
