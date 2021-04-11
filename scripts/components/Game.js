import * as React from 'react';
import Header from './Header'
import Search from './Search'
import "./App.css"
import Socket from "../Socket";
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import Catalog from "./Catalog"
import {CATAGORIES} from './Catagories'
import Result from "./Result"
const Shows= () =>{
    const[searchTerm ,setSearchTerm] = React.useState("")
    const upcomingMovies = {title:["call of duty ","call of duty", "call of duty"] ,cover:["https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg","https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg","https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg"], ID:[1,2,3]}
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
                category: CATAGORIES["Game"],
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