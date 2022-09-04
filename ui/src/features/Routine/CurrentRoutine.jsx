// import * as React from 'react';
// import Accordion from '@mui/material/Accordion';
// import AccordionSummary from '@mui/material/AccordionSummary';
// import AccordionDetails from '@mui/material/AccordionDetails';
// import Typography from '@mui/material/Typography';
// import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
// import { Button, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@material-ui/core';

// export default function CurrentRoutineAccordion(currentRoutine =[], roomId, handleSelectedRoutine) {

//     const [currentRoutines, setCurrentRoutines] = React.useState([])
//     const [activeRoutine, setActiveRoutine] = React.useState()
//     const routines = [];

    

//     React.useEffect(() => {
//         const fetchDevices = async () => {
//             const data = await currentRoutine.currentRoutine;
//             // console.log(data);
//             setCurrentRoutines(data);
//             // console.log("Current Routine...", currentRoutines)
//         };
//         fetchDevices()
//             .catch(console.error);
//     }, [currentRoutine.currentRoutine]);

//     React.useEffect(() => {
//         const fetchActiveRoutine = async () => {
//             const data = currentRoutines
//             currentRoutines.map((row) => {
//                 routines.push(row)
//             })
//             setActiveRoutine(routines)
//         };
//         fetchActiveRoutine()
//             .catch(console.error);
//     }, [currentRoutine])

//     console.log("Selected Routines...", activeRoutine)


//     const renderRow = (row, index) => {
//         return (
//             <TableRow
//                 key={index}
//                 sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
//             >
//                 <TableCell component="th" scope="row">
//                     {row.name}
//                 </TableCell>
//                 <TableCell>
//                     <Button color="primary">edit</Button>
//                 </TableCell>
//             </TableRow>
//         );
//     }

//     return (
//         < div >
//             <Accordion>
//                 <AccordionSummary
//                     expandIcon={<ExpandMoreIcon />}
//                     aria-controls="panel1a-content"
//                     id="panel1a-header"
//                 >
//                     <Typography>{currentRoutine.name} { }
//                     {currentRoutine.currentRoutine.start_time} - {currentRoutine.currentRoutine.end_time}</Typography>
//                 </AccordionSummary>
//                 <AccordionDetails>
//                     <TableContainer component={Paper} sx={{ marginTop: 3 }}>
//                         <Table sx={{ minWidth: 380 }} aria-label="simple table">
//                             <TableHead>
//                                 <TableRow>
//                                     <TableCell>Device</TableCell>
//                                     <TableCell></TableCell>
//                                 </TableRow>
//                             </TableHead>
//                             <TableBody>
//                                 {/* {devices &&
//                                     devices.map((row, index) =>
//                                         renderRow(row, index)
//                                     )} */}
//                             </TableBody>
//                         </Table>
//                     </TableContainer>

//                 </AccordionDetails>
//             </Accordion>
//         </div >
//     );
// }

