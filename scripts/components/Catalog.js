import * as React from 'react';
import Product from './Product'



const Catalog= (props) =>{
    // sample products 
    const products = [{name:"starWars",creators :" lucas films" ,description :"jfdfjask"},{name:"starWars",creators :" lucas films" ,description :"jfdfjask"},{name:"starWars",creators :" lucas films" ,description :"jfdfjask"}]
   
    return (
       <div>
         <h1>{props.title} </h1>  
         { products.map((product, index) =>
    
    <li key={index}>
      <Product description ={product.description} creators ={product.creators}/>
    </li>
  )}
       </div>
    );
}
export default Catalog