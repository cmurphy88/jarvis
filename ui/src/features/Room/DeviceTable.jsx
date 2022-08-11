import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Button } from '@mui/material';
import { mock_devices } from '../../mock/MockDevices';

export default function DeviceTable() {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 200 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell><b>Device</b></TableCell>
            <TableCell></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {mock_devices.map((row) => (
            <TableRow
              key={row.label}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.label}
              </TableCell>
              <TableCell align="right"><Button>edit</Button></TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
