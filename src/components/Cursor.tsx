import { useEffect, useRef } from "react";
import "./styles/Cursor.css";
import gsap from "gsap";

const Cursor = () => {
  const cursorRef = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    let hover = false;
    const cursor = cursorRef.current!;
    
    // Create highly optimized quick setters for GSAP
    const xTo = gsap.quickTo(cursor, "x", { duration: 0.15, ease: "power3" });
    const yTo = gsap.quickTo(cursor, "y", { duration: 0.15, ease: "power3" });

    const handleMouseMove = (e: MouseEvent) => {
      if (!hover) {
        xTo(e.clientX);
        yTo(e.clientY);
      }
    };
    
    document.addEventListener("mousemove", handleMouseMove);

    const elements = document.querySelectorAll("[data-cursor]");
    
    elements.forEach((item) => {
      const element = item as HTMLElement;
      
      element.addEventListener("mouseover", (e: MouseEvent) => {
        const target = e.currentTarget as HTMLElement;
        const rect = target.getBoundingClientRect();

        if (element.dataset.cursor === "icons") {
          cursor.classList.add("cursor-icons");
          gsap.to(cursor, { x: rect.left, y: rect.top, duration: 0.1 });
          cursor.style.setProperty("--cursorH", `${rect.height}px`);
          hover = true;
        }
        if (element.dataset.cursor === "disable") {
          cursor.classList.add("cursor-disable");
        }
      });
      
      element.addEventListener("mouseout", () => {
        cursor.classList.remove("cursor-disable", "cursor-icons");
        hover = false;
      });
    });

    return () => {
      document.removeEventListener("mousemove", handleMouseMove);
    };
  }, []);

  return <div className="cursor-main" ref={cursorRef}></div>;
};

export default Cursor;
