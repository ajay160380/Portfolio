import "./styles/Career.css";
import { useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(ScrollTrigger);

const Career = () => {
  const sectionRef = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    const section = sectionRef.current;
    if (!section) return;
    if (window.innerWidth <= 1024) return;

    // Animate the career timeline bar growing downward
    gsap.to(section.querySelector(".career-timeline"), {
      maxHeight: "100%",
      duration: 2,
      ease: "power2.out",
      scrollTrigger: {
        trigger: section.querySelector(".career-info"),
        start: "top 70%",
        end: "bottom 60%",
        scrub: 1,
      },
    });

    // Animate each career-info-box sliding in
    const boxes = section.querySelectorAll(".career-info-box");
    boxes.forEach((box, i) => {
      gsap.fromTo(
        box,
        { y: 60, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 0.8,
          delay: i * 0.15,
          ease: "power3.out",
          scrollTrigger: {
            trigger: box,
            start: "top 88%",
            toggleActions: "play none none reverse",
          },
        }
      );
    });

    // Animate the heading
    gsap.fromTo(
      section.querySelector("h2"),
      { y: 80, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: {
          trigger: section.querySelector("h2"),
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );
  }, []);

  return (
    <div className="career-section section-container" ref={sectionRef}>
      <div className="career-container">
        <h2>
          My Education <span>&</span>
          <br /> Experience
        </h2>
        <div className="career-info">
          <div className="career-timeline">
            <div className="career-dot"></div>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>B.Tech CSE (Artificial Intelligence)</h4>
                <h5>BBD University, Lucknow</h5>
              </div>
              <h3>NOW</h3>
            </div>
            <p>
              Currently pursuing 4th Year, 7th Semester with <strong>8.63 CGPA</strong>. 
              Focused on AI/ML, full-stack development, and building real-world 
              projects that solve meaningful problems.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>NSS Volunteer</h4>
                <h5>National Service Scheme</h5>
              </div>
              <h3>2 Yrs</h3>
            </div>
            <p>
              Completed two years of service through NSS, contributing to
              outreach activities, social initiatives, and community-level
              engagement.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Tech Expo'26 — Certificate of Appreciation</h4>
                <h5>BBD University, Lucknow</h5>
              </div>
              <h3>2026</h3>
            </div>
            <p>
              Recognized for participating in Tech Expo'26 with the Smart Women's
              Safety Device — demonstrating hardware innovation for real-world
              social impact.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Career;
