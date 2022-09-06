import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import MuiInput from '@mui/material/Input';
import DeviceThermostatIcon from '@mui/icons-material/DeviceThermostat';

const Input = styled(MuiInput)`
  width: 42px;
`;

export default function TrvTemperature({ temperature, handleFormInputChange, disabled = false }) {

    React.useEffect(() => {
        setValue(temperature)
    }, [temperature])

    const [value, setValue] = React.useState(0);

    const handleSliderChange = (event, newValue) => {
        setValue(newValue);
        handleFormInputChange(newValue);
    };

    const handleInputChange = (event) => {
        const newValue =
            event.target.value === "" ? "" : Number(event.target.value);
        setValue(newValue);
        handleFormInputChange(newValue);
    };

    const handleBlur = () => {
        if (value < 25) {
            setValue(25);
        } else if (value > 35) {
            setValue(35);
        }
    };

    return (
        <Box sx={{ width: 250 }}>
            <Typography id="input-slider" gutterBottom>
                Temperature
            </Typography>
            <Grid container spacing={2} alignItems="center">
                <Grid item>
                    <DeviceThermostatIcon sx={{ display: { xs: "none", md: "flex" } }}
                    />
                </Grid>
                <Grid item xs>
                    <Slider
                        value={typeof value === 'number' ? value : 0}
                        onChange={handleSliderChange}
                        aria-labelledby="input-slider"
                        max={35}
                        min={25}
                        disabled={disabled}
                        sx={{ display: { xs: "none", md: "flex" } }}
                    />
                </Grid>
                <Grid item>
                    <Input
                        value={value}
                        size="small"
                        onChange={handleInputChange}
                        onBlur={handleBlur}
                        disabled={disabled}
                        inputProps={{
                            step: 1,
                            min: 25,
                            max: 35,
                            type: 'number',
                            'aria-labelledby': 'input-slider',
                        }}
                    />
                </Grid>
            </Grid>
        </Box>
    );
}
