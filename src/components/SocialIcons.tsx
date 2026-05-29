import {
  FaGithub,
  FaLinkedinIn,
} from "react-icons/fa6";
import "./styles/SocialIcons.css";
import { TbNotes } from "react-icons/tb";
import { useEffect } from "react";
import gsap from "gsap";
import HoverLinks from "./HoverLinks";

const SocialIcons = () => {
  useEffect(() => {
    const social = document.getElementById("social") as HTMLElement;
    const spans = social.querySelectorAll("span");
    
    // Pre-calculate all defaults
    const iconData = Array.from(spans).map((item) => {
      const elem = item as HTMLElement;
      const link = elem.querySelector("a") as HTMLElement;
      const rect = elem.getBoundingClientRect();
      const defaultX = rect.width / 2;
      const defaultY = rect.height / 2;
      
      link.style.setProperty("--siLeft", `${defaultX}px`);
      link.style.setProperty("--siTop", `${defaultY}px`);

      return {
        elem,
        link,
        rect,
        defaultX,
        defaultY,
        xTo: gsap.quickTo(link, "--siLeft", { duration: 0.3, ease: "power3.out" }),
        yTo: gsap.quickTo(link, "--siTop", { duration: 0.3, ease: "power3.out" }),
      };
    });

    // Single listener for all icons instead of one per icon
    const onMouseMove = (e: MouseEvent) => {
      iconData.forEach(({ rect, defaultX, defaultY, xTo, yTo }) => {
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        if (x < 40 && x > 10 && y < 40 && y > 5) {
          xTo(x);
          yTo(y);
        } else {
          xTo(defaultX);
          yTo(defaultY);
        }
      });
    };

    document.addEventListener("mousemove", onMouseMove);

    return () => {
      document.removeEventListener("mousemove", onMouseMove);
    };
  }, []);

  return (
    <div className="icons-section">
      <div className="social-icons" data-cursor="icons" id="social">
        <span>
          <a href="https://github.com/ajay160380" target="_blank">
            <FaGithub />
          </a>
        </span>
        <span>
          <a href="https://www.linkedin.com/in/ajay-vishwakarma-71649129a/" target="_blank">
            <FaLinkedinIn />
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
