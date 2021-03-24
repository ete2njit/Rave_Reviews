import * as React from 'react';
import Product from './Product'



const Catalog= (props) =>{
    // sample products 
    const products = [{name:"starWars",creators :" lucas films" ,description :"jfdfjask"},{name:"starWars",creators :" lucas films" ,description :"jfdfjask"},{name:"starWars",creators :" lucas films" ,description :"jfdfjask"}]
   
    return (
       <div>
         <h1>{props.title} </h1>  
         { props.data["ID"].map((id, index) =>
    <li key={id}>
      <Product  name = {props.data["title"][index]} img = {props.data["cover"][index]}/>
    </li>
  )}
       </div>
    );
}
export default Catalog