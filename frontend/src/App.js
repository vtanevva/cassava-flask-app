import React from 'react';
import FileUpload from './components/FileUpload';
import './App.css';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Upload an image for prediction</h1>
                <FileUpload />
            </header>
        </div>
    );
}

export default App;
