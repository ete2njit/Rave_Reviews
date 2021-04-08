import * as React from 'react';
import {Navbar,Nav,} from 'react-bootstrap';


const Header= () =>{
    return (
      <Navbar bg="primary" variant="dark">
      <Navbar.Brand href="#home">Rave Reviews </Navbar.Brand>
      <Nav className="mr-auto">
        <Nav.Link href="#/Home">Home</Nav.Link>
        <Nav.Link href="#/Movies">Movies</Nav.Link>
        <Nav.Link href="#/TVShows">TV Shows</Nav.Link>
        <Nav.Link href="#/Books">Books</Nav.Link>
        <Nav.Link href="#/Games">Games</Nav.Link>
      </Nav>
    </Navbar>
        
    );
}
export default Header
