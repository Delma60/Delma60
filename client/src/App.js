import './App.css';
import {useEffect, useState} from 'react'
import Home from './pages/Home';
// import fetch 

// import Router
function App() {
  const [Data, setData] = useState([])
  useEffect(() => {
    // fetch("http://127.0.0.1:5000/home")
    // .then((res) => res.json()
    // )
    // .then(data => {
    //   setData(data.message)
    //   console.log(data.message)
    // }
    
    // )
    // .catch((er) => console.log(er))
  }, [])
  return (
    <div className="">
      <Home />
      {
        // Data.map(item => (
        //   <div>
        //     {item}
        //   </div>
        // ))
      }
    </div>
  );
}

export default App;
