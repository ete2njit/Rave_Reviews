import * as React from 'react';
import Product from './Product';
import ListGroup from 'react-bootstrap/ListGroup'
import Image from 'react-bootstrap/Image'


const Result= (props) =>{

    function selected (){
        console.log("clicked ")
    }
    return (
       <div>
         <h1>{props.title} </h1>  
         { props.data["ID"].map((id, index) =>
    <ol key={id}>
      <ListGroup> <ListGroup.Item  action onClick={selected}>  <Image src={props.data["cover"][index]} width={171}
    height={180}roundedCircle />{props.data["title"][index]} </ListGroup.Item></ListGroup>
    </ol>
  )}
       </div>
    );
}
export default Result