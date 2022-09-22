import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import { addNewHome } from '../../shared/api/HomesAPI';
import { Controller, useForm } from 'react-hook-form';
import { TextField } from '@mui/material';
import useAuth from '../../provider/useAuth';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: { xs: 300, md: 400 },
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

export default function AddRoomModal() {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const { handleSubmit, control } = useForm();
    const { user } = useAuth()

    const createNewHome = (formData) => addNewHome(formData.home_name, user.id, true);

    // React.useEffect(() => {
    //     const settingNewHome = async () => {
    //         const data = await formData.home_name;
    //         setNewHome(data);
    //     };
    //     settingNewHome()
    // }, [data])


    // const successMessage = () => {
    //     <Alert severity="success">This is a success alert — check it out!</Alert>
    // };

    return (
        <div>
            <Button
                onClick={handleOpen}
                sx={{ padding: 2 }}
                display='flex'
                variant='contained'
            >
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
                        Add new home
                    </Typography>
                    <div>
                        <Controller
                            name="home_name"
                            control={control}
                            defaultValue=""
                            rules={{ required: "Name required" }}
                            render={({
                                field: { onChange, value },
                                fieldState: { error },
                            }) => (
                                <TextField
                                    id="outlined-name"
                                    label="Home name"
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
                    </div>
                    <Button
                        variant='contained'
                        sx={{ marginTop: 5 }}
                        onClick={
                            handleSubmit(createNewHome)
                        }
                    >
                        Submit
                    </Button>
                    {/* <Alert severity="success">This is a success alert — check it out!</Alert> */}
                    <Button
                        onClick={handleClose}
                        variant='contained'
                        sx={{ marginTop: 5, marginLeft: 5 }}
                    >
                        Cancel
                    </Button>
                </Box>
            </Modal>
        </div>
    );
}