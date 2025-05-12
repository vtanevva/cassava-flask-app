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
        <div>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleImageChange} />
                <button type="submit">Make a Prediction</button>
            </form>
            {preview && <img src={preview} alt="Image Preview" width="200" />}
            {message && <h2>{message}</h2>}
        </div>
    );
};

export default FileUpload;
