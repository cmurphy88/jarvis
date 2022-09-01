import * as React from "react";
import Box from "@mui/material/Box";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import LightManagement from "./LightManagement";
import { Button, Grid } from "@mui/material";
import MediaManagement from "./MediaManager";
import TrvManagement from "./TrvManager";
import { mock_devices } from "../../mock/MockDevices";

export default function ManageDevice({
    rowId,
    selectedDevice,
    handleClose,
    handleDevice,
}) {
    const types = [
        {
            value: "light",
            label: "Light",
        },
        {
            value: "media",
            label: "Media",
        },
        {
            value: "trv",
            label: "TRV",
        },
    ];

    const [deviceSettings, setDeviceSettings] = React.useState(null);
    const [device, setDevice] = React.useState("");
    const [type, setType] = React.useState("");

    React.useEffect(() => {
        selectedDevice && setType(selectedDevice.type);
        selectedDevice && setDevice(selectedDevice.name);
        selectedDevice && setDeviceSettings(selectedDevice);

    }, [selectedDevice]);

    React.useEffect(() => {
        if (deviceSettings !== null && deviceSettings.name !== device) {
            const newSettings = { ...deviceSettings };
            newSettings.name = device;
            setDeviceSettings(newSettings);
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [deviceSettings, device]);

    const handleFieldChange = (field, value) => {
        const newForm = {
            ...deviceSettings,
            [field]: value,
        };

        setDeviceSettings(newForm);
    };

    const handleTypeChange = (event) => {
        setType(event.target.value);
        setDevice(null);
    };

    const handleChange = (event) => {
        setDevice(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        handleDevice(deviceSettings, rowId);
    };

    const getDeviceSettings = () => {
        if (type === "light") {
            return (
                <LightManagement
                    deviceSettings={deviceSettings}
                    setDeviceSettings={setDeviceSettings}
                    handleFieldChange={handleFieldChange}
                    deviceName={device}
                />
            );
        } else if (type === "media") {
            return <MediaManagement
                deviceSettings={deviceSettings}
                setDeviceSettings={setDeviceSettings}
                handleFieldChange={handleFieldChange}
                deviceName={device}
            />;
        } else if (type === "trv") {
            return <TrvManagement
                deviceSettings={deviceSettings}
                setDeviceSettings={setDeviceSettings}
                handleFieldChange={handleFieldChange}
                deviceName={device}
            />;
        }
    };

    const selectedDeviceList = mock_devices.filter((d) => d.type === type);
    return (
        <Box sx={{ minWidth: 200, marginTop: 5 }}>
            <Grid container>
                <Grid item xs={5} md={5}>
                    <FormControl fullWidth>
                        <InputLabel id="demo-simple-select-label">
                            Type
                        </InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            value={type}
                            label="Type"
                            onChange={handleTypeChange}
                            sx={{
                                marginBottom: 2,
                                p: 2,
                                display: "block",
                                textOverflow: "ellipsis",
                            }}
                            disabled={selectedDevice}
                        >
                            {types.map((option) => (
                                <MenuItem
                                    key={option.value}
                                    value={option.value}
                                >
                                    {option.label}
                                </MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                </Grid>
                <Grid item xs={1} md={1} />
                <Grid item xs={6} md={6}>
                    <FormControl fullWidth>
                        <InputLabel id="demo-simple-select-label">
                            Device
                        </InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            value={device || ""}
                            label="Device"
                            onChange={handleChange}
                            sx={{
                                marginBottom: 2,
                                p: 2,
                                display: "block",
                                textOverflow: "ellipsis",
                            }}
                            disabled={!type}
                        >
                            {selectedDeviceList.map((option) => (
                                <MenuItem
                                    key={option.value}
                                    value={option.value}
                                >
                                    {option.label}
                                </MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                </Grid>
            </Grid>

            {device && getDeviceSettings()}

            <Grid
                container
                spacing={4}
                style={{
                    display: "flex",
                    justifyContent: "right",
                    marginTop: "20px",
                }}
            >
                <Grid item>
                    <Button
                        variant="contained"
                        color="secondary"
                        onClick={handleClose}
                    >
                        Cancel
                    </Button>
                </Grid>

                {device && (
                    <Grid item>
                        <Button
                            variant="contained"
                            color="primary"
                            type="submit"
                            onClick={handleSubmit}
                        >
                            Confirm
                        </Button>
                    </Grid>
                )}
            </Grid>
        </Box>
    );
}
