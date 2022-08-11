import React, { useState } from "react";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import Toggle from "./Toggle";
import LightBrightness from "./LightBrightnessCounter";

const defaultValues = {
    name: "",
    is_active: true,
    brightness: 100,
    type: "light",
};

const LightManagement = ({
    deviceSettings,
    setDeviceSettings,
    deviceName,
    handleFieldChange,
}) => {
    const [isOn, setIsOn] = useState(true);

    React.useEffect(() => {
        if (deviceSettings) {
            setIsOn(deviceSettings.is_active);
        }

        if (!deviceSettings) {
            setDeviceSettings(defaultValues);
        }

        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    React.useEffect(() => {
        if (deviceSettings) {
            const newForm = {
                ...deviceSettings,
                is_active: isOn,
                brightness: isOn ? deviceSettings.brightness : 0,
            };
            setDeviceSettings(newForm);
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [isOn]);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        const newForm = {
            ...deviceSettings,
            [name]: value,
        };
        setDeviceSettings(newForm);
    };

    const handleBrightnessChange = (value) => {
        handleFieldChange("brightness", value);
    };

    const handleChecked = () => {
        setIsOn(!isOn);
    };

    if (!deviceSettings) {
        return;
    }
    return (
        <Grid container alignItems="flex-end" direction="row">
            <Grid item xs={8} md={8}>
                <TextField
                    id="name-input"
                    name="name"
                    label="Selected Device"
                    type="text"
                    value={deviceSettings.name || deviceName}
                    onChange={handleInputChange}
                    style={{ width: "100%" }}
                    disabled
                />
            </Grid>
            <Grid item xs={4} md={4} style={{ alignSelf: "flex-end" }}>
                <Toggle
                    isChecked={deviceSettings.is_active}
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
                    <LightBrightness
                        brightness={deviceSettings.brightness}
                        handleFormInputChange={handleBrightnessChange}
                    />
                </Grid>
            )}
        </Grid>
    );
};
export default LightManagement;
