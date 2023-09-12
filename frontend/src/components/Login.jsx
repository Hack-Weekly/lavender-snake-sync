import { Button, Label, TextInput } from "flowbite-react";
import { UserCircleIcon, LockClosedIcon } from "@heroicons/react/24/outline";
import { Link } from "react-router-dom";
import { useState } from "react";
export const Login = ({ handleLogin, failureLogin, setFailureLogin }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const handleFormClick = (e) => {
      e.preventDefault();
      handleLogin(username,password);
  }
  return (
    <form className="flex w-4/6 flex-col gap-4" onSubmit={handleFormClick}>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="email2" value="Your username" />
        </div>
        <TextInput
          icon={UserCircleIcon}
          color={failureLogin ? "failure" : ""}
          id="username"
          required
          shadow
          type="text"
          onChange={(e) => {
              setUsername(e.target.value);
              setFailureLogin(false);
            }}
        />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="password2" value="Your password" />
        </div>
        <TextInput
          icon={LockClosedIcon}
          color={failureLogin ? "failure" : ""}
          id="password2"
          required
          shadow
          type="password"
          onChange={(e) => {
              setPassword(e.target.value);
              setFailureLogin(false);
            }}
        />
      </div>
      <div className="flex flex-col items-center gap-2 dark:text-white">
        {failureLogin && <p className="text-red-700">Please enter a valid username or password !</p>}
        <div className="flex gap-2">
          Don’t have an account yet?{" "}
          <Link to="/signup">
            <span className="text-blue-500 underline">Sign up</span>
          </Link>
        </div>
      </div>
      <Button type="submit" className="bg-gradient-to-r from-purple-500 to-purple-700">
        Login
      </Button>
    </form>
  );
};
