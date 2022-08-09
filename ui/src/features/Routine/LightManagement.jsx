import React, { useState } from "react";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Toggle from "./Toggle";
import LightBrightness from "./LightBrightnessCounter"


const defaultValues = {
    name: "",
    is_active: true,
    brightness: 0,

};
const LightManagement = ({device}) => {
    const [formValues, setFormValues] = useState(defaultValues);

    React.useEffect(() => {
        device && setFormValues(device)
    }, [device])


    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormValues({
            ...formValues,
            [name]: value,
        });
    };
    const handleSliderChange = (name) => (e, value) => {
        setFormValues({
            ...formValues,
            [name]: value,
        });
    };
    const handleSubmit = (event) => {
        event.preventDefault();
    };
    return (
        <form onSubmit={handleSubmit}>
            <Grid container alignItems="center" justify="center" direction="column" >
                <Grid item style={{ marginBottom: 15 }}>
                    <TextField
                        id="name-input"
                        name="name"
                        label="Device Nickname"
                        type="text"
                        value={formValues.name}
                        onChange={handleInputChange}
                    />
                </Grid>
                
                <Grid item >
                    <Grid container spacing={8} direction="row" justify="center" style={{ marginTop: 3, marginBottom: 3 }}>
                        <Grid item style={{ paddingTop: 43 }}>
                            Light On/Off
                        </Grid>
                        <Grid item >
                            <Toggle isChecked={formValues.is_active} />
                        </Grid>
                    </Grid>
                </Grid>
                <Grid item style={{ marginBottom: 40 }}>
                    <LightBrightness brightness={formValues.brightness} />
                </Grid>
            </Grid>
        </form>
    );
};
export default LightManagement;