import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Button } from "@material-ui/core";

export default function DeviceTable({
  routine,
  handleSelectedDevice,
  removeDevice,
}) {
  const renderRow = (row, index) => {
    return (
      <TableRow
        key={index}
        sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
      >
        <TableCell component="th" scope="row">
          {row.name}
        </TableCell>
        <TableCell>
          <Button
            color="primary"
            onClick={() => handleSelectedDevice(row, index)}
          >
            edit
          </Button>
        </TableCell>
        <TableCell>
          <Button color="primary" onClick={() => removeDevice(index)}>
            remove
          </Button>
        </TableCell>
      </TableRow>
    );
  };
console.log(routine)
  return (
    <TableContainer component={Paper} sx={{ marginTop: 3 }}>
      <Table sx={{ minWidth: 380 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Device</TableCell>
            <TableCell></TableCell>
            <TableCell></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {routine &&
            routine.devices.map((row, index) =>
              renderRow(row, index)
            )}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
