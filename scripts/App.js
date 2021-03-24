import React from "react"
import Home from "./components/Home"
import Socket from "./Socket";
import Movies from "./components/Movies"
import Error from "./components/Error"
import {Switch , Route} from "react-router-dom"

const App= () =>{

   


    return (
        <main>
            <Switch>
               <Route path="/movies">
                  <Movies/>
                </Route>

                <Route path="/">
                  <Home />
                </Route>

           </Switch>

        </main>
    )
}
export default App
