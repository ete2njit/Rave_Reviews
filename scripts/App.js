import React from "react"
import Home from "./components/Home"
import Socket from "./Socket";
import Movies from "./components/Movies"
import Books from "./components/Books"
import Error from "./components/Error"
import Shows from "./components/Shows"
import Game from "./components/Game"
import {Switch , Route} from "react-router-dom"

const App= () =>{

   


    return (
        <main>
            <Switch>
               <Route path="/movies">
                  <Movies/>
                </Route>

                <Route path="/books">
                  <Books/>
                </Route>

                <Route path="/TVShows">
                  <Shows/>
                </Route>
                <Route path="/Games">
                  <Game/>
                </Route>


                <Route path="/">
                  <Home />
                </Route>

           </Switch>

        </main>
    )
}
export default App
