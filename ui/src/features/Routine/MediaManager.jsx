import React, { useState } from "react";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import Toggle from "./Toggle";

const defaultValues = {
    name: "",
    is_active: true,
    media_url: "",
    type: "media",
};

const MediaManagement = ({
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
                media_url: isOn ? deviceSettings.media_url : "",
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

    const handleChecked = () => {
        setIsOn(!isOn);
    };

    // const handleMediaUrlChange = (value) => {;
    //     handleFieldChange("media_url", value)
    // }

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
                    fullWidth
                    disabled
                />
            </Grid>
            <Grid item xs={4} md={4} style={{ alignSelf: "flex-end" }}>
                <Toggle
                    isChecked={deviceSettings.is_active}
                    handleChecked={handleChecked} />
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
                >                    <TextField
                        id="name-input"
                        name="media_url"
                        label="Media URL"
                        type="text"
                        value={deviceSettings.media_url}
                        onChange={handleInputChange}
                        style={{ width: "100%" }}
                    />
                </Grid>)}

        </Grid>
    );
};
export default MediaManagement;