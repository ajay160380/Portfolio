import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { smoother } from "../Navbar";

export function initialFX() {
  document.body.style.overflowY = "auto";
  if (smoother) {
    smoother.paused(false);
  }
  ScrollTrigger.refresh();
  document.getElementsByTagName("main")[0]?.classList.add("main-active");

  // Ensure landing container is 100% visible
  gsap.set(".landing-container", { opacity: 1, y: 0 });

  // Animate Left Hero elements with a coordinated stagger
  gsap.fromTo(
    [
      ".landing-greeting",
      ".landing-intro h1",
      ".landing-status",
      ".landing-badge",
      ".landing-pills",
      ".landing-stats-row",
    ],
    { opacity: 0, y: 30 },
    {
      opacity: 1,
      y: 0,
      duration: 0.8,
      stagger: 0.08,
      ease: "power2.out",
      delay: 0.2,
    }
  );

  // Animate Right Hero elements
  gsap.fromTo(
    [
      ".landing-info h3",
      ".landing-role-heading",
      ".landing-bio-subtitle",
      ".landing-cta-group",
    ],
    { opacity: 0, y: 30 },
    {
      opacity: 1,
      y: 0,
      duration: 0.8,
      stagger: 0.08,
      ease: "power2.out",
      delay: 0.3,
    }
  );

  // Animate Global navigation and floating elements
  gsap.fromTo(
    [".header", ".icons-section", ".nav-fade", ".landing-scroll-indicator"],
    { opacity: 0 },
    {
      opacity: 1,
      duration: 1,
      ease: "power1.inOut",
      delay: 0.1,
    }
  );

  // Start smooth role title transition (DATA ANALYST <-> AI/ML ENGINEER)
  setupRoleLoop();
}

function setupRoleLoop() {
  const role1 = document.querySelector(".landing-h2-info") as HTMLElement;
  const role2 = document.querySelector(".landing-h2-info-1") as HTMLElement;
  if (!role1 || !role2) return;

  gsap.set(role1, { opacity: 1, y: 0 });
  gsap.set(role2, { opacity: 0, y: 25 });

  const tl = gsap.timeline({ repeat: -1, repeatDelay: 2.5 });
  tl.to(role1, { opacity: 0, y: -20, duration: 0.5, ease: "power2.inOut" })
    .fromTo(
      role2,
      { opacity: 0, y: 20 },
      { opacity: 1, y: 0, duration: 0.5, ease: "power2.inOut" },
      "-=0.15"
    )
    .to(role2, { opacity: 0, y: -20, duration: 0.5, ease: "power2.inOut", delay: 2.5 })
    .fromTo(
      role1,
      { opacity: 0, y: 20 },
      { opacity: 1, y: 0, duration: 0.5, ease: "power2.inOut" },
      "-=0.15"
    );
}
