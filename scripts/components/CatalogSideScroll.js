import * as React from 'react';
import Product from './Product'
import HorizontalScroll from 'react-scroll-horizontal'



const CatalogSideScroll= (props) => {
    // sample products 
    return (
        <div className= "horizontal-scroll">
            <h1>{props.title} </h1>  
            <HorizontalScroll className="product-list">
                {props.data["ID"].map((id, index) =>
                    <div className="catalog-item" key={id}>
                      <Product  name = {props.data["title"][index]} img = {props.data["cover"][index]}/>
                    </div>
                )}
            </HorizontalScroll>
       </div>
    );
}
export default CatalogSideScroll