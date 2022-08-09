import React, { useState } from "react";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import Toggle from "./Toggle";
import MediaVolume from "./MediaVolumeControl";
import TrvTemperature from "./TrvTemperature";


const defaultValues = {
    name: "",
    ipAddress: ""

};
const TrvManagement = ({ device }) => {
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

                <Grid item >
                    <Grid container spacing={8} direction="row" justify="center" style={{ marginTop: 3, marginBottom: 3 }}>
                        <Grid item style={{ paddingTop: 43 }}>
                            TRV On/Off
                        </Grid>
                        <Grid item >
                        <Toggle isChecked={formValues.is_active} />
                        </Grid>
                    </Grid>
                </Grid>
                <Grid item style={{ marginBottom: 40 }}>
                    <TrvTemperature temperature={formValues.temperature}/>
                </Grid>
            </Grid>
        </form>
    );
};
export default TrvManagement;