import React, { useState, useEffect } from 'react';
import axios from 'axios';


const Restaurants = () => {
  const [restaurants, setRestaurants] = useState([])

  const handleDelete = (id) => {
    axios.delete(`/restaurants/${id}`)
      .then(() => {
        setRestaurants((prevRestaurants) => prevRestaurants.filter(restaurant => restaurant.id !== id));
      })
      .catch((error) => {
        console.error(error);
      })
  }

  useEffect(() => {
    axios.get('/restaurants')
      .then((response) => {
        setRestaurants(response.data);
      })
      .catch((error) => {
        console.error(error)
      })
  }, [])

  return (
    <div>
      <h1>Restaurants</h1>
      {restaurants.map((restaurant) => (
        <div key={restaurant.id}>
          <h2>{restaurant.name}</h2>
          <p>{restaurant.address}</p>
          <button onClick={() => handleDelete(restaurant.id)}>Delete</button>
        </div>
      ))}
    </div>
  )
}

export default Restaurants;