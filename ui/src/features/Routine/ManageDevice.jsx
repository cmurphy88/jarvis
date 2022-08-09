import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import LightManagement from './LightManagement'
import { Button, Grid } from '@mui/material';
import MediaManagement from './MediaManager';
import TrvManagement from './TrvManager';

export default function ManageDevice({ selectedDevice, handleClose }) {

    const devices = [
        {
            value: 'light',
            label: 'Light',
        },
        {
            value: 'media',
            label: 'Media',
        },
        {
            value: 'trv',
            label: 'TRV',
        },
    ]

    const [device, setDevice] = React.useState('');

    React.useEffect(() => {
        selectedDevice && setDevice(selectedDevice.type)
    }, [selectedDevice])

    const [formValues, setFormValues] = React.useState({});
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormValues({
            ...formValues,
            [name]: value,
        });
    };

    const handleChange = (event) => {
        setDevice(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
    };

    const getDeviceSettings = () => {
        if (device === 'light') {
            return <LightManagement device={selectedDevice} />

        } else if (device === 'media') {
            return <MediaManagement device={selectedDevice} />

        } else if (device === 'trv') {
            return <TrvManagement device={selectedDevice} />
        }
    }

    return (
        <Box sx={{ minWidth: 200, marginTop: 5 }}>

            <form onSubmit={handleSubmit}>



                <FormControl fullWidth>
                    <InputLabel id="demo-simple-select-label">Device</InputLabel>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        value={device}
                        label="Device"
                        onChange={handleChange}
                        sx={{ marginBottom: 5, p: 2, display: 'block', textOverflow: 'ellipsis' }}
                        disabled={selectedDevice}
                    >
                        {devices.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                                {option.label}
                            </MenuItem>

                        ))}

                    </Select>



                    {/* <div style={{marginTop: "20px"}}>
                    <Button variant="contained">Cancel</Button>
                    <Button variant="contained">Confirm</Button>
                    </div> */}
                </FormControl>

            </form>
            {device && getDeviceSettings()}
            {
                device && (
                    <Grid container spacing={4}>
                        <Grid item>
                            <Button onClick={handleClose}>
                                Cancel
                            </Button>
                        </Grid>
                        <Grid item >
                            <Button variant='contained' type='submit'>
                                Confirm
                            </Button>
                        </Grid>

                    </Grid>)
            }

        </Box >
    );
}
