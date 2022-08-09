import React from "react";
import { Stack, Link, TextField, Alert } from "@mui/material";
import { Controller, useForm } from "react-hook-form";
import { CustomizedButton as Button } from "../../components/Button";
import useAuth from "../../provider/useAuth";

function LoginForm({ openRegister }) {
    const { login, loading, error } = useAuth();
    const { handleSubmit, control } = useForm();

    const handleLogin = (formData) => login(formData);

    if (loading) {
        return <div>Loading...</div>
    }

    return (
        <>
            <div>
                <h1>JARVIS</h1>
                <Controller
                    name="username"
                    control={control}
                    defaultValue=""
                    rules={{ required: "Username required" }}
                    render={({
                        field: { onChange, value },
                        fieldState: { error },
                    }) => (
                        <TextField
                            id="standard-email"
                            label="Username"
                            value={value}
                            onChange={onChange}
                            variant="standard"
                            error={!!error}
                            helperText={error ? error.message : null}
                        />
                    )}
                />
            </div>
            <br />
            <div>
                <Controller
                    name="password"
                    control={control}
                    defaultValue=""
                    rules={{ required: "Password required" }}
                    render={({
                        field: { onChange, value },
                        fieldState: { error },
                    }) => (
                        <TextField
                            id="outlined-name"
                            label="Password"
                            type="password"
                            value={value}
                            onChange={onChange}
                            variant="standard"
                            margin="dense"
                            error={!!error}
                            helperText={error ? error.message : null}
                        />
                    )}
                />
            </div>

            <Stack
                direction="row"
                spacing={4}
                justifyContent="center"
                sx={{ marginTop: 2 }}
            >
                {error && <Alert severity="error">{"Username and Password does not exist - Try Again"}</Alert>}
            </Stack>

            <Stack
                direction="row"
                spacing={4}
                justifyContent="center"
                sx={{ marginTop: 2 }}
            >
                <Button
                    variant="contained"
                    color="success"
                    type="submit"
                    onClick={handleSubmit(handleLogin)}
                    theme={"primary"}

                >
                    Login
                </Button>
            </Stack>
            <Link
                component="button"
                variant="body2"
                onClick={openRegister}
                sx={{ marginTop: 5 }}
            >
                REGISTER HERE
            </Link>
        </>
    );
}

export { LoginForm };
