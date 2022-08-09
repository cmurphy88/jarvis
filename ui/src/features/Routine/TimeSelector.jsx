import * as React from 'react';

export default function TimeSelector() {
  const [value, setValue] = React.useState(null);

  return (
    <>
      {/* <LocalizationProvider dateAdapter={AdapterDateFns} locale="en">
        <DesktopTimePicker
          label="For desktop"
          value={value}
          onChange={(newValue) => {
            setValue(newValue);
          }}
          renderInput={(params) => <TextField {...params} />}
        />
      </LocalizationProvider> */}
    </>
  );
}
