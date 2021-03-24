import * as React from 'react';
import Header from './Header'

import Jumbotron from 'react-bootstrap/Jumbotron'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Card from 'react-bootstrap/Card'

const Product = (props) => {
    return (
        <div>
            <Container fluid >
                <Row>
                    <Col>
                       <Card style={{ width: '25rem' }}>
                            <Card.Img variant="top" src={props.img} />
                            <Card.Body>
                                <Card.Title>Title </Card.Title>
                                <Card.Text>
                                    {props.name}
                            </Card.Text>
                            <Card.Text>
                                   {props.creators}
                                </Card.Text>
                                <Card.Text>
                                Description 
                                {props.description}
                                </Card.Text>
                            
                                <Card.Text>
                                   Reviews
                                    {props.reviews}
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>

                </Row>
                <Row>
                   
                </Row>

            </Container>

        </div>

    );
}
export default Product