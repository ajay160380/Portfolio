import { lazy, Suspense } from "react";
import "./App.css";

const CharacterModel = lazy(() => import("./components/Character"));
const MainContainer = lazy(() => import("./components/MainContainer"));
const AnimatedBackground = lazy(() => import("./components/AnimatedBackground"));
import { LoadingProvider } from "./context/LoadingProvider";
import { ThemeProvider } from "./context/ThemeProvider";
import ThemeToggle from "./components/ThemeToggle";

const App = () => {
  return (
    <>
      <ThemeProvider>
        <ThemeToggle />
        <Suspense>
          <AnimatedBackground />
        </Suspense>
        <LoadingProvider>
          <Suspense>
            <MainContainer>
              <Suspense>
                <CharacterModel />
              </Suspense>
            </MainContainer>
          </Suspense>
        </LoadingProvider>
      </ThemeProvider>
    </>
  );
};

export default App;
