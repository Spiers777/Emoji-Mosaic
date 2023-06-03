import './App.scss';
import {React, useState} from 'react'

function App() {
  const [data, setData] = useState(null)
  const [selectedImage, setSelectedImage] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    var reader = new FileReader();
    formData.append('file', selectedImage, selectedImage.name);

    await fetch('https://emoji-mosaic-backend.onrender.com/?sampleSize=10', {
      method: 'POST',
      body: formData
    }).then(response => response.json()).then(data => {
      console.log(data["output"])
      setData(data["output"])
    })
  }

  return (
    <>
      <input type='file' name='imageUpload' onChange={(e) => {setSelectedImage(e.target.files[0])}}></input>
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