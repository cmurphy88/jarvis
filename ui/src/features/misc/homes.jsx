import { Container } from "@material-ui/core";
import React, { useState } from "react";
import { useEffect } from "react";
import { getUsersHomes } from "../../shared/api/HomesAPI";

function ShowAllHomes() {
    return (
        <div className="app">
            <h1>Homes</h1>
        </div>


    )
}

function ShowAllHomeUsers() {

    const [homes, setHomes] = useState()

    useEffect(() => {
        // declare the data fetching function
        const fetchHomes = async () => {
            const data = await getUsersHomes();
            setHomes(data)
        }

        // call the function
        fetchHomes()
            // make sure to catch any error
            .catch(console.error);
    }, [])

    const renderAllHomes = () => {
        return homes.map(home => {
            return (
                <div className="app">
                    <h3>{home.name}</h3>
                </div>
            )
        })
    }

    if (!homes) {
        return <div>No data present...</div>
    }

    return (
        <div>
            {renderAllHomes()}
        </div>
    )




}

export { ShowAllHomes, ShowAllHomeUsers };