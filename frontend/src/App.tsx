import {Button} from './components/Button';

import { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000')
      .then((res) => res.json())
      .then((data) => setMessage(data.message));
  }, []);

  const handleClick = () => {
    const randomNumber = Math.floor(Math.random() * 100);
    alert(`Random number: ${randomNumber}`);
  }
  return (
    <div>
      <h1>{message}</h1>
      <Button onClick = {handleClick} label = "Generate random Number" />
      </div>
  );
}

export default App;
