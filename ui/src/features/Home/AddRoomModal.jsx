import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import { Controller, useForm } from 'react-hook-form';
import { TextField } from '@mui/material';
import { createNewRoom } from '../../shared/api/RoomAPI';

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

export default function AddRoomModal(home) {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const { handleSubmit, control } = useForm();

  // const createNewRoom = (formData) => addNewRoom(formData.home_name, user.id, true);

  const addNewRoom = (formData) => createNewRoom(formData.room_name, home.home.id);

  return (
    <div>
      <Button onClick={handleOpen}>
        {/* <AddIcon fontSize='large' /> */}
        Add room
      </Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Create a new room: <b>{home.home.name}</b>
          </Typography>
          <Controller
            name="room_name"
            control={control}
            defaultValue=""
            rules={{ required: "Name required" }}
            render={({
              field: { onChange, value },
              fieldState: { error },
            }) => (
              <TextField
                id="outlined-name"
                label="room name"
                type="text"
                value={value}
                onChange={onChange}
                variant="standard"
                margin="dense"
                error={!!error}
                helperText={error ? error.message : null}
                required
              />
            )}
          />
          <Box>
            <Button
              variant='contained'
              sx={{ marginTop: 5 }}
              onClick={
                handleSubmit(addNewRoom)
              }
            >
              submit
            </Button>
            <Button
              onClick={handleClose}
              variant='contained'
              sx={{ marginTop: 5, marginLeft: 5 }}
            >
              Cancel
            </Button>
          </Box>

        </Box>
      </Modal>
    </div>
  );
}