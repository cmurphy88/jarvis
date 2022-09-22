import React, { useState, useEffect } from "react";
import { Box } from "@mui/material";
import { CustomizedButton as Button } from "../../components/Button";
import { Container } from "@mui/system";
import HomeAccordian from "./HomeAccordian";
import HomeIcon from "@mui/icons-material/Home"
import { getUsersHomes } from "../../shared/api/HomesAPI";
import useAuth from "../../provider/useAuth";
import AddHomeModal from "./AddHomeModal.jsx";

function HomePage() {
  const { user } = useAuth()
  const [homes, setHomes] = useState()
  const [displayModal, setDisplayModal] = React.useState(false);

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
      <Container
        maxWidth='md'
      >
        <Box sx={{ boxShadow: 3, p: 2 }}>
          <Box
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
              >
                <h2>Add Home</h2>
                <Container
                >
                  <Box
                    component="span"
                    m={1}
                    display="flex"
                    justifyContent="space-between"
                    alignItems="center"
                  >
                    <AddHomeModal
                      handleClose={() => {
                        setDisplayModal(false);
                      }}
                    />

                    <Button
                      variant="contained"
                      sx={{ display: "flex" }}
                      disabled
                    >
                      Join Home
                    </Button>
                  </Box>
                </Container>
              </Box>
            </Container>
          </Box>
        </Box>
      </Container>
    </div>
  );
}

export { HomePage };
