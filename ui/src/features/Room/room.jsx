import React, { useEffect } from "react";
import { Box, Button, Grid, ListItem } from "@mui/material";
import { Container } from "@mui/system";
import RoomIcon from "@mui/icons-material/Room";
import Breadcrumb from "../Navigation/Breadcrumb";
import RoutineTable from "./RoutineTable";
import MembersTable from "./MembersTable";
import DeviceTable from "./DeviceTable";
import { green } from "@mui/material/colors";
import RoutineModal from "../Routine/RoutineModal";
import {
  getRoomRoutines,
} from "../../shared/api/RoutinesAPI";
import { useParams } from "react-router-dom";
import { getRoom } from "../../shared/api/RoomAPI";

function RoomPage() {
  let { id } = useParams();
  const [displayModal, setDisplayModal] = React.useState(false);
  const [activeRoutine] = React.useState(false);

  const [routines, setRoutines] = React.useState([]);
  const [selectedRoutine, setSelectedRoutine] = React.useState(null);
  const [room, setRoom] = React.useState(null);


  useEffect(() => {
    const retrieveRoom = async () => {
      const data = await getRoom(id);
      setRoom(data);
    };

    retrieveRoom()
  }, [id])

  useEffect(() => {
    const fetchRoutines = async () => {
      const data = await getRoomRoutines(id);
      setRoutines(data);
    };

    fetchRoutines()
      // make sure to catch any error
      .catch(console.error);
  }, [id]);

  const handleSelectedRow = (routine) => {
    setSelectedRoutine(routine);
    setDisplayModal(true);
  };

  if (!room) {
    return
  }
  return (
    <div className="App">
      <Container maxWidth="md" sx={{ marginBottom: 5 }}>


        <Container sx={{ marginTop: 2 }}>
          <Breadcrumb room={room && room.name} />

<div style={{display: "flex", flexDirection: "row", justifyContent: "center", alignItems:"center"}}>
          <h2>{room && room.name}</h2>
          <RoomIcon fontSize="large" />
          </div>
          <Box
            borderColor="divider"
            borderTop={1}
            borderBottom={1}
            borderLeft={1}
            borderRight={1}
            sx={{ p: 3, marginBottom: 5}}
          >
            <h2>Current Routine: </h2>
            {activeRoutine ? (<RoutineTable
              routines={[]}
              handleSelectedRow={handleSelectedRow}

            />) : <p>No routine active</p>}
            
          </Box>
          <Box
            borderColor="divider"
            borderTop={1}
            borderBottom={1}
            borderLeft={1}
            borderRight={1}
            sx={{ p: 3 }}
          >
            <h2>Routines</h2>

            <RoutineTable
              routines={routines}
              handleSelectedRow={handleSelectedRow}
            />
            <RoutineModal
              roomId={id}
              isOpen={displayModal}
              handleClose={() => {
                setDisplayModal(false);
                setSelectedRoutine(null);
              }}
              selectedRoutine={selectedRoutine}
            />
            <Button
              variant="contained"
              sx={{ color: "white" }}
              onClick={() => setDisplayModal(true)}
            >
              Create Routine
            </Button>
          </Box>
        </Container>

        <Container sx={{ marginTop: 5 }}>
          <Box
            marginTop={5}
          >
            <Grid container spacing={3}>
              <Grid item xs>
                <Box
                  borderColor="divider"
                  borderTop={1}
                  borderBottom={1}
                  borderLeft={1}
                  borderRight={1}
                  sx={{ p: 3 }}>
                  <ListItem>
                    <h3>Members</h3>
                  </ListItem>
                  <MembersTable />
                  <Button variant="contained" sx={{ margin: 2 }}>
                    {" "}
                    Add member
                  </Button>
                  <Button
                    variant="contained"
                    sx={{ margin: 2, background: green[300] }}
                  >
                    {" "}
                    Edit order
                  </Button>
                </Box>
              </Grid>
              <Grid item xs>
                <Box
                  borderColor="divider"
                  borderTop={1}
                  borderBottom={1}
                  borderLeft={1}
                  borderRight={1}
                  sx={{ p: 3 }}>
                  <ListItem>
                    <h3>Devices</h3>
                  </ListItem>
                  <DeviceTable />
                  <Button variant="contained" sx={{ margin: 2 }}>
                    Add device
                  </Button>
                </Box>
              </Grid>
            </Grid>
          </Box>
        </Container>


      </Container>
    </div>
  );
}

export { RoomPage };
