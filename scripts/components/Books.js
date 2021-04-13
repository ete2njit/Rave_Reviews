import * as React from 'react';
import Header from './Header'
import Search from './Search'
import Socket from "../Socket";
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import CatalogGrid from "./CatalogGrid"
import CatalogSideScroll from "./CatalogSideScroll"
import { CATAGORIES } from './Catagories'

const Books= () =>{
    const [searchTerm, setSearchTerm] = React.useState("");

    const [hardcoverFiction, setHardcoverFiction] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Book"],
            "searchTerm": "hardcover-fiction",
        });

        return { title: ["harry potter", "harry potter", "harry potter"], cover: ["https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg", "https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg", "https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg"], ID: [1, 2, 3] }
    });

    const [hardcoverNonFiction, setHardcoverNonFiction] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Book"],
            "searchTerm": "hardcover-nonfiction",
        });

        return { title: ["harry potter", "harry potter", "harry potter"], cover: ["https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg", "https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg", "https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg"], ID: [1, 2, 3] }
    });

    const [youngAdult, setYoungAdult] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Book"],
            "searchTerm": "young-adult-hardcover",
        });

        return { title: ["harry potter", "harry potter", "harry potter"], cover: ["https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg", "https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg", "https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg"], ID: [1, 2, 3] }
    });

    const [science, setScience] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Book"],
            "searchTerm": "science",
        });

        return { title: ["harry potter", "harry potter", "harry potter"], cover: ["https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg", "https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg", "https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg"], ID: [1, 2, 3] }
    });

    const [advice, setAdvice] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Book"],
            "searchTerm": "hardcover-advice",
        });

        return { title: ["harry potter", "harry potter", "harry potter"], cover: ["https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg", "https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg", "https://m.media-amazon.com/images/I/51YuFod+3FL._SL500_.jpg"], ID: [1, 2, 3] }
    });

    const [searchData, setSearchData] = React.useState({});
    const callbackFunction  = (data) =>{
      
        setSearchTerm(data)
      console.log("reciving serch term from child") 
      console.log(searchTerm)
    }

    React.useEffect(() => {
        Socket.on("category response", (data) => {
            console.log("data recieved")
            console.log(data)
            if (data["category"].length > 0) {
                if (data["category"][0] == "hardcover-fiction") {
                    setHardcoverFiction(data)
                }
                if (data["category"][0] == "hardcover-nonfiction") {
                    setHardcoverNonFiction(data)
                }
                if (data["category"][0] == "hardcover-advice") {
                    setAdvice(data)
                }
                if (data["category"][0] == "young-adult-hardcover") {
                    setYoungAdult(data)
                }
                if (data["category"][0] == "science") {
                    setScience(data)
                }
            }
        });
    });

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
            <Header />
            <div className="catalog-header">
                <h1>Books</h1>
                <Search parentCallback={callbackFunction} />
            </div>
            <div className="catalog books">
                <CatalogGrid data={searchData} />
            </div>
        </div> )
    }
    return (
        <div>
            <Header />
            <div className="catalog-header">
                <h1>Books</h1>
                <Search parentCallback={callbackFunction} />
            </div>
            <div className="catalog">
                <h2>Fiction</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={hardcoverFiction} />
                </div>
                <h2>Non-Fiction</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={hardcoverNonFiction} />
                </div>
                <h2>Young Adult</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={youngAdult} />
                </div>
                <h2>Science</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={science} />
                </div>
                <h2>Advice</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={advice} />
                </div>
            </div>
        </div>
    );
}
export default Books
