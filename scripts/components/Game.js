import * as React from 'react';
import Header from './Header'
import Search from './Search'
import Socket from "../Socket";
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import CatalogGrid from "./CatalogGrid"
import CatalogSideScroll from "./CatalogSideScroll"
import Catalog from "./Catalog"
import {CATAGORIES} from './Catagories'
const Shows= () =>{
    const [searchTerm, setSearchTerm] = React.useState("")

    const [topRated, setTopRated] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Game"],
            "searchTerm": "rating",
            "limit": 10,
        });

        return { title: ["call of duty ", "call of duty", "call of duty"], cover: ["https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg", "https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg", "https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg"], ID: [1, 2, 3] }
    });

    const [newReleases, setNewReleases] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Game"],
            "searchTerm": "new",
            "limit": 10,
        });

        return { title: ["call of duty ", "call of duty", "call of duty"], cover: ["https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg", "https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg", "https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg"], ID: [1, 2, 3] }
    });

    const [mostAnticipated, setMostAnticipated] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Game"],
            "searchTerm": "anticipation",
            "limit": 10,
        });

        return { title: ["call of duty ", "call of duty", "call of duty"], cover: ["https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg", "https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg", "https://bnetcmsus-a.akamaihd.net/cms/blog_header/6a/6ADE9XLH1RZS1602609187570.jpg"], ID: [1, 2, 3] }
    });



    const [searchData , setSearchData] = React.useState({})
    const callbackFunction  = (data) =>{
      
        setSearchTerm(data)
   
      console.log(searchTerm)
        
    }

    React.useEffect(() => {
        Socket.on("category response", (data) => {
            console.log("data recieved")
            console.log(data)
            if (data["category"].length > 0) {
                if (data["category"][0] == "rating") {
                    setTopRated(data)
                }
                if (data["category"][0] == "anticipation") {
                    setMostAnticipated(data)
                }
                if (data["category"][0] == "new") {
                    setNewReleases(data)
                }
            }
        });
    });

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
                <Header />
                <div className="catalog-header">
                    <h1>Movies</h1>
                    <Search parentCallback={callbackFunction} />
                </div>
                <div className="catalog games">
                    <CatalogGrid data={searchData} />
                </div>
            </div>)
    }
    return (
        <div>
            <Header />
            <div className="catalog-header">
                <h1>Games</h1>
                <Search parentCallback={callbackFunction} />
            </div>
            <div className="catalog">
                <h2>Top Rated</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={topRated} />
                </div>
                <h2>New Releases</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={newReleases} />
                </div>
                <h2>Most Anticipated</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={mostAnticipated} />
                </div>
            </div>
        </div>
    );
}
export default Shows
