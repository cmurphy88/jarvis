import React, { useState } from "react";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import DeviceTable from "./DeviceTabel";
import AddIcon from '@mui/icons-material/Add';
import ManageDevice from "./ManageDevice";
import TimeSelector from "./TimeSelector";

const defaultValues = {
  "room_id": 0,
  "name": "",
  "startTime": "",
  "endTime": "",
  "devices": [],
}

const ManageRoutineForm = ({ routine }) => {
  const [isManagedView, setIsManagedView] = useState(false);
  const [formValues, setFormValues] = useState(defaultValues);
  const [selectedDevice, setSelectedDevice] = useState(null);

  React.useEffect(() => {
    routine && setFormValues(routine)
  }, [routine])

  const handleInputChange = (e) => {
    const { name, mediaUrl, value } = e.target;
    setFormValues({
      ...formValues,
      [name]: value,
      [mediaUrl]: value,
    });
  };
  const handleSubmit = (event) => {
    event.preventDefault();
  };

  const handleSelectedDevice = (device) => {
    setSelectedDevice(device)
    setIsManagedView(true)
  }

  function handleClose() {
    setIsManagedView(false);
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <Grid container direction="row">
          <Grid xs={12} md={12}>
            <TextField
              id="name-input"
              name="name"
              label="Routine name"
              type="text"
              value={formValues.name}
              onChange={handleInputChange}
              disabled={isManagedView}
              sx={{ display: "flex", justifyContent: "center" }}
            />
          </Grid>
          <Grid>
            <TextField
              id="start-time-input"
              name="startTime"
              label="Start Time"
              type="time"
              value={formValues.start_time}
              onChange={handleInputChange}
              disabled={isManagedView}

            />
            <TextField
              id="end-time-input"
              name="endTime"
              label="End Time"
              type="time"
              value={formValues.end_time}
              onChange={handleInputChange}
              disabled={isManagedView}
            />
          </Grid>
        </Grid>
      </form>

      {
        isManagedView ? (
          <div>
            <ManageDevice selectedDevice={selectedDevice} handleClose={handleClose} />
          </div>

        ) : (
          <>
            <Grid item>
              <DeviceTable routine={formValues} handleSelectedDevice={handleSelectedDevice} />
              <Button sx={{ width: "auto" }} color='primary' onClick={() => {
                setSelectedDevice(null)
                setIsManagedView(true)
              }}>{"Add device"}<AddIcon /></Button>

            </Grid>

            <br />
            <br />
            <Button variant="contained" color="primary" type="submit">
              Submit
            </Button>
          </>
        )
      }

    </>

  );
};
export default ManageRoutineForm;