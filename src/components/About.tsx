import "./styles/About.css";
import { useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(ScrollTrigger);

const stats = [
  { number: "6+", label: "Projects Built" },
  { number: "10+", label: "Certifications" },
  { number: "2", label: "Years NSS" },
  { number: "3rd", label: "Year B.Tech" },
];

const About = () => {
  const sectionRef = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    const section = sectionRef.current;
    if (!section) return;

    // Animate the About text
    gsap.fromTo(
      section.querySelector(".about-me"),
      { y: 50, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.8,
        ease: "power3.out",
        scrollTrigger: {
          trigger: section,
          start: "top 75%",
          toggleActions: "play none none reverse",
        },
      }
    );

    // Animate stats cards with stagger
    const statCards = section.querySelectorAll(".stat-card");
    gsap.fromTo(
      statCards,
      { y: 40, opacity: 0, scale: 0.9 },
      {
        y: 0,
        opacity: 1,
        scale: 1,
        duration: 0.5,
        stagger: 0.1,
        ease: "back.out(1.5)",
        scrollTrigger: {
          trigger: section.querySelector(".about-stats"),
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );
  }, []);

  return (
    <div className="about-section" id="about" ref={sectionRef}>
      <div className="about-me">
        <div className="about-label">
          <span className="about-line"></span>
          <h3 className="title">About Me</h3>
        </div>
        <p className="para">
          I'm Ajay Vishwakarma, a 3rd-year B.Tech CSE (Artificial Intelligence) student at
          BBD University, Lucknow. I'm passionate about building impactful tech — from AI-powered
          education platforms and smart safety devices to full-stack web apps and digital twin
          simulations. With 2 years of NSS experience and 10+ certifications, I'm always learning,
          creating, and looking for opportunities to collaborate and grow.
        </p>
        <div className="about-stats">
          {stats.map((stat, i) => (
            <div className="stat-card" key={i}>
              <h2>{stat.number}</h2>
              <p>{stat.label}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default About;
