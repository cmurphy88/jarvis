import * as React from 'react';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Link from '@mui/material/Link';

function handleClick(event) {
  event.preventDefault();
  console.info('You clicked a breadcrumb.');
}

export default function Breadcrumb({room}) {
  return (
    <div role="presentation" onClick={handleClick}>
      <Breadcrumbs aria-label="breadcrumb">
        <Link underline="hover" color="inherit" href="/">
          Home
        </Link>
        {room && <Link
          underline="hover"
          color="text.primary"
          href="/material-ui/react-breadcrumbs/"
          aria-current="page"
        >
          {room}
        </Link>}
      </Breadcrumbs>
    </div>
  );
}