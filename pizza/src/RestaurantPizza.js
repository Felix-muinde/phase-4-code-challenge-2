import React, { useState } from 'react';
import axios from 'axios';


const RestaurantPizza = () => {
  const [formData, setFormData] = useState({
    price: '',
    pizza_id: '',
    restaurant_id: '',
  })

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('/restaurant_pizzas', formData)
      .then((response) => {
        console.log('RestaurantPizza created:', response.data);
        window.alert('welcome to our Restaurant Pizza!!')

        setFormData({
          price: '',
          pizza_id: '',
          restaurant_id: '',
        })
      })
      .catch((error) => {
        console.error('Error creating RestaurantPizza:', error)
        window.alert('Try again later!!')
      })
  }

  return (
    <div>
      <h1>Add a Restaurant Pizza</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Price:</label>
          <input
            type="number"
            name="price"
            value={formData.price}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Pizza ID:</label>
          <input
            type="number"
            name="pizza_id"
            value={formData.pizza_id}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Restaurant ID:</label>
          <input
            type="number"
            name="restaurant_id"
            value={formData.restaurant_id}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Create RestaurantPizza</button>
      </form>
    </div>
  )
}

export default RestaurantPizza;