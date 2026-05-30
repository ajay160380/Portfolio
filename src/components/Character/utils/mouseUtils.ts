import * as THREE from "three";

export const handleMouseMove = (
  event: MouseEvent,
  setMousePosition: (x: number, y: number) => void
) => {
  const mouseX = (event.clientX / window.innerWidth) * 2 - 1;
  const mouseY = -(event.clientY / window.innerHeight) * 2 + 1;
  setMousePosition(mouseX, mouseY);
};

export const handleTouchMove = (
  event: TouchEvent,
  setMousePosition: (x: number, y: number) => void
) => {
  const mouseX = (event.touches[0].clientX / window.innerWidth) * 2 - 1;
  const mouseY = -(event.touches[0].clientY / window.innerHeight) * 2 + 1;
  setMousePosition(mouseX, mouseY);
};

export const handleTouchEnd = (
  setMousePosition: (
    x: number,
    y: number,
    interpolationX: number,
    interpolationY: number
  ) => void
) => {
  setTimeout(() => {
    setMousePosition(0, 0, 0.03, 0.03);
    setTimeout(() => {
      setMousePosition(0, 0, 0.1, 0.2);
    }, 1000);
  }, 2000);
};

let currentHeadRotationX: number | null = null;
let currentHeadRotationY: number | null = null;

export const resetHeadRotation = () => {
  currentHeadRotationX = null;
  currentHeadRotationY = null;
};

export const handleHeadRotation = (
  headBone: THREE.Object3D,
  mouseX: number,
  mouseY: number,
  interpolationX: number,
  interpolationY: number,
  lerp: (x: number, y: number, t: number) => number
) => {
  if (!headBone) return;
  
  if (currentHeadRotationX === null || currentHeadRotationY === null) {
    currentHeadRotationX = headBone.rotation.x;
    currentHeadRotationY = headBone.rotation.y;
  }

  if (window.scrollY < 200) {
    const maxRotation = Math.PI / 6;
    currentHeadRotationY = lerp(
      currentHeadRotationY,
      mouseX * maxRotation,
      interpolationY
    );
    let minRotationX = -0.3;
    let maxRotationX = 0.4;
    let targetRotationX = 0;
    if (mouseY > minRotationX) {
      if (mouseY < maxRotationX) {
        targetRotationX = -mouseY - 0.5 * maxRotation;
      } else {
        targetRotationX = -maxRotation - 0.5 * maxRotation;
      }
    } else {
      targetRotationX = -minRotationX - 0.5 * maxRotation;
    }
    currentHeadRotationX = lerp(
      currentHeadRotationX,
      targetRotationX,
      interpolationX
    );
  } else {
    if (window.innerWidth > 1024) {
      currentHeadRotationX = lerp(currentHeadRotationX, -0.4, 0.03);
      currentHeadRotationY = lerp(currentHeadRotationY, -0.3, 0.03);
    }
  }

  // Apply to bone, completely overriding the mixer for these axes
  headBone.rotation.x = currentHeadRotationX;
  headBone.rotation.y = currentHeadRotationY;
};
