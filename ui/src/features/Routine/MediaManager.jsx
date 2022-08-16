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
        <Grid
            container
            rowSpacing={2}
            alignItems="center"
            justify="center"
            direction="column"
        >
            <Grid item style={{ marginBottom: 15 }}>
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

            <Grid item style={{ marginBottom: 15 }}>
                <TextField
                    id="name-input"
                    name="media_url"
                    label="Media URL"
                    type="text"
                    value={deviceSettings.media_url}
                    onChange={handleInputChange}
                    style={{ width: "100%"}}
                />
            </Grid>

            <Grid item>
                <Grid
                    container
                    spacing={8}
                    direction="row"
                    justify="center"
                    style={{ marginTop: 3, marginBottom: 3 }}
                >
                    <Grid item>
                        <Toggle
                            isChecked={deviceSettings.is_active}
                            handleChecked={handleChecked}
                        />
                    </Grid>
                </Grid>
            </Grid>
        </Grid>
    );
};
export default MediaManagement;