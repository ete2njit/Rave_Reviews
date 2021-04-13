import * as React from 'react';
import Product from './Product'



const CatalogGrid = (props) =>{
    // sample products 
    return (
       <div>
            <h1>{props.title} </h1>  
            <ul className="product-list">
                {props.data["ID"].map((id, index) =>
                    <li className="catalog-item" key={id}>
                      <Product  name = {props.data["title"][index]} img = {props.data["cover"][index]}/>
                    </li>
                )}
            </ul>
       </div>
    );
}
export default CatalogGrid