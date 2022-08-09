import React, { useState } from "react";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Toggle from "./Toggle";
import LightBrightness from "./LightBrightnessCounter";

const defaultValues = {
    name: "",
    is_active: true,
    brightness: 0,
};
const LightManagement = ({ device }) => {
    const [formValues, setFormValues] = useState(defaultValues);
    const [isOn, setIsOn] = useState(true);

    React.useEffect(() => {
        device && setFormValues(device);
        device && setIsOn(device.is_active);
    }, [device]);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormValues({
            ...formValues,
            [name]: value,
        });
    };
    const handleChecked = () => {
        setIsOn(!isOn);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
    };
    return (
        <form onSubmit={handleSubmit}>
            <Grid container alignItems="right" direction="row">
                <Grid item xs={8} md={8}>
                    <TextField
                        id="name-input"
                        name="name"
                        label="Device Nickname"
                        type="text"
                        value={formValues.name}
                        onChange={handleInputChange}
                        style={{ width: "100%" }}
                    />
                </Grid>
                <Grid xs={4} md={4} style={{ alignSelf: "flex-end" }}>
                    <Toggle
                        isChecked={formValues.is_active}
                        handleChecked={handleChecked}
                    />
                </Grid>

                {isOn && (
                    <Grid
                        item
                        xs={12}
                        md={12}
                        style={{
                            marginTop: 20,
                            display: "flex",
                            justifyContent: "center",
                        }}
                    >
                        <LightBrightness brightness={formValues.brightness} />
                    </Grid>
                )}
            </Grid>
        </form>
    );
};
export default LightManagement;