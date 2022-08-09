import styled from "@emotion/styled";
import Button from "@mui/material/Button";

const CustomizedButton = styled(Button)`
    background-color: ${(props) => {
        if (props.theme === "primary") {
            return theme.primary.backgroundColor;
        }
        if (props.theme === "secondary") {
            return theme.secondary.backgroundColor;
        }

        return;
    }};
    margin: 5px;
    padding: 10px;
    width: 125px;
`;

const theme = {
    primary: {
        backgroundColor: "#9beba9",
    },
    secondary: {
        backgroundColor: "#dee0df",
    },
};

export { CustomizedButton };
