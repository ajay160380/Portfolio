import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          three: ["three", "three-stdlib"],
          gsap: ["gsap", "gsap/ScrollTrigger", "gsap/ScrollSmoother", "gsap/SplitText"],
          physics: ["@react-three/rapier"],
          r3f: ["@react-three/fiber", "@react-three/drei"],
        },
      },
    },
  },
});
