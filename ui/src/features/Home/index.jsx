import React, { useState, useEffect } from "react";
import { Box } from "@mui/material";
import { CustomizedButton as Button } from "../../components/Button";
import { Container } from "@mui/system";
import HomeAccordian from "./HomeAccordian";
import HomeIcon from "@mui/icons-material/Home"
import { getUsersHomes } from "../../shared/api/HomesAPI";
import useAuth from "../../provider/useAuth";
import Breadcrumb from "../Navigation/Breadcrumb";

function HomePage() {
  const { user } = useAuth()
  const [homes, setHomes] = useState()

  useEffect(() => {
    // declare the data fetching function
    const fetchHomes = async () => {
      const data = await getUsersHomes(user.id);
      setHomes(data)
    }

    // call the function
    fetchHomes()
      // make sure to catch any error
      .catch(console.error);
  }, [user])

  return (
    <div className="App">
      <Container maxWidth='md'>
        <Breadcrumb />
        <Box
          borderColor="primary.main"
          borderTop={2}
          borderBottom={2}
          borderLeft={2}
          borderRight={2}
        // marginTop={5}
        >
          <h2>My Homes</h2>
          <HomeIcon fontSize="large" />

          <Container>
            {homes && homes.map((h, i) => {
              return <HomeAccordian key={h.id} home={h} />
            })}
          </Container>

          <Container sx={{ marginTop: 10 }}>
            <Box
              borderColor="primary.main"
              borderTop={2}
              borderBottom={2}
              borderLeft={2}
              borderRight={2}
            // marginTop={5}
            >
              <h2>Add Home</h2>
              <Container>
                <Box
                  component="span"
                  m={1}
                  display="flex"
                  justifyContent="space-between"
                  alignItems="center"
                >
                  <Button variant="contained" color="success" style={{ padding: "0px 100px", marginLeft: 50, marginBottom: 30 }}>
                    <h4>Create new home</h4>
                  </Button>
                  <Button variant="contained" style={{ padding: "15px 100px", marginRight: 50, marginBottom: 30 }}>
                    <h4>Join Home</h4>
                  </Button>
                </Box>

              </Container>
            </Box>
          </Container>



        </Box>

      </Container>

    </div>
  );
}

export { HomePage };
