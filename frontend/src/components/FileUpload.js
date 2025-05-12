// FileUpload.js
import React, { useState } from 'react';

const FileUpload = () => {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [message, setMessage] = useState('');

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    setImage(file);
    setPreview(URL.createObjectURL(file));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('image', image);

    const response = await fetch('http://localhost:5000/api/predict', {
      method: 'POST',
      body: formData,
    });

    const result = await response.json();
    setMessage(result.message);
  };

  return (
    <div className="flex flex-col items-center space-y-4 sm:flex-row sm:space-x-4 sm:space-y-0">
      <form onSubmit={handleSubmit} className="flex flex-col space-y-4 sm:w-1/2 lg:w-1/3">
        <input type="file" onChange={handleImageChange} className="p-2 border rounded" />
        <button type="submit" className="p-2 bg-blue-500 text-white rounded">Make a Prediction</button>
      </form>
      {preview && <img src={preview} alt="Image Preview" width="200" className="rounded shadow-md sm:w-1/2 lg:w-1/3" />}
      {message && <h2 className="mt-4 text-lg">{message}</h2>}
    </div>
  );
};

export default FileUpload;
