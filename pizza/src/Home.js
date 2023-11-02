import React from 'react';
import { useNavigate } from 'react-router-dom';


function Home() {
  const navigate = useNavigate()

  return (
    <div>
      <h1>welcome to my pizza inn!!</h1>
      <p>Get your yummy pizza with us!!</p>
      <button onClick={() => navigate('/restaurants')}>Restaurants</button>
      <button onClick={() => navigate('/pizza')}>Pizzas</button>
      <button onClick={() => navigate('/restaurant-pizza')}>Restaurant Pizzas</button>
    </div>
  )
}

export default Home;