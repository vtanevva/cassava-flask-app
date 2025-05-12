// App.js
import React from 'react';
import FileUpload from './components/FileUpload';

function App() {
  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100 p-4 sm:p-8">
      <header className="text-center p-6 bg-blue-500 text-white rounded-lg shadow-md sm:p-8 lg:p-10 xl:p-12">
        <h1 className="text-2xl sm:text-3xl lg:text-4xl font-semibold">Upload an image for prediction</h1>
        <FileUpload />
      </header>
    </div>
  );
}

export default App;
