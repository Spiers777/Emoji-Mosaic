import './App.scss';
import {React, useState} from 'react'

function App() {
  const [data, setData] = useState(null)
  const [selectedImage, setSelectedImage] = useState(null);
  const [sampleSize, setSampleSize] = useState(25);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', selectedImage, selectedImage?.name);

    await fetch(`https://emoji-mosaic-backend.onrender.com/?sampleSize=${sampleSize}`, {
      method: 'POST',
      body: formData
    }).then(response => response.json()).then(data => {
      console.log(data["output"])
      setData(data["output"])
    })
  }

  return (
    <>
      <input type='file' accept="image/*" name='imageUpload' onChange={(e) => {setSelectedImage(e.target.files[0])}}></input>
      <input type="range" min="1" max="50" defaultvalue="25" onChange={(e) => {setSampleSize(e.target.value)}}></input>{sampleSize}
      <button onClick={handleUpload}>Generate</button>
      <div className='output'>
        {data ? data.map((row) => 
          <p>{row}</p>
        ) : "Loading"}
      </div>
    </>
  )
}

export default App