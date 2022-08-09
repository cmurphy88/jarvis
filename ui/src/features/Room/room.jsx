import React, { useEffect } from "react";
import { Box, Button, Grid, ListItem } from "@mui/material";
import { Container } from "@mui/system";
import RoomIcon from '@mui/icons-material/Room';
import Breadcrumb from "../Navigation/Breadcrumb";
import RoutineTable from "./RoutineTable";
import MembersTable from "./MembersTable";
import DeviceTable from "./DeviceTable";
import { green } from "@mui/material/colors";
import RoutineModal from "../Routine/RoutineModal";
import { getAllUsersRoutines, getUsersRoutines } from "../../shared/api/RoutinesAPI";
import useAuth from "../../provider/useAuth";

const routineMockData = [
  {
    "id": 1,
    "name": "Morning",
    "user": "Conor",
    "startTime": "08:00",
    "endTime": "10:00",
    "devices": [
      {
        "id": 1,
        "name": "HEAT",
        "temperature": 50,
        "is_active": true,
        "type": "trv",

      },
      {
        "id": 1,
        "name": "Test Light",
        "brightness": 20,
        "is_active": true,
        "type": "light"
      },
      {
        "id": 1,
        "name": "Alexa",
        "media_url": "test.com",
        "is_active": true,
        "type": "media",
      },
    ]

  },
  {
    "id": 2,
    "room_id": 1,
    "name": "Night",
    "user": "Nathan",
    "startTime": "13:00",
    "endTime": "14:00",
    "devices": [
      {
        "id": 1,
        "name": "HEAT",
        "temperature": 50,
        "is_active": true,
        "type": "trv",

      },
      {
        "id": 1,
        "name": "Test Light",
        "brightness": 88,
        "is_active": true,
        "type": "light"
      },
      {
        "id": 1,
        "name": "Alexa",
        "media_url": "",
        "is_active": false,
        "type": "media",
      },
    ]
  }
]




function RoomPage() {
  const { user } = useAuth()
  const [displayModal, setDisplayModal] = React.useState(false);
  const [routines, setRoutines] = React.useState(routineMockData);
  const [selectedRoutine, setSelectedRoutine] = React.useState(null);

  React.useEffect(() => {
    console.log("Call Routine Endpoint now...")
    //setRoutines(response.data)
  }, [])

  useEffect(() => {
    const fetchRoutines = async () => {
      const data = await getAllUsersRoutines(user.id);
      setRoutines(data)
      console.log("User...", user.id)
      console.log("Routines...", routines)
    }

    fetchRoutines()
      // make sure to catch any error
      .catch(console.error);
  }, [user])

  const handleSelectedRow = (routine) => {
    setSelectedRoutine(routine);
    setDisplayModal(true)
  }

  return (
    <div className="App">
      <Container maxWidth='md' sx={{ marginBottom: 20 }}>
        <Breadcrumb />
        <Box
          borderColor="primary.main"
          borderTop={2}
          borderBottom={2}
          borderLeft={2}
          borderRight={2}
        // marginTop={5}
        >
          <h2>Kitchen</h2>
          <RoomIcon fontSize="large" />

          <Container>

          </Container>

          <Container sx={{ marginTop: 5 }}>
            <Box
              borderColor="primary.main"
              borderTop={2}
              borderBottom={2}
              borderLeft={2}
              borderRight={2}

            // marginTop={5}
            >
              <h2>Routines</h2>

              <RoutineTable routines={routines} handleSelectedRow={handleSelectedRow} />
              <RoutineModal isOpen={displayModal} handleClose={() => {
                setDisplayModal(false)
                setSelectedRoutine(null)
              }} selectedRoutine={selectedRoutine} />
              <Button variant="contained" sx={{ marginBottom: 5, color: 'white' }} onClick={() => setDisplayModal(true)}>
                Create Routine
              </Button>


            </Box>
          </Container>

          <Box
            borderColor="primary.main"
            borderTop={2}
            borderBottom={2}
            borderLeft={2}
            borderRight={2}
            marginTop={5}
          >

            <Grid container spacing={3}>
              <Grid item xs>
                <ListItem>
                  <h3>Members</h3>
                </ListItem>
                <MembersTable />
                <Button variant='contained' sx={{ margin: 2 }}> Add member</Button>
                <Button variant='contained' sx={{ margin: 2, background: green[300] }}> Edit order</Button>
              </Grid>
              <Grid item xs>
                <ListItem>
                  <h3>Devices</h3>
                </ListItem>
                <DeviceTable />
                <Button variant='contained' sx={{ margin: 2 }}>Add device</Button>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>

    </div>
  );
}

export { RoomPage };
