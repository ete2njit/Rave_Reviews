import * as React from 'react';
import Header from './Header'
import Search from './Search'



const Movies= (props) =>{
    const callbackFunction  = (data) =>{
        console.log("calling back child data ")
        console.log( data)
      }
    return (
        <div>

<Header/>
       <Search parentCallback = {callbackFunction} />
        </div>
       
    );
}
export default Movies
