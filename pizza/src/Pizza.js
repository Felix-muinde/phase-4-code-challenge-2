import React, { useState, useEffect } from 'react';
import axios from 'axios';


const Pizza = () => {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    axios.get('/pizzas')
      .then((response) => {
        setPizzas(response.data)
      })
      .catch((error) => {
        console.error(error)
      })
  }, [])

  return (
    <div>
      <h1>Pizzas</h1>
      {pizzas.map((pizza) => (
        <div key={pizza.id}>
          <h2>{pizza.name}</h2>
          <p>{pizza.ingredients}</p>
        </div>
      ))}
    </div>
  )
}

export default Pizza;