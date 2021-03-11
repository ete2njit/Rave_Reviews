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

                        <Card style={{ width: '28rem' }}>
                            <Card.Img variant="top" src={props.img} />
                            <Card.Body>
                                <Card.Title>Product </Card.Title>
                                <Card.Text>
                                    {props.name}
                            </Card.Text>

                            </Card.Body>
                        </Card>

                    </Col>

                    <Col>
                        <Card style={{ width: '38rem' }}>
                            <Card.Body>
                                <Card.Title>Content Creators </Card.Title>
                                <Card.Text>
                                   {props.creators}
                                </Card.Text>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Jumbotron>
                            <h1>Description</h1>
                            <p>
                                {props.description}
                                </p>

                        </Jumbotron>
                    </Col>
                </Row>

                <Row>
                    <Col>
                        <Card>
                            <h1> Reviews </h1>
                            <Card.Body>{props.reviews}</Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>

        </div>

    );
}
export default Product