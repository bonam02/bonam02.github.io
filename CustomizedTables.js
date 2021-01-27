import React from 'react';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Database from './Database';



const StyledTableCell = withStyles((theme) => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  body: {
    fontSize: 14,
  },
}))(TableCell);

const StyledTableRow = withStyles((theme) => ({
  root: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.action.hover,
    },
  },
}))(TableRow);

function createData(name, calories, fat, carbs, protein) {
  return { name, calories, fat, carbs, protein };
}





const useStyles = makeStyles({
  table: {
    minWidth: 700,
  },
});

const getData = (props) => {
  const dd = props
  console.log('ddop', dd)
}


export default function CustomizedTables(props) {
  const dd = props.data
  console.log('props-----', dd)
  const classes = useStyles();
  
if(dd)
{
  Object.keys(dd).map(function(key,index){
    console.log("key--",dd[key])
  })
  return (
  
    <TableContainer style={{"margin-top":"15%"}} component={Paper}>
      <Table className={classes.table} aria-label="customized table">
        <TableHead>
          <TableRow>

            <StyledTableCell align="right">ID</StyledTableCell>
            <StyledTableCell align="right">User_Id</StyledTableCell>
            <StyledTableCell align="right">Title</StyledTableCell>
            <StyledTableCell align="right">Body</StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {dd.data.map((row,col) => (         
            <StyledTableRow key={'hai'}>
              <StyledTableCell component="th" scope="row">{row.id}</StyledTableCell>
              <StyledTableCell align="right">{row.user_id}</StyledTableCell>
              <StyledTableCell align="right">{row.title}</StyledTableCell>
              <StyledTableCell align="right">{row.body}</StyledTableCell>
            </StyledTableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );


}
else{
  return ""
}





  
}
