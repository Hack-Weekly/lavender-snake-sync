import { LandingText } from "../components/LandingText"
import { TopNavbar } from "../components/TopNavbar"
export const LandingPage = () => {
    return(
        <div className="h-screen w-screen dark:bg-gray-900">
            <TopNavbar />
            <LandingText />
        </div>
    )
}