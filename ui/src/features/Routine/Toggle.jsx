import * as React from "react";
import Switch from "@mui/material/Switch";
import FormControlLabel from "@mui/material/FormControlLabel";

export default function Toggle({ isChecked, handleChecked, disabled = false }) {
  const [checked, setChecked] = React.useState(false);

  React.useEffect(() => {
    setChecked(isChecked);
  }, [isChecked]);

  const handleChange = (event) => {
    setChecked(event.target.checked);
    handleChecked();
  };

  const labelText = checked ? "On" : "Off";
  return (
    <div>
      <FormControlLabel
        value="top"
        control={<Switch color="primary" />}
        label={labelText}
        labelPlacement="start"
        checked={checked}
        onChange={handleChange}
        disabled={disabled}
      />
    </div>
  );
}