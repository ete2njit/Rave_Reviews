import * as React from 'react';
import Header from './Header'
import Search from './Search'
import Socket from "../Socket";
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import CatalogGrid from "./CatalogGrid"
import CatalogSideScroll from "./CatalogSideScroll"
import {CATAGORIES} from './Catagories'

const Movies= () =>{
    const [searchTerm, setSearchTerm] = React.useState("")

    const [nowPlaying, setNowPlaying] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Movie"],
            "searchTerm": "now playing",
            "limit": 20,
        });

        return { title: ["star wars", "star wars", "star wars"], cover: ["https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg", "https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg", "https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"], ID: [1, 2, 3] }
    });

    const [trending, setTrending] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Movie"],
            "searchTerm": "trending",
            "limit": 20,
        });

        return { title: ["star wars", "star wars", "star wars"], cover: ["https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg", "https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg", "https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"], ID: [1, 2, 3] }
    });

    const [topRated, setTopRated] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Movie"],
            "searchTerm": "rating",
            "limit": 20,
        });

        return { title: ["star wars", "star wars", "star wars"], cover: ["https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg", "https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg", "https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"], ID: [1, 2, 3] }
    });

    const [upcoming, setUpcoming] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Movie"],
            "searchTerm": "upcoming",
            "limit": 20,
        });

        return { title: ["star wars", "star wars", "star wars"], cover: ["https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg", "https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg", "https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"], ID: [1, 2, 3] }
    });

    const [popular, setPopular] = React.useState(() => {
        Socket.emit("category request", {
            "category": CATAGORIES["Movie"],
            "searchTerm": "popular",
            "limit": 20,
        });

        return { title: ["star wars", "star wars", "star wars"], cover: ["https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg", "https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg", "https://www.themoviedb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"], ID: [1, 2, 3] }
    });

    const [searchData, setSearchData] = React.useState({})
    const callbackFunction = (data) => {

        setSearchTerm(data)
        console.log("reciving serch term from child")
        console.log(searchTerm)

    }

    React.useEffect(() => {
        Socket.on("category response", (data) => {
            console.log("data recieved")
            console.log(data)
            if (data["category"].length > 0) {
                if (data["category"][0] == "now playing") {
                    setNowPlaying(data)
                }
                if (data["category"][0] == "trending") {
                    setTrending(data)
                }
                if (data["category"][0] == "rating") {
                    setTopRated(data)
                }
                if (data["category"][0] == "upcoming") {
                    setUpcoming(data)
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
                category: CATAGORIES["Movie"],
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
                        <h1>Movies</h1>
                        <Search parentCallback={callbackFunction} />
                    </div>
                    <div className="catalog movies">
                            <CatalogGrid data={searchData} />
                    </div>
                </div> )
            }
    return (
        <div>
            <Header />
            <div className="catalog-header">  
                <h1>Movies</h1>
                <Search parentCallback={callbackFunction} />
            </div>
            <div className="catalog">
                <h2>Now Playing</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={nowPlaying} />
                </div>
                <h2>Trending</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={trending} />
                </div>
                <h2>Top Rated</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={topRated} />
                </div>
                <h2>Upcoming</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={upcoming} />
                </div>
                <h2>Popular</h2>
                <div className="catalog-row">
                    <CatalogSideScroll data={popular} />
                </div>
            </div>
        </div>
    );
}
export default Movies