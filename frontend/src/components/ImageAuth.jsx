import React from 'react';
import bgImage from "../assets/bg-png.png"
export const ImageAuth = () => {
    return (
        <div className="bg-purple-600 bg-opacity-70 shadow-lg text-white p-4 text-center rounded-lg">
            <img src={bgImage} alt="bg" />
            <p className="text-3xl mt-4"><span className='font-medium text-lime-200'>Simplify</span> Scheduling with Us</p>
        </div>
    );
};
