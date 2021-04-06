import Form from 'react-bootstrap/Form'
import * as React from 'react';
import Col from 'react-bootstrap/Col'


const Search = (props) =>{
    const [searchTerm, setSearchTerm] = React.useState("");
    const handleKeyDown = (event) => {
        if (event.key === 'Enter' && searchTerm.length >0) {
            props.parentCallback(searchTerm)
            console.log("sending data")
    
        }
        
      }

    // React.useEffect(() => {
    //     props.parentCallback("comming from child");
    //     }, []);
    
    return (
    
    
    <div>
         <Form>
      <Form.Row>
      <Col md ={10}>
      <Form.Control placeholder="Title" onKeyDown = {handleKeyDown} onChange = {(e) => setSearchTerm(e.target.value)}
      />
      </Col>
      <Col>
      </Col>
      <Col>
      </Col>
  </Form.Row>
      </Form>

    </div>
    
    );
}
export default Search