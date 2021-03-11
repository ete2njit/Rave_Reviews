    
import * as React from 'react';
import Header from './Header'
import Product from './Product'

const Home= () =>{
   
    return (
     <div>
       <Header/>
      <Product img = "https://specials-images.forbesimg.com/imageserve/5f3e8d3a5a5822f2d9ab9638/960x0.jpg?fit=scale" reviews = "this is a sample review" description = " call of duty is a first person shooter game ...."  creators = "activision"/>
     </div>
    );
}
export default Home
