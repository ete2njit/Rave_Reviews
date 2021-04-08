
import * as React from 'react';
import Header from './Header'
import Dropdown from 'react-bootstrap/Dropdown'
import DropdownButton from 'react-bootstrap/DropdownButton'
import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import Card from 'react-bootstrap/Card'
import Socket from "../Socket";
import Catalog from "./Catalog"
import { Container } from 'react-bootstrap';
import {CATAGORIES} from './Catagories'


const Home = () => {
  const [searchTerm, setSearchTerm] = React.useState("");
  const [searchCategory, setSearchCategory] = React.useState("Category");
  const [searchData , setSearchData] = React.useState({})
  const upcomingMovies = {title:["star wars","star wars", "star wars"] ,cover:["https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg","https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg","https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"], ID:[1,2,3]}
  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
    

      if ( searchCategory != "Category" && searchTerm != ""){
        event.preventDefault();
      
      

        Socket.emit("search request", {
            category: searchCategory,
            searchTerm: searchTerm,
        }); 
      }
      else if (searchCategory == "Category"){
        alert("Please enter category ")
      }
      else{
        alert("Please enter title")
      }
    }
  }

  React.useEffect(() => {
    Socket.on("connected", (data) => {
     
        });
    }, []);

    React.useEffect(() => {
      Socket.on("search response", (data) => {
    
          setSearchData(data)
  
          });
      }, []);
 if (Object.keys(searchData).length !== 0 ){
   return ( <div><Header />
    <Form>
    <Form.Row>
    <Col md ={10}>
    <Form.Control placeholder="Title" onKeyDown = {handleKeyDown} onChange = {(e) => setSearchTerm(e.target.value)}
    />
    </Col>
    <Col>
    <DropdownButton id="dropdown-basic-button" title={searchCategory}>
      <Dropdown.Item   onClick={() => setSearchCategory(CATAGORIES["Movie"])}> Movies</Dropdown.Item>
      <Dropdown.Item onClick={() => setSearchCategory(CATAGORIES["Book"])}>Books</Dropdown.Item>
      <Dropdown.Item onClick={() => setSearchCategory(CATAGORIES["TVShow"])}>TVShows</Dropdown.Item>
      <Dropdown.Item onClick={() => setSearchCategory(CATAGORIES["Game"])}>game</Dropdown.Item>
    </DropdownButton>
    </Col>
    <Col>
    </Col>
</Form.Row>
    </Form> 
    <Catalog data ={searchData}/>
    </div>)
 }

  return (  <div>
    <Header />
      <Form>
      <Form.Row>
      <Col md ={10}>
      <Form.Control placeholder="Title" onKeyDown = {handleKeyDown} onChange = {(e) => setSearchTerm(e.target.value)}
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

      <Card>
  <Card.Body>Upcoming Movies</Card.Body>
</Card>
      <Container>
  <Row>
    <Col>  <Catalog data={upcomingMovies}/>  </Col>
    <Col>  <Catalog data={upcomingMovies}/>  </Col>
  </Row>
</Container>
    
    </div>
  ); 
  }

export default Home
