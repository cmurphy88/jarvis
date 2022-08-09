import { TextField } from "@mui/material";
import React from "react";


function JoinHome() {
    return (
        <div className="app">
            <TextField
                label="Label"
                placeholder="Type in here…"
                error
                helperText="You got this wrong. Try again!"
            />
        </div>

    )




}

export { JoinHome };