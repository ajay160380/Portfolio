import * as THREE from "three";
import { DRACOLoader, GLTF, GLTFLoader } from "three-stdlib";
import { setCharTimeline, setAllTimeline } from "../../utils/GsapScroll";
import { decryptFile } from "./decrypt";

const setCharacter = (
  renderer: THREE.WebGLRenderer,
  scene: THREE.Scene,
  camera: THREE.PerspectiveCamera
) => {
  const loader = new GLTFLoader();
  const dracoLoader = new DRACOLoader();
  dracoLoader.setDecoderPath("/draco/");
  loader.setDRACOLoader(dracoLoader);

  const loadCharacter = () => {
    return new Promise<GLTF | null>(async (resolve, reject) => {
      try {
        const encryptedBlob = await decryptFile(
          "/models/character.enc",
          "Character3D#@"
        );
        const blobUrl = URL.createObjectURL(new Blob([encryptedBlob]));

        let character: THREE.Object3D;
        loader.load(
          blobUrl,
          async (gltf) => {
            character = gltf.scene;
            await renderer.compileAsync(character, camera, scene);
            character.traverse((child: any) => {
              if (child.isMesh) {
                const mesh = child as THREE.Mesh;
                // child.castShadow = true;
                // child.receiveShadow = true;
                mesh.frustumCulled = true;

                // Apply white theme ONLY to body/clothes parts, preserving original hair/eyes textures
                if (mesh.material) {
                  const name = (mesh.name || "").toLowerCase();
                  
                  // Only target body, clothes, and skin
                  const isBodyPart = name.includes("body") || name.includes("hand") || 
                                     name.includes("neck") || name.includes("pant") || 
                                     name.includes("shoe") || name.includes("ear") || 
                                     name.includes("sole");

                  if (isBodyPart) {
                    const mat = mesh.material as any;
                    mat.color = new THREE.Color(0xffffff);
                    mat.metalness = 0.3;
                    mat.roughness = 0.4;
                    mat.emissive = new THREE.Color(0x000000);
                  }
                }
              }
            });
            resolve(gltf);
            setCharTimeline(character, camera);
            setAllTimeline();
            character!.getObjectByName("footR")!.position.y = 3.36;
            character!.getObjectByName("footL")!.position.y = 3.36;
            dracoLoader.dispose();
          },
          undefined,
          (error) => {
            console.error("Error loading GLTF model:", error);
            reject(error);
          }
        );
      } catch (err) {
        reject(err);
        console.error(err);
      }
    });
  };

  return { loadCharacter };
};

export default setCharacter;
