import React from "react";
import axios from "axios";
import { useState } from "react";
import { useEffect } from "react";

const user_id = 1;

function Homes() {
    const url = "http://127.0.0.1:8000/homes/users/1"
    const [home, setHome] = useState(null);

    useEffect(() => {
        axios.get(url)
            .then(response => {
                setHome(response.data)
            });
    }, [url])

    if (home) {
        return (

            <div>
                {home.map(home => (
                     home.name
                ))} 
            </div>
            // <div className="app">
            //     <h3>{home[i].name} </h3>

            // </div>
        )
    } else {

    }
    return (
        <div>
            Error finding data
        </div>
    )
}






export { Homes };