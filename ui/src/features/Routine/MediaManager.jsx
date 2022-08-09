import React, { useState } from "react";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Toggle from "./Toggle";
import LightBrightness from "./LightBrightnessCounter"
import MediaVolume from "./MediaVolumeControl";


const defaultValues = {
    name: "",
    mediaUrl: "",

};
const MediaManagement = ({ device }) => {
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
    console.log("media...", formValues)
    return (
        <form onSubmit={handleSubmit}>
            <Grid container rowSpacing={2} alignItems="center" justify="center" direction="column" >
                <Grid item style={{ marginBottom: 15 }}>
                    <TextField
                        id="name-input"
                        name="name"
                        label="Device Nickname"
                        type="text"
                        value={formValues.name}
                        onChange={handleInputChange}
                        fullWidth
                    />
                </Grid>

                <Grid item style={{ marginBottom: 15 }}>
                    <TextField
                        id="name-input"
                        name="mediaUrl"
                        label="Media URL"
                        type="text"
                        value={formValues.media_url}
                        onChange={handleInputChange}

                    />
                </Grid>

                <Grid item >
                    <Grid container spacing={8} direction="row" justify="center" style={{ marginTop: 3, marginBottom: 3 }}>
                        <Grid item style={{ paddingTop: 43 }}>
                            Media On/Off
                        </Grid>
                        <Grid item >
                            <Toggle isChecked={formValues.is_active} />
                        </Grid>
                    </Grid>
                </Grid>

            </Grid>
        </form>
    );
};
export default MediaManagement;