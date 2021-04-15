import * as React from 'react';
import Header from './Header'
import Search from './Search'
import Socket from "../Socket";
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import CatalogGrid from "./CatalogGrid"
import CatalogSideScroll from "./CatalogSideScroll"
import { CATAGORIES } from './Catagories'

const Shows= () =>{
    const [searchTerm, setSearchTerm] = React.useState("")

    const [running, setRunning] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["TVShow"],
            "searchTerm": "running",
            "limit": 20,
        });

        return { title: ["south park", "south park", "south park"], cover: ["https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png", "https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png", "https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png"], ID: [1, 2, 3] }
    });

    const [trending, setTrending] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["TVShow"],
            "searchTerm": "trending",
            "limit": 20,
        });

        return { title: ["south park", "south park", "south park"], cover: ["https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png", "https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png", "https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png"], ID: [1, 2, 3] }
    });

    const [topRated, setTopRated] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["TVShow"],
            "searchTerm": "rating",
            "limit": 20,
        });

        return { title: ["south park", "south park", "south park"], cover: ["https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png", "https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png", "https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png"], ID: [1, 2, 3] }
    });

    const [popular, setPopular] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["TVShow"],
            "searchTerm": "popular",
            "limit": 20,
        });

        return { title: ["south park", "south park", "south park"], cover: ["https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png", "https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png", "https://upload.wikimedia.org/wikipedia/en/4/41/South_Park_main_characters.png"], ID: [1, 2, 3] }
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
                if (data["category"][0] == "running") {
                    setRunning(data)
                }
                if (data["category"][0] == "trending") {
                    setTrending(data)
                }
                if (data["category"][0] == "rating") {
                    setTopRated(data)
                }
                if (data["category"][0] == "popular") {
                    setPopular(data)
                }
            }
        });
    });

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
                    <Header />
                    <div className="catalog-header">
                        <h1>TV Shows</h1>
                        <Search parentCallback={callbackFunction} />
                    </div>
                    <div className="catalog shows">
                        <CatalogGrid data={searchData} />
                    </div>
                </div> )
        }
    return (
        <div>
            <Header />
            <div className="catalog-header">
                <h1>TV Shows</h1>
                <Search parentCallback={callbackFunction} />
            </div>
            <div className="catalog">
                <h2>Now Playing</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={running} />
                </div>
                <h2>Trending</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={trending} />
                </div>
                <h2>Top Rated</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={topRated} />
                </div>
                <h2>Popular</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={popular} />
                </div>
            </div>
        </div>
    );
}
export default Shows