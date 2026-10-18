import { useEffect } from "react";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import HoverLinks from "./HoverLinks";
import { gsap } from "gsap";
import { ScrollSmoother } from "gsap/ScrollSmoother";
import { FaRobot } from "react-icons/fa6";
import ThemeToggle from "./ThemeToggle";
import "./styles/Navbar.css";

gsap.registerPlugin(ScrollSmoother, ScrollTrigger);
export let smoother: ScrollSmoother;

const Navbar = () => {
  useEffect(() => {
    const isDesktop = window.innerWidth > 1024;
    if (isDesktop) {
      smoother = ScrollSmoother.create({
        wrapper: "#smooth-wrapper",
        content: "#smooth-content",
        smooth: 0.8,
        speed: 1,
        effects: false,
      });

      smoother.scrollTop(0);
      smoother.paused(true);
    }

    const handleAnchorClick = (e: MouseEvent) => {
      const target = (e.target as HTMLElement).closest("a");
      if (!target) return;
      const href = target.getAttribute("data-href") || target.getAttribute("href");
      if (href && href.startsWith("#") && href.length > 1) {
        const targetElement = document.querySelector(href);
        if (targetElement) {
          e.preventDefault();
          if (window.innerWidth > 1024 && smoother) {
            smoother.scrollTo(href, true, "top top");
          } else {
            targetElement.scrollIntoView({ behavior: "smooth" });
          }
        }
      }
    };
    document.addEventListener("click", handleAnchorClick);

    const handleResize = () => {
      ScrollSmoother.refresh(true);
    };
    window.addEventListener("resize", handleResize);

    return () => {
      document.removeEventListener("click", handleAnchorClick);
      window.removeEventListener("resize", handleResize);
    };
  }, []);
  return (
    <>
      <div className="header">
        <div style={{ display: "flex", alignItems: "center", gap: "14px" }}>
          <a href="/#" className="navbar-title" data-cursor="disable">
            AV
          </a>
          <ThemeToggle />
        </div>
        <a
          href="mailto:ajaykumar160380@gmail.com"
          className="navbar-connect"
          data-cursor="disable"
        >
          ajaykumar160380@gmail.com
        </a>
        <ul>
          <li>
            <a data-href="#about" href="#about">
              <HoverLinks text="ABOUT" />
            </a>
          </li>
          <li>
            <a data-href="#work" href="#work">
              <HoverLinks text="WORK" />
            </a>
          </li>
          <li>
            <a data-href="#contact" href="#contact">
              <HoverLinks text="CONTACT" />
            </a>
          </li>
          <li>
            <a data-href="#terminal" href="#terminal">
              <HoverLinks text={<span style={{ display: "flex", alignItems: "center", gap: "6px" }}><FaRobot size={18} style={{ transform: "translateY(-2px)" }} /> ASK AI</span>} />
            </a>
          </li>
        </ul>
      </div>

      <div className="landing-circle1"></div>
      <div className="landing-circle2"></div>
      <div className="nav-fade"></div>
    </>
  );
};

export default Navbar;
