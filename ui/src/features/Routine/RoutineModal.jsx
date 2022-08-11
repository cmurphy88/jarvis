import * as React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import ManageRoutineForm from "./ManageRoutineForm";

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 400,
  bgcolor: "background.paper",
  border: "2px solid #000",
  boxShadow: 24,
  p: 4,
  color: "#000",
};

export default function RoutineModal(props) {
  return (
    <Modal
      open={props.isOpen}
      onClose={props.handleClose}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
    >
      <Box sx={style}>
        <Typography id="modal-modal-title" variant="h6" component="h2">
          Routine
          <hr />
        </Typography>
        <ManageRoutineForm
          roomId={props.roomId}
          routine={props.selectedRoutine}
          handleModalClose={props.handleClose}
        />
      </Box>
    </Modal>
  );
}