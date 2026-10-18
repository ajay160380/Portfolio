import {
  FaGithub,
  FaLinkedinIn,
  FaTelegram,
} from "react-icons/fa6";
import "./styles/SocialIcons.css";
import { TbNotes } from "react-icons/tb";
import { useEffect } from "react";
import gsap from "gsap";
import HoverLinks from "./HoverLinks";

const SocialIcons = () => {
  useEffect(() => {
    const social = document.getElementById("social") as HTMLElement;
    if (!social) return;

    const spans = social.querySelectorAll("span");
    const cleanupFns: Array<() => void> = [];

    spans.forEach((item) => {
      const elem = item as HTMLElement;
      const link = elem.querySelector("a") as HTMLElement;
      if (!link) return;

      const rect = elem.getBoundingClientRect();
      const defaultX = rect.width / 2;
      const defaultY = rect.height / 2;

      link.style.setProperty("--siLeft", `${defaultX}px`);
      link.style.setProperty("--siTop", `${defaultY}px`);

      const xTo = gsap.quickTo(link, "--siLeft", { duration: 0.3, ease: "power3.out" });
      const yTo = gsap.quickTo(link, "--siTop", { duration: 0.3, ease: "power3.out" });

      const onMouseMove = (e: MouseEvent) => {
        const itemRect = elem.getBoundingClientRect();
        const x = e.clientX - itemRect.left;
        const y = e.clientY - itemRect.top;
        xTo(x);
        yTo(y);
      };

      const onMouseLeave = () => {
        xTo(defaultX);
        yTo(defaultY);
      };

      elem.addEventListener("mousemove", onMouseMove);
      elem.addEventListener("mouseleave", onMouseLeave);

      cleanupFns.push(() => {
        elem.removeEventListener("mousemove", onMouseMove);
        elem.removeEventListener("mouseleave", onMouseLeave);
      });
    });

    return () => {
      cleanupFns.forEach((fn) => fn());
    };
  }, []);

  return (
    <div className="icons-section">
      <div className="social-icons" id="social">
        <span>
          <a href="https://github.com/ajay160380" target="_blank" rel="noreferrer" data-cursor="disable">
            <FaGithub />
          </a>
        </span>
        <span>
          <a href="https://www.linkedin.com/in/ajay-vishwakarma-71649129a/" target="_blank" rel="noreferrer" data-cursor="disable">
            <FaLinkedinIn />
          </a>
        </span>
        <span>
          <a href="https://t.me/Ajay_kumar_9936" target="_blank" rel="noreferrer" data-cursor="disable">
            <FaTelegram />
          </a>
        </span>
      </div>
      <a className="resume-button" href="/resume.html" target="_blank">
        <HoverLinks text="RESUME" />
        <span>
          <TbNotes />
        </span>
      </a>
    </div>
  );
};

export default SocialIcons;
