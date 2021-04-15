import Form from 'react-bootstrap/Form'
import * as React from 'react';
import Col from 'react-bootstrap/Col'
import {CATAGORIES} from './Catagories'


const Search = (props) =>{
    const [searchTerm, setSearchTerm] = React.useState("");
    const handleKeyDown = (event) => {
        if (event.key === 'Enter' && searchTerm.length >0) {
            event.preventDefault()
            props.parentCallback(searchTerm)
            console.log("sending data")
            
    
        }
        
      }

   
    return (
    
    
    <div className="search-div">
      <Form className="search-form">
        <Form.Row>
          <Form.Control className="search-bar" placeholder="Title" onKeyDown = {handleKeyDown} onChange = {(e) => setSearchTerm(e.target.value)}/>
        </Form.Row>
      </Form>
    </div>
    
    );
}
export default Search