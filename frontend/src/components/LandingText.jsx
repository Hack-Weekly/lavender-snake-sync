import { Button, Card } from "flowbite-react";
import landingImage from '../assets/landing-image.png'; 

export const LandingText = () => {
  return (
    <div className="flex flex-row justify-center items-center w-screen h-screen gap-20">
      <div className="flex flex-col">
        <h2 className="text-5xl font-semibold dark:text-white">Unite Your Team</h2>
        <h1 className="text-5xl font-semibold text-purple-800 dark:text-purple-600">Anytime</h1>
        <h2 className="text-5xl font-semibold text-lime-500 dark:text-lime-400">Anywhere</h2>
        <h3 className="text-xl opacity-75 dark:text-white mt-4">Simplify Team Scheduling Across Timezones.</h3>
        <div className="flex flex-col items-center mt-4"> {/* Wrap button and image in a flex container */}
          <Button size="sm" color="dark" pill>Try for free</Button>
        </div>
      </div>
      <div className="w-2/4 bg-lime p-10 rounded-3xl">
        <div className="relative">
          <div className="absolute top-2 left-2 w-full h-full bg-lime-500 opacity-80 rounded-3xl transform -rotate-2 dark:opacity-95"></div>
          <div className="relative z-10">
            <img src={landingImage} alt="Landing" className="w-full h-auto" />
          </div>
        </div>
      </div>
    </div>
  );
};
