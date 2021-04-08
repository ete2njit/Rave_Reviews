import * as React from 'react';
import Header from './Header'
import Search from './Search'
import "./App.css"
import Socket from "../Socket";
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import Catalog from "./Catalog"
import {CATAGORIES} from './Catagories'
const Books= () =>{
    const[searchTerm ,setSearchTerm] = React.useState("")
    const upcomingMovies = {title:["harry potter","harry potter", "harry potter"] ,cover:["https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg","https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg","https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg"], ID:[1,2,3]}
    const [searchData , setSearchData] = React.useState({})
    const callbackFunction  = (data) =>{
      
        setSearchTerm(data)
      console.log("reciving serch term from child") 
      console.log(searchTerm)
        
      }

      React.useEffect(() => {
          if (searchTerm.length >0){
            Socket.emit("search request", {
                category: CATAGORIES["Book"],
                searchTerm: searchTerm,
            }); 
            console.log("sending data to backedn")
          }
       
        }, [searchTerm]);

      React.useEffect(() => {
        Socket.on("connected", (data) => {
            console.log("connected")
         
            });
        }, []);

        React.useEffect(() => {
            Socket.on("search response", (data) => {
                console.log("data recieved")
                console.log(data)
          
                setSearchData(data)
                console.log(searchData)
        
                });
            }, []);


            if(Object.keys(searchData).length !=0){
                return (

                
                <div>
                    <Header/>
                    <Search parentCallback = {callbackFunction}/>
                    <Catalog data ={searchData}/>
                </div> )
            }
    return (
        <div >
        <Header/>
       
         <Search parentCallback = {callbackFunction} />
         <Row>
    <Col>  <Catalog data={upcomingMovies}/>  </Col>
    <Col>  <Catalog data={upcomingMovies}/>  </Col>
  </Row>
        </div>
       
    );
}
export default Books
