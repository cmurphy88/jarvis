import * as React from "react";
import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import Slider from "@mui/material/Slider";
import MuiInput from "@mui/material/Input";
import LightbulbIcon from "@mui/icons-material/Lightbulb";

const Input = styled(MuiInput)`
    width: 42px;
`;

export default function LightBrightness({ brightness, handleFormInputChange, disabled = false }) {
  const [value, setValue] = React.useState(100);

  React.useEffect(() => {
    setValue(brightness);
  }, [brightness]);

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
    if (value < 0) {
      setValue(0);
    } else if (value > 100) {
      setValue(100);
    }
  };

  return (
    <Box sx={{ width: 250 }}>
      <Typography id="input-slider" gutterBottom>
        Brightness
      </Typography>
      <Grid container spacing={2} alignItems="center">
        <Grid item>
          <LightbulbIcon />
        </Grid>
        <Grid item xs>
          <Slider
            value={typeof value === "number" ? value : 0}
            onChange={handleSliderChange}
            aria-labelledby="input-slider"
            disabled={disabled}
          />
        </Grid>
        <Grid item>
          <Input
            value={value}
            size="small"
            onChange={handleInputChange}
            onBlur={handleBlur}
            inputProps={{
              step: 10,
              min: 0,
              max: 100,
              type: "number",
              "aria-labelledby": "input-slider",
            }}
            disabled={disabled}
          />
        </Grid>
      </Grid>
    </Box>
  );
}
