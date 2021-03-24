
import * as React from 'react';
import Header from './Header'
import Product from './Product'
import Dropdown from 'react-bootstrap/Dropdown'
import DropdownButton from 'react-bootstrap/DropdownButton'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Col from 'react-bootstrap/Col'
import Socket from "../Socket";
import Catalog from "./Catalog"

const Home = () => {
  const [searchTerm, setSearchTerm] = React.useState("");
  const [searchCategory, setSearchCategory] = React.useState("Category");
  
  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      console.log('do validate')

      if ( searchCategory != "Category"){
        e.preventDefault();

        Socket.emit("search request", {
            category: searchCategory,
            searchTerm: searchTerm,
        }); 
      }
      else{
        alert("Please enter category ")
      }
    }
  }
 
  return (
    <div>
      <Header />
      <Form>
      <Form.Row>
      <Col md ={10}>
      <Form.Control placeholder="Title" onKeyDown = {handleKeyDown}
      />
      </Col>
      <Col>
      <DropdownButton id="dropdown-basic-button" title={searchCategory}>
        <Dropdown.Item   onClick={() => setSearchCategory("movie")}> Movies</Dropdown.Item>
        <Dropdown.Item onClick={() => setSearchCategory("book")}>Books</Dropdown.Item>
        <Dropdown.Item onClick={() => setSearchCategory("show")}>TVShows</Dropdown.Item>
        <Dropdown.Item onClick={() => setSearchCategory("game")}>game</Dropdown.Item>
      </DropdownButton>
      </Col>
      <Col>
      
      </Col>
     
     
  </Form.Row>
      </Form>
      
    </div>
  ); 
  }

export default Home
