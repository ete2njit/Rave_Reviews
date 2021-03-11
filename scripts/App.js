import React from "react"
import Home from "./components/Home"
import Socket from "./Socket";
import Movies from "./components/Movies"
import Error from "./components/Error"

const App= () =>{

    const [searchTerm, setSearchTerm] = React.useState("");
    const [searchCategory, setSearchCategory] = React.useState("");

    function handlePost(e) {
        e.preventDefault();

        Socket.emit("search request", {
            category: searchCategory,
            searchTerm: searchTerm,
        });
      }



    React.useEffect(() => {
    Socket.on("connected", (data) => {
        alert(data["test"]);
        });
    }, []);


    React.useEffect(() => {
    Socket.on("search response", (data) => {
        alert(data["title"]);
        });
    }, []);


    return (
        <main>
            <Home/>

            <form htmlFor="newitem" onSubmit={handlePost}>
              <label htmlFor="textbox">
                <input
                  type="text"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
              </label>
              <label htmlFor="textbox">
                <input
                  type="text"
                  value={searchCategory}
                  onChange={(e) => setSearchCategory(e.target.value)}
                />
              </label>
              <button
                className="submit-button"
                onClick={handlePost}
                variant="primary"
                type="submit"
                value="Submit"
              >
                Submit
              </button>
            </form>
        </main>
    )
}
export default App
