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

const ManageRoutineForm = ({ roomId, routine, handleModalClose }) => {
  const [isManagedView, setIsManagedView] = useState(false);
  const [routineSettings, setRoutineSettings] = useState(defaultValues);
  const [devicesToRemove, setDevicesToRemove] = useState([]);
  const [selectedRowId, setSelectedRowId] = useState(null);
  const [selectedDevice, setSelectedDevice] = useState(null);

  React.useEffect(() => {
    if(routine){
      routine.room_id = roomId
      setRoutineSettings(routine);
    }
    routine && setRoutineSettings(routine);
  }, [routine, roomId]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setRoutineSettings({
      ...routineSettings,
      [name]: value,
    });
  };
  const handleSubmit = () => {
    console.log("Save this routine....", routineSettings);
  };

  const handleSelectedDevice = (device, rowId) => {
    setSelectedDevice(device);
    setSelectedRowId(rowId);
    setIsManagedView(true);
  };

  const handleDevice = (device, rowId) => {
    if (device && rowId !== null) {
      updateDevice(device, rowId);
    } else if (device && !rowId) {
      addDevice(device);
    }

    setSelectedDevice(null);
    setSelectedRowId(null);
  };

  const addDevice = (device) => {
    const updatedForm = { ...routineSettings };
    updatedForm.devices = [...routineSettings.devices, device];
    setRoutineSettings(updatedForm);
    setIsManagedView(false);
  };

  const updateDevice = (device, rowId) => {
    const updatedForm = { ...routineSettings };
    updatedForm.devices.splice(rowId, 1, device);
    setRoutineSettings(updatedForm);
    setIsManagedView(false);
  };

  const removeDevice = (rowId) => {
    const updatedForm = { ...routineSettings };
    const deviceToRemove = updatedForm.devices[rowId];
    updatedForm.devices.splice(rowId, 1);
    setRoutineSettings(updatedForm);
    setDevicesToRemove([...devicesToRemove, deviceToRemove])
    setIsManagedView(false);
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
              value={routineSettings.name}
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
              value={routineSettings.start_time}
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
              value={routineSettings.end_time}
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
            rowId={selectedRowId}
            selectedDevice={selectedDevice}
            handleClose={handleClose}
            handleDevice={handleDevice}
          />
        </div>
      ) : (
        <>
          <Grid item>
            <DeviceTable
              routine={routineSettings}
              handleSelectedDevice={handleSelectedDevice}
              removeDevice={removeDevice}
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
              onClick={() => handleModalClose()}
            >
              Close
            </Button>
            <Button
              variant="contained"
              color="primary"
              onClick={() => handleSubmit()}
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
