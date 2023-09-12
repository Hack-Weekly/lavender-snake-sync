import React from 'react';
import { ImageAuth } from '../components/ImageAuth';
import { Signup } from '../components/Signup';

export const SignupPage = () => {
    return (
        <div className="flex h-screen dark:bg-slate-900">
            <div className="w-1/2 bg-gradient-to-r from-purple-500 to-purple-700 flex justify-center items-center">
                <ImageAuth />
            </div>
            <div className="w-1/2 flex flex-col items-center justify-center">
                <h1 className='text-4xl font-semibold dark:text-white'>Sign up</h1>
                <Signup />
            </div>
        </div>
    );
};
