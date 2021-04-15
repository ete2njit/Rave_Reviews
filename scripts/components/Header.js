import * as React from 'react';
import {Navbar,Nav,} from 'react-bootstrap';


const Header= () =>{
    return (
      <Navbar variant="dark">
      <Navbar.Brand href="#home">
                <img className="logo" src="static/logo.png" alt="logo" />
      </Navbar.Brand>
      <Nav className="mr-auto">
        <Nav.Link href="#/Movies">Movies</Nav.Link>
        <Nav.Link href="#/TVShows">TV Shows</Nav.Link>
        <Nav.Link href="#/Books">Books</Nav.Link>
        <Nav.Link href="#/Games">Games</Nav.Link>
      </Nav>
    </Navbar>
        
    );
}
export default Header
