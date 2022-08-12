import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import { red } from '@material-ui/core/colors';
import { getHomeRooms } from '../../shared/api/RoomAPI';
import { Link } from 'react-router-dom';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

export default function RemoveRoomModal({ home }) {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const [rooms, setRooms] = React.useState()

    React.useEffect(() => {
        const fetchRooms = async () => {
            if(home && home.id) {
                const data = await getHomeRooms(home.id);
                setRooms(data)
            }
        }

        fetchRooms()
            // make sure to catch any error
            .catch(console.error);
    }, [home])

    return (
        <div>
            <Button onClick={handleOpen} sx={{ color: red[700] }}>
                {/* <AddIcon fontSize='large' /> */}
                Remove
            </Button>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <Typography id="modal-modal-title" variant="h6" component="h2">
                        This is the remove room modal
                    </Typography>
                    <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                        This is where you can remove a room from the house...
                        Please select which room you would like to remove:

                        {rooms && rooms.map((r, i) => {
                            return <Link key={i} href={'rooms/' + r.id}>
                                primary={r.name}
                            </Link>
                        })}
                    </Typography>
                    <Button variant='contained' color='error' sx={{ marginTop: 5 }}>Remove Room</Button>
                    <Button onClick={handleClose} variant='contained' sx={{ marginTop: 5, marginLeft: 5 }}>Cancel</Button>
                </Box>
            </Modal>
        </div>
    );
}