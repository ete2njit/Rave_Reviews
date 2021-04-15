import * as React from 'react';
import Header from './Header'

import Jumbotron from 'react-bootstrap/Jumbotron'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Card from 'react-bootstrap/Card'

const Product = (props) => {
    return (
        <div className="product-div">
            <Container fluid >
                <Row>
                    <Col>
                       <Card className="product-card card">
                            <Card.Img className="product-card image" variant="top" src={props.img} />
                            <Card.Body className="product-card body">
                                <Card.Title className="product-card title">{props.name}</Card.Title>
                                <Card.Text className="product-card rating">
                                    [rating here]
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
        </div>
    );
}
export default Product