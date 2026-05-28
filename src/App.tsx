import { lazy, Suspense } from "react";
import "./App.css";

const CharacterModel = lazy(() => import("./components/Character"));
const MainContainer = lazy(() => import("./components/MainContainer"));
import { LoadingProvider } from "./context/LoadingProvider";
import { ThemeProvider } from "./context/ThemeProvider";
import ThemeToggle from "./components/ThemeToggle";

const App = () => {
  return (
    <>
      <ThemeProvider>
        <ThemeToggle />
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
