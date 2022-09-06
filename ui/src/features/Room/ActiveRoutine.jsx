import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Grid from "@material-ui/core/Grid";
import { getActiveRoutine } from "../../shared/api/RoutinesAPI";
import TextField from "@material-ui/core/TextField";
import Toggle from "../Routine/Toggle";
import LightBrightness from "../Routine/LightBrightnessCounter";
import TrvTemperature from '../Routine/TrvTemperature';

export default function ActiveRoutine({ roomId }) {
  const [routine, setRoutine] = React.useState(null)

  React.useEffect(() => {
    const fetchActiveRoutine = async () => {
      const data = await getActiveRoutine(roomId)
      setRoutine(data)
    };
    fetchActiveRoutine()
      .catch(console.error);
  }, [roomId])

  const getTime = (time_value) => {
    return time_value ? time_value.substring(0, 5) : ""
  }

  const renderLightSettings = (device) => {
    return (
      <Grid container key={device.name} alignItems="flex-end" direction="row">
        <Grid item xs={4} md={4}>
          <TextField
            id="name-input"
            name="name"
            label="Device"
            type="text"
            value={device.name}
            style={{ width: "100%" }}
            disabled
          />
        </Grid>
        <Grid item xs={4} md={2} style={{ alignSelf: "flex-end" }}>
          <Toggle
            isChecked={device.is_active}
            disabled={true}
          />
        </Grid>

        {device.is_active && (
          <Grid
            item
            xs={4}
            md={6}
            style={{
              marginTop: 20,
              display: "flex",
              justifyContent: "center",
            }}
          >
            <LightBrightness
              brightness={device.brightness}
              handleFormInputChange={() => { }}
              disabled={true}
            />
          </Grid>
        )}
      </Grid>
    )
  }

  const renderMediaSettings = (device) => {
    return (
      <Grid container key={device.name} alignItems="flex-end" direction="row">
        <Grid item xs={4} md={4}>
          <TextField
            id="name-input"
            name="name"
            label="Device"
            type="text"
            value={device.name}
            fullWidth
            disabled
          />
        </Grid>
        <Grid item xs={4} md={2} style={{ alignSelf: "flex-end", marginRight: 60 }}>
          <Toggle
            isChecked={device.is_active}
            handleChecked={() => { }}
            disabled={true} />
        </Grid>

        {device.is_active && (
          <Grid
            item
            xs={12}
            md={4}
            style={{
              marginTop: 20,
              // marginLeft: 60,
              display: "flex",
              justifyContent: "center",
            }}
          >
            <TextField
              id="name-input"
              name="media_url"
              label="Playing"
              type="text"
              value={device.media_url}
              style={{ width: "100%" }}
              disabled
            />
          </Grid>)}

      </Grid>
    )
  }

  const renderTrvSettings = (device) => {
    return (
      <Grid container key={device.name} alignItems="flex-end" direction="row">
        <Grid item xs={4} md={4}>
          <TextField
            id="name-input"
            name="name"
            label="Device"
            type="text"
            value={device.name}
            style={{ width: "100%" }}
            disabled
          />
        </Grid>

        <Grid item xs={4} md={2} style={{ alignSelf: "flex-end" }}>
          <Toggle
            isChecked={device.is_active}
            handleChecked={() => { }}
            disabled={true}
          />
        </Grid>

        {device.is_active && (
          <Grid
            item
            xs={4}
            md={6}
            style={{
              marginTop: 20,
              display: "flex",
              justifyContent: "center",
            }}
          >                 <TrvTemperature
              temperature={device.temperature}
              handleFormInputChange={() => { }}
              disabled={true}
            />
          </Grid>)}
      </Grid>
    )
  }



  if (!routine) return (
    <>
      <h2>Active Routine</h2>
      <p>No routine active</p>
    </>)

  return (
    <Box sx={{ p: 3 }}>
      <h2>Active Routine</h2>
      <Accordion>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1a-content"
          id="panel1a-header"
        >
          <Typography><b>{routine.name}:  </b>{ }
            {getTime(routine.start_time)} - {getTime(routine.end_time)}</Typography>
        </AccordionSummary>
        <AccordionDetails>


          {routine && routine.devices.map(d => {
            if (d.type === "light") {
              return renderLightSettings(d)
            }
            else if (d.type === "media") {
              return renderMediaSettings(d)
            }
            else if (d.type === "trv") {
              return renderTrvSettings(d)
            }

            return null
          })}

        </AccordionDetails>
      </Accordion>

    </Box>
  );
}
