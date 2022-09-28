import React, { useState, useEffect } from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { ListItemButton, ListItemText } from '@mui/material';
import { getHomeRooms } from '../../shared/api/RoomAPI';
import AddRoomModal from './AddRoomModal';
import RemoveRoomModal from './RemoveRoomModal';
import { useNavigate } from 'react-router-dom';
import { Box } from '@material-ui/core';



export default function HomeAccordian({ home }) {
    const [rooms, setRooms] = useState()
    const navigate = useNavigate()

    useEffect(() => {
        const fetchRooms = async () => {
            const data = await getHomeRooms(home.id);
            setRooms(data)
        }

        fetchRooms()
            // make sure to catch any error
            .catch(console.error);
    }, [home.id])


    return (
        <Accordion>
            <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls="panel1a-content"
                id="panel1a-header"
            >
                <Typography> {home.name} </Typography>
            </AccordionSummary>
            <AccordionDetails>
                {rooms && rooms.map((r, i) => {
                    return <ListItemButton key={i} onClick={() => navigate(`/rooms/${r.id}`)}>
                        <ListItemText primary={r.name}>{r.name}</ListItemText>
                    </ListItemButton>
                })}

                <Box sx={{ display: "flex", justifyContent: "right", p: 2 }}>
                    <AddRoomModal
                        home={home}
                    />
                    <RemoveRoomModal />
                </Box>
            </AccordionDetails>

        </Accordion>
    );
}
