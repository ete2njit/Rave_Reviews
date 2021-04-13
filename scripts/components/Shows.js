import * as React from 'react';
import Header from './Header'
import Search from './Search'
import "./App.css"
import Socket from "../Socket";
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import Catalog from "./Catalog"
import Result from "./Result"
import {CATAGORIES} from './Catagories'
const Shows= () =>{
    const[searchTerm ,setSearchTerm] = React.useState("")
    const upcomingMovies = {title:["south park","south park", "south park"] ,cover:["https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png","https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png","https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png"], ID:[1,2,3]}
    const [searchData , setSearchData] = React.useState({})
    const callbackFunction  = (data) =>{
      
        setSearchTerm(data)
   
      console.log(searchTerm)
        
      }

        // TODO implement call back
        const handleResults = (data) =>{
        
        }

      React.useEffect(() => {
          if (searchTerm.length >0){
            Socket.emit("search request", {
                category: CATAGORIES["TVShow"],
                searchTerm: searchTerm,
            }); 
         
          }
       
        }, [searchTerm]);

     

        React.useEffect(() => {
            Socket.on("search response", (data) => {
              
                setSearchData(data)
          
        
                });
            }, []);


            if(Object.keys(searchData).length !=0){
                return (

                
                <div>
                    <Header/>
                    <Search parentCallback = {callbackFunction}/>
                    <Result  productCallBack={ handleResults} data = {searchData}/>
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
export default Shows