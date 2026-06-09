import { useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import "./styles/Testimonials.css";
import { FaQuoteLeft } from "react-icons/fa";

gsap.registerPlugin(ScrollTrigger);

const testimonialsData = [
  {
    id: 1,
    name: "Vikram Singh",
    role: "Senior Software Engineer",
    text: "Ajay's work on the EduTech AI platform was exceptional. He quickly grasped complex LLM integrations and delivered a seamless full-stack solution. His problem-solving skills are top-notch.",
    initials: "VS",
    color: "#ff6b6b"
  },
  {
    id: 2,
    name: "Dr. Anjali Desai",
    role: "Project Mentor, BBD University",
    text: "I was thoroughly impressed by Ajay's dedication to his AI/ML projects. His Digital Twin Platform showcases a deep understanding of natural language processing and modern web architecture.",
    initials: "AD",
    color: "#4ecdc4"
  },
  {
    id: 3,
    name: "Rohit Verma",
    role: "Tech Lead",
    text: "We collaborated on a project and Ajay's speed and code quality were fantastic. He's very proactive, understands requirements perfectly, and writes scalable, maintainable React/Node code.",
    initials: "RV",
    color: "#c2a4ff"
  }
];

const Testimonials = () => {
  const containerRef = useRef<HTMLDivElement>(null);
  const cardsRef = useRef<(HTMLDivElement | null)[]>([]);

  useEffect(() => {
    const ctx = gsap.context(() => {
      // Animate the title
      gsap.fromTo(
        ".testimonials-title",
        { y: 50, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 1,
          ease: "power3.out",
          scrollTrigger: {
            trigger: ".testimonials-section",
            start: "top 80%",
          },
        }
      );

      // Animate the cards
      cardsRef.current.forEach((card, index) => {
        if (!card) return;
        gsap.fromTo(
          card,
          { y: 100, opacity: 0 },
          {
            y: 0,
            opacity: 1,
            duration: 0.8,
            delay: index * 0.2,
            ease: "power3.out",
            scrollTrigger: {
              trigger: ".testimonials-section",
              start: "top 70%",
            },
          }
        );
      });
    }, containerRef);

    return () => ctx.revert();
  }, []);

  return (
    <div className="testimonials-section section-container" id="testimonials" ref={containerRef}>
      <h2 className="testimonials-title">
        People <span>Say</span>
      </h2>
      <div className="testimonials-grid">
        {testimonialsData.map((t, i) => (
          <div 
            key={t.id} 
            className="testimonial-card" 
            ref={(el) => (cardsRef.current[i] = el)}
          >
            <div className="quote-icon">
              <FaQuoteLeft />
            </div>
            <p className="testimonial-text">"{t.text}"</p>
            <div className="testimonial-author">
              <div 
                className="author-initials" 
                style={{ backgroundColor: t.color || 'var(--accentColor)' }}
              >
                {t.initials}
              </div>
              <div className="author-info">
                <h4>{t.name}</h4>
                <span>{t.role}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Testimonials;
