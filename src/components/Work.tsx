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
    description: "An advanced AI-powered educational platform featuring interactive learning modules, secure payments, and personalized LLM tutoring to ensure distraction-free learning.",
    tools: "Django, Groq LLM, PostgreSQL, Razorpay, Firebase, WebGL",
    link: "https://edu-tech-ai-vk2e.onrender.com",
    image: "/images/edutech.png",
  },
  {
    name: "AI Tutor",
    category: "AI / NLP Education Platform",
    description: "India's smartest AI tutor providing intelligent, real-time conversational learning paths. Accelerate your learning with personalized guidance from Class 5 to 12.",
    tools: "Django, Python, NLP, Groq LLM, SQLite, REST API",
    link: "https://edu-ai-ko5w.onrender.com",
    image: "/images/ai_tutor.png",
  },
  {
    name: "Expense Tracker",
    category: "Finance / AI WhatsApp Bot",
    description: "A smart expense tracking application that lives directly inside your WhatsApp. Zero apps required—just text your expenses, and our intelligent AI categorizes and tracks your budget automatically.",
    tools: "Python, WhatsApp API, Data Analytics, NLP",
    link: "https://ajay160380-paisa-mitra.hf.space",
    image: "/images/paisa.png",
  },
  {
    name: "Digital Twin Platform",
    category: "AI / Conversational Clone",
    description: "An intelligent AI clone designed to think, talk, and give suggestions exactly like a human. It acts as a personal digital twin, engaging in natural conversations and providing personalized advice.",
    tools: "Django, Python, JavaScript, Render",
    link: "https://digital-twin-jqav.onrender.com",
    image: "/images/digital_twin.png",
  },
  {
    name: "Healthcare Management System",
    category: "Full Stack Web App",
    description: "A comprehensive medical web application for seamless patient data management, intelligent appointment scheduling, and secure health record tracking.",
    tools: "React, Node.js, MongoDB, REST API",
    link: "https://healthcare-project-egyw.onrender.com",
    image: "/images/healthcare.png",
  },
  {
    name: "Smart Women's Safety Device",
    category: "Hardware / Safety Tech",
    description: "A life-saving IoT hardware project integrating real-time distress signaling, exact GPS location tracking, and an automated emergency alert system.",
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
                {project.description && <p style={{ fontSize: "14px", color: "#a3a3a3", marginTop: "-10px", lineHeight: "1.5" }}>{project.description}</p>}
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
