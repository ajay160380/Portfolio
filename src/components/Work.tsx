import "./styles/Work.css";
import WorkImage from "./WorkImage";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(useGSAP, ScrollTrigger);

const projects = [
  {
    name: "EduTech AI",
    category: "Full Stack SaaS / AI EdTech",
    tools: "Django, Groq LLM, PostgreSQL, Razorpay, Firebase, WebGL",
    link: "https://edu-tech-ai-vk2e.onrender.com",
    image: "/images/edutech.png",
  },
  {
    name: "AI Tutor",
    category: "AI / NLP Education Platform",
    tools: "Django, Python, NLP, Groq LLM, SQLite, REST API",
    link: "https://edu-ai-ko5w.onrender.com",
    image: "/images/ai_tutor.png",
  },
  {
    name: "Paisa Mitra",
    category: "Finance / Expense Tracker",
    tools: "Python, Data Analytics, Hugging Face",
    link: "https://ajay160380-paisa-mitra.hf.space",
    image: "/images/paisa.png",
  },
  {
    name: "Digital Twin Platform",
    category: "AI / Simulation Web App",
    tools: "Django, Python, JavaScript, Render",
    link: "https://digital-twin-jqav.onrender.com",
    image: "/images/digital_twin.png",
  },
  {
    name: "Healthcare Management System",
    category: "Full Stack Web App",
    tools: "React, Node.js, MongoDB, REST API",
    link: "https://healthcare-project-egyw.onrender.com",
    image: "/images/healthcare.png",
  },
  {
    name: "Smart Women's Safety Device",
    category: "Hardware / Safety Tech",
    tools: "ESP32, GPS, GSM, C++",
    link: "",
    image: "/images/safety.png",
  },
];

const Work = () => {
  useGSAP(() => {
    if (window.innerWidth <= 1024) return;

    const workFlex = document.querySelector(".work-flex") as HTMLElement;
    
    if (!workFlex) return;

    // Use GSAP's standard horizontal scroll calculation
    let getScrollAmount = () => -(workFlex.scrollWidth - window.innerWidth);

    const tween = gsap.to(workFlex, {
      x: getScrollAmount,
      ease: "none",
      scrollTrigger: {
        trigger: ".work-section",
        start: "top top",
        end: () => `+=${Math.abs(getScrollAmount())}`,
        pin: true,
        scrub: 1,
        invalidateOnRefresh: true,
      }
    });

    return () => {
      tween.kill();
    };
  }, []);
  return (
    <div className="work-section" id="work">
      <div className="work-container">
        <div className="section-container" style={{ margin: "0 auto" }}>
          <h2>
            My <span>Projects</span>
          </h2>
        </div>
        <div className="work-flex">
          {projects.map((project, index) => (
            <div className="work-box" key={index}>
              <div className="work-info">
                <div className="work-title">
                  <h3>0{index + 1}</h3>

                  <div>
                    <h4>{project.name}</h4>
                    <p>{project.category}</p>
                  </div>
                </div>
                <h4>Tools and features</h4>
                <p>{project.tools}</p>
              </div>
              <WorkImage
                image={project.image}
                alt={project.name}
                link={project.link || undefined}
              />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Work;
