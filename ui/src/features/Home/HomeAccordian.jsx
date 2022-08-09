import React, { useState, useEffect } from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { IconButton, ListItemButton, ListItemText } from '@mui/material';
import { blue, red } from '@mui/material/colors';
import { getHomeRooms } from '../../shared/api/RoomAPI';
import AddRoomModal from './AddRoomModal';
import RemoveRoomModal from './RemoveRoomModal';



export default function HomeAccordian({ home }) {
    const [rooms, setRooms] = useState()

    useEffect(() => {
        const fetchRooms = async () => {
            const data = await getHomeRooms(home.id);
            setRooms(data)
        }

        fetchRooms()
            // make sure to catch any error
            .catch(console.error);
    })


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
                <Typography>
                    {rooms && rooms.map((r, i) => {
                        return <ListItemButton key={i} component="a" href={'rooms/' + r.id}>
                            <ListItemText primary={r.name} />
                        </ListItemButton>
                    })}

                    <ListItemButton component="a">

                        <IconButton href='#' sx={{ color: blue[500] }} >
                            <AddRoomModal />
                        </IconButton>
                        <IconButton href='#' sx={{ color: red[500] }} >
                           <RemoveRoomModal />
                        </IconButton>
                    </ListItemButton>
                </Typography>
            </AccordionDetails>

        </Accordion>
    );
}
