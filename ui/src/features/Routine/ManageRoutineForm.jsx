import React, { useState } from "react";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import DeviceTable from "./DeviceTabel";
import AddIcon from "@mui/icons-material/Add";
import ManageDevice from "./ManageDevice";

const defaultValues = {
  room_id: 0,
  name: "",
  startTime: "",
  endTime: "",
  devices: [],
};

const ManageRoutineForm = ({ routine }) => {
  const [isManagedView, setIsManagedView] = useState(false);
  const [formValues, setFormValues] = useState(defaultValues);
  const [selectedDevice, setSelectedDevice] = useState(null);

  React.useEffect(() => {
    routine && setFormValues(routine);
  }, [routine]);

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
    setSelectedDevice(device);
    setIsManagedView(true);
  };

  function handleClose() {
    setIsManagedView(false);
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <Grid container direction="row">
          <Grid
            item
            xs={12}
            md={12}
            style={{ display: "flex", justifyContent: "left" }}
          >
            <TextField
              id="name-input"
              name="name"
              label="Routine name"
              type="text"
              value={formValues.name}
              onChange={handleInputChange}
              disabled={isManagedView}
              style={{ minWidth: "100%", paddingBottom: 20 }}
            />
          </Grid>
          <Grid item xs={6} md={6}>
            <TextField
              id="start-time-input"
              name="startTime"
              label="Start Time"
              type="time"
              value={formValues.start_time}
              onChange={handleInputChange}
              disabled={isManagedView}
              style={{ width: "90%" }}
            />
          </Grid>
          <Grid item xs={6} md={6}>
            <TextField
              id="end-time-input"
              name="endTime"
              label="End Time"
              type="time"
              value={formValues.end_time}
              onChange={handleInputChange}
              disabled={isManagedView}
              style={{ width: "90%" }}
            />
          </Grid>
        </Grid>
      </form>

      {isManagedView ? (
        <div>
          <ManageDevice
            selectedDevice={selectedDevice}
            handleClose={handleClose}
          />
        </div>
      ) : (
        <>
          <Grid item>
            <DeviceTable
              routine={formValues}
              handleSelectedDevice={handleSelectedDevice}
            />
            <Button
              style={{ width: "100%" }}
              color="primary"
              onClick={() => {
                setSelectedDevice(null);
                setIsManagedView(true);
              }}
            >
              {"Add device"}
              <AddIcon />
            </Button>
          </Grid>

          <div
            style={{
              display: "flex",
              flexDirection: "row",
              marginTop: "20px",
              justifyContent: "right",
            }}
          >
            <Button
              variant="contained"
              color="secondary"
              style={{ marginRight: "20px" }}
            >
              Close
            </Button>
            <Button
              variant="contained"
              color="primary"
              type="submit"
            >
              Save
            </Button>
          </div>
        </>
      )}
    </>
  );
};
export default ManageRoutineForm;