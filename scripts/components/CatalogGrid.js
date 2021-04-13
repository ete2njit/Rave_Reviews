import * as React from 'react';
import Product from './Product'



const CatalogGrid = (props) =>{
    // sample products 
    return (
       <div>
            <h1>{props.title} </h1>  
            <div className="catalog-grid">
                {props.data["ID"].map((id, index) =>
                    <div className="catalog-item" key={id}>
                      <Product  name = {props.data["title"][index]} img = {props.data["cover"][index]}/>
                    </div>
                )}
            </div>
       </div>
    );
}
export default CatalogGrid