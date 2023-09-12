import React from 'react';
import { Login } from '../components/Login';
import { ImageAuth } from '../components/ImageAuth';

export const LoginPage = () => {
    return (
        <div className="flex h-screen dark:bg-slate-900">
            <div className="w-1/2 bg-gradient-to-r from-purple-500 to-purple-700 flex justify-center items-center">
                <ImageAuth />
            </div>
            <div className="w-1/2 flex flex-col items-center justify-center">
                <h1 className='text-4xl font-semibold dark:text-white'>Login</h1>
                <Login />
            </div>
        </div>
    );
};
