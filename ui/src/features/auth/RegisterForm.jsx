import React from "react";
import React, { FormEvent } from "react";
import { Link } from "react-router-dom";
import useAuth from "../useAuth";

// Just regular CSS modules, style, however, you desire
import styles from "./index.module.css";

// This is a uncontrolled form! No need to manage state for each input!
export default function SignUpPage() {
  const { signUp, loading, error } = useAuth();

  async function handleSubmit(FormEvent) {
    preventDefault();

    const formData = new FormData(currentTarget);

    signUp(
      formData.get("username"),
      formData.get("first_name"),
      formData.get("last_name"),
      formData.get("password")
    );
  }

  return (
    <form className={"app"} onSubmit={handleSubmit}>
      <h1>Sign up</h1>

      {/*
          On a real world scenario, you should investigate
          the error object to see what's happening
      */}
      {error && <p className={"app"}>Sign up error!</p>}

      <label>
        Name
        <input name="first_name" />
      </label>

      <label>
        Name
        <input name="last_name" />
      </label>

      <label>
        Email
        <input name="username" type="email" />
      </label>

      <label>
        Password
        <input name="password" type="password" />
      </label>

      {/*
        While the network request is in progress,
        we disable the button. You can always add
        more stuff, like loading spinners and whatnot.
      */}
      <button disabled={loading}>Submit</button>

      <Link to="/login">Login</Link>
    </form>
  );
}