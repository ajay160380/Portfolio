import { MdArrowOutward, MdCopyright, MdSend } from "react-icons/md";
import { useRef, useState } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";
import "./styles/Contact.css";

gsap.registerPlugin(ScrollTrigger);

const Contact = () => {
  const sectionRef = useRef<HTMLDivElement>(null);
  const [formData, setFormData] = useState({ name: "", email: "", message: "" });
  const [sending, setSending] = useState(false);
  const [sent, setSent] = useState(false);

  useGSAP(() => {
    const section = sectionRef.current;
    if (!section) return;

    // Animate the "Let's Talk" heading
    gsap.fromTo(
      section.querySelector(".contact-heading"),
      { y: 60, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.8,
        ease: "power3.out",
        scrollTrigger: {
          trigger: section,
          start: "top 80%",
          toggleActions: "play none none reverse",
        },
      }
    );

    // Animate the sub text
    gsap.fromTo(
      section.querySelector(".contact-subtext"),
      { y: 30, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.6,
        delay: 0.2,
        ease: "power3.out",
        scrollTrigger: {
          trigger: section,
          start: "top 80%",
          toggleActions: "play none none reverse",
        },
      }
    );

    // Animate the contact info boxes
    const boxes = section.querySelectorAll(".contact-info-box");
    gsap.fromTo(
      boxes,
      { y: 40, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.6,
        stagger: 0.12,
        ease: "power3.out",
        scrollTrigger: {
          trigger: section.querySelector(".contact-flex"),
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );

    // Animate the form
    gsap.fromTo(
      section.querySelector(".contact-form"),
      { y: 50, opacity: 0, scale: 0.98 },
      {
        y: 0,
        opacity: 1,
        scale: 1,
        duration: 0.8,
        delay: 0.3,
        ease: "power3.out",
        scrollTrigger: {
          trigger: section.querySelector(".contact-form"),
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );

    // Animate footer
    gsap.fromTo(
      section.querySelector(".contact-footer"),
      { y: 30, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.6,
        delay: 0.5,
        ease: "power3.out",
        scrollTrigger: {
          trigger: section.querySelector(".contact-footer"),
          start: "top 90%",
          toggleActions: "play none none reverse",
        },
      }
    );
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.name || !formData.email || !formData.message) return;

    setSending(true);

    // Use mailto to send directly to email
    const subject = encodeURIComponent(`Portfolio Message from ${formData.name}`);
    const body = encodeURIComponent(
      `Name: ${formData.name}\nEmail: ${formData.email}\n\nMessage:\n${formData.message}`
    );
    
    window.location.href = `mailto:ajaykumar160380@gmail.com?subject=${subject}&body=${body}`;
    
    setTimeout(() => {
      setSending(false);
      setSent(true);
      setFormData({ name: "", email: "", message: "" });
      setTimeout(() => setSent(false), 4000);
    }, 1000);
  };

  return (
    <div className="contact-section section-container" id="contact" ref={sectionRef}>
      <div className="contact-container">
        <div className="contact-top">
          <h3 className="contact-heading">
            Let's <span>Talk</span>
          </h3>
          <p className="contact-subtext">
            Got a project idea, a question, or just want to connect? Drop me a message!
          </p>
        </div>

        <div className="contact-grid">
          {/* Left: Info */}
          <div className="contact-flex">
            <div className="contact-info-box">
              <div className="contact-icon">📧</div>
              <h4>Email</h4>
              <a href="mailto:ajaykumar160380@gmail.com" data-cursor="disable">
                ajaykumar160380@gmail.com
              </a>
            </div>
            <div className="contact-info-box">
              <div className="contact-icon">📱</div>
              <h4>Phone</h4>
              <a href="tel:+917905398965" data-cursor="disable">
                +91 79053 98965
              </a>
            </div>
            <div className="contact-info-box">
              <div className="contact-icon">🔗</div>
              <h4>Social</h4>
              <div className="contact-social-links">
                <a
                  href="https://github.com/ajay160380"
                  target="_blank"
                  data-cursor="disable"
                  className="contact-social"
                >
                  Github <MdArrowOutward />
                </a>
                <a
                  href="https://www.linkedin.com/in/ajay-vishwakarma-71649129a/"
                  target="_blank"
                  data-cursor="disable"
                  className="contact-social"
                >
                  Linkedin <MdArrowOutward />
                </a>
                <a
                  href="https://t.me/ajay160380"
                  target="_blank"
                  data-cursor="disable"
                  className="contact-social"
                >
                  Telegram <MdArrowOutward />
                </a>
              </div>
            </div>
          </div>

          {/* Right: Message Form */}
          <form className="contact-form" onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="name">Your Name</label>
              <input
                type="text"
                id="name"
                placeholder="John Doe"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                required
                data-cursor="disable"
              />
            </div>
            <div className="form-group">
              <label htmlFor="email">Your Email</label>
              <input
                type="email"
                id="email"
                placeholder="john@example.com"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                required
                data-cursor="disable"
              />
            </div>
            <div className="form-group">
              <label htmlFor="message">Message</label>
              <textarea
                id="message"
                rows={5}
                placeholder="Tell me about your project..."
                value={formData.message}
                onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                required
                data-cursor="disable"
              />
            </div>
            <button type="submit" className={`form-btn ${sending ? "sending" : ""} ${sent ? "sent" : ""}`} data-cursor="disable">
              {sent ? (
                <>✓ Message Opened!</>
              ) : sending ? (
                <>Opening Mail...</>
              ) : (
                <>Send Message <MdSend style={{ marginLeft: "8px" }} /></>
              )}
            </button>
          </form>
        </div>

        {/* Footer */}
        <div className="contact-footer">
          <h2>
            Designed & Developed <br /> by <span>Ajay Vishwakarma</span>
          </h2>
          <h5>
            <MdCopyright /> 2026
          </h5>
        </div>
      </div>
    </div>
  );
};

export default Contact;
