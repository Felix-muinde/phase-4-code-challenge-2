import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from './Home';
import Restaurants from './Restaurants';
import Pizza from './Pizza';
import RestaurantPizza from './RestaurantPizza';


function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/restaurants" element={<Restaurants />} />
        <Route path="/pizza" element={<Pizza />} />
        <Route path="/restaurant-pizza" element={<RestaurantPizza />} />
      </Routes>
    </div>
  )
}

export default App;
