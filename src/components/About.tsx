import "./styles/About.css";
import { useRef, useState, useEffect } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(ScrollTrigger);

const stats = [
  { target: 6, suffix: "+", label: "Projects Built" },
  { target: 10, suffix: "+", label: "Certifications" },
  { target: 2, suffix: "", label: "Years NSS" },
  { target: 8.63, suffix: "", decimals: 2, label: "Latest CGPA" },
  { target: 3, suffix: "rd", label: "Year B.Tech" },
];

const About = () => {
  const sectionRef = useRef<HTMLDivElement>(null);
  const [activeTab, setActiveTab] = useState<"bio" | "focus" | "achievements">("bio");

  useGSAP(() => {
    const section = sectionRef.current;
    if (!section) return;

    // Animate the About text elements
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

    // Count animation for stats numbers
    const statNumbers = section.querySelectorAll(".stat-number");
    statNumbers.forEach((el) => {
      const target = parseFloat(el.getAttribute("data-target") || "0");
      const suffix = el.getAttribute("data-suffix") || "";
      const decimals = parseInt(el.getAttribute("data-decimals") || "0", 10);
      const valObj = { val: 0 };
      
      gsap.fromTo(
        valObj,
        { val: 0 },
        {
          val: target,
          duration: 1.5,
          ease: "power3.out",
          scrollTrigger: {
            trigger: el,
            start: "top 92%",
            toggleActions: "play none none reverse",
          },
          onUpdate: () => {
            el.textContent = valObj.val.toFixed(decimals) + suffix;
          },
        }
      );
    });

    // Animate stats cards with stagger
    const statCards = section.querySelectorAll(".stat-card");
    gsap.fromTo(
      statCards,
      { y: 80, opacity: 0, scale: 0.85 },
      {
        y: 0,
        opacity: 1,
        scale: 1,
        duration: 0.7,
        stagger: 0.15,
        ease: "back.out(1.7)",
        scrollTrigger: {
          trigger: section.querySelector(".about-stats"),
          start: "top 92%",
          toggleActions: "play none none reverse",
        },
      }
    );
  }, []);

  // Smooth fade-in tab content transitions when tab changes
  useEffect(() => {
    const pane = sectionRef.current?.querySelector(".tab-pane");
    if (pane) {
      gsap.fromTo(
        pane,
        { opacity: 0, y: 15, scale: 0.98 },
        { opacity: 1, y: 0, scale: 1, duration: 0.4, ease: "power2.out" }
      );
    }
  }, [activeTab]);

  return (
    <div className="about-section" id="about" ref={sectionRef}>
      <div className="about-me">
        <div className="about-label">
          <span className="about-line"></span>
          <h3 className="title">About Me</h3>
        </div>
        
        <p className="para">
          I'm <span className="highlight">Ajay Vishwakarma</span>, a 3rd-year B.Tech CSE (Artificial Intelligence) student at BBD University, Lucknow. I am passionate about building impactful technology that bridges the gap between AI theory and real-world execution.
        </p>

        {/* Tab Selection buttons */}
        <div className="about-tabs-container">
          <div className="about-tabs">
            <button
              className={`tab-btn ${activeTab === "bio" ? "active" : ""}`}
              onClick={() => setActiveTab("bio")}
            >
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
              </svg>
              Biography
            </button>
            <button
              className={`tab-btn ${activeTab === "focus" ? "active" : ""}`}
              onClick={() => setActiveTab("focus")}
            >
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/>
              </svg>
              Core Focus
            </button>
            <button
              className={`tab-btn ${activeTab === "achievements" ? "active" : ""}`}
              onClick={() => setActiveTab("achievements")}
            >
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M19 5h-2V3H7v2H5c-1.1 0-2 .9-2 2v3c0 2.44 1.72 4.48 4 4.88v2.12c0 2.2 1.8 4 4 4h2c2.2 0 4-1.8 4-4v-2.12c2.28-.4 4-2.44 4-4.88V7c0-1.1-.9-2-2-2zM5 10V7h2v3H5zm14 0h-2V7h2v3z"/>
              </svg>
              Achievements
            </button>
          </div>
        </div>

        {/* Dynamic Tab Pane content */}
        <div className="tab-content-wrapper">
          {activeTab === "bio" && (
            <div className="tab-pane bio-pane">
              <div className="bio-grid">
                <div className="bio-item">
                  <span className="bio-label">Current Role</span>
                  <span className="bio-value">AI Explorer & Full Stack Developer</span>
                </div>
                <div className="bio-item">
                  <span className="bio-label">University</span>
                  <span className="bio-value">BBD University, Lucknow</span>
                </div>
                <div className="bio-item">
                  <span className="bio-label">Academic Track</span>
                  <span className="bio-value">B.Tech CSE (Artificial Intelligence)</span>
                </div>
                <div className="bio-item">
                  <span className="bio-label">Academic Performance</span>
                  <span className="bio-value">8.63 CGPA (Latest Semester)</span>
                </div>
                <div className="bio-item">
                  <span className="bio-label">Location</span>
                  <span className="bio-value">Lucknow, UP, India</span>
                </div>
                <div className="bio-item">
                  <span className="bio-label">Core Philosophy</span>
                  <span className="bio-value">Build tech that makes a social impact</span>
                </div>
              </div>
              <div className="bio-quote">
                "The best way to explore Artificial Intelligence is to build working interfaces that humans can seamlessly interact with."
              </div>
            </div>
          )}

          {activeTab === "focus" && (
            <div className="tab-pane focus-pane">
              <div className="focus-grid">
                <div className="focus-card">
                  <div className="focus-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8z" />
                      <path d="M12 2v2M12 20v2M4 12H2M22 12h-2M5.75 5.75l1.41 1.41M16.84 16.84l1.41 1.41M5.75 18.25l1.41-1.41M16.84 7.16l1.41-1.41" />
                    </svg>
                  </div>
                  <div className="focus-info">
                    <h4>Artificial Intelligence</h4>
                    <p>Building intelligent web agents, predictive healthcare modules, and NLP-driven edutech solutions.</p>
                  </div>
                </div>

                <div className="focus-card">
                  <div className="focus-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <polygon points="12 2 2 7 12 12 22 7 12 2" />
                      <polyline points="2 17 12 22 22 17" />
                      <polyline points="2 12 12 17 22 12" />
                    </svg>
                  </div>
                  <div className="focus-info">
                    <h4>Full Stack Engineering</h4>
                    <p>Designing performant server structures, responsive interfaces, and custom visual layers.</p>
                  </div>
                </div>

                <div className="focus-card main-project-card">
                  <div className="focus-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M22 10v6M2 10l10-5 10 5-10 5z" />
                      <path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5" />
                    </svg>
                  </div>
                  <div className="focus-info">
                    <h4>EduTech AI (Main Project)</h4>
                    <p>Building a full-stack learning SaaS powered by Groq LLM, custom AI study guides, structured roadmaps, and secure Razorpay checkouts.</p>
                  </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === "achievements" && (
            <div className="tab-pane achievements-pane">
              <div className="achievements-list">
                <div className="achievement-item">
                  <div className="achievement-badge">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6" />
                      <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18" />
                      <path d="M4 22h16" />
                      <path d="M10 14.66V17c0 .55-.45 1-1 1H4v2h16v-2h-5c-.55 0-1-.45-1-1v-2.34" />
                      <path d="M12 2a6 6 0 0 1 6 6v5a6 6 0 0 1-6 6 6 6 0 0 1-6-6V8a6 6 0 0 1 6-6z" />
                    </svg>
                  </div>
                  <div className="achievement-info">
                    <span className="achievement-title">10+ Professional Certifications</span>
                    <span className="achievement-subtitle">Google, deep learning models, advanced DSA, and full-stack disciplines.</span>
                  </div>
                </div>

                <div className="achievement-item">
                  <div className="achievement-badge">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                    </svg>
                  </div>
                  <div className="achievement-info">
                    <span className="achievement-title">2 Years Active NSS Leader</span>
                    <span className="achievement-subtitle">Successfully completed community services, and outreach drives with NSS BBDU.</span>
                  </div>
                </div>

                <div className="achievement-item">
                  <div className="achievement-badge">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <circle cx="12" cy="8" r="7" />
                      <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88" />
                    </svg>
                  </div>
                  <div className="achievement-info">
                    <span className="achievement-title">Tech Expo'26 Innovator Award</span>
                    <span className="achievement-subtitle">Appreciated for developing and demonstrating the Smart Women's Safety Device.</span>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Futuristic Stats Grid */}
        <div className="about-stats">
          {stats.map((stat, i) => (
            <div className="stat-card" key={i}>
              <h2
                className="stat-number"
                data-target={stat.target}
                data-suffix={stat.suffix}
                data-decimals={stat.decimals || 0}
              >
                0{stat.suffix}
              </h2>
              <p>{stat.label}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default About;
