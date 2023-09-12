import { Button, Label, TextInput } from "flowbite-react";
import {
  AtSymbolIcon,
  LockClosedIcon,
  UserCircleIcon,
} from "@heroicons/react/24/outline";
import { Link } from "react-router-dom";
import { useState } from "react";
export const Signup = ({ handleSignup, failureSignup, setFailureSignup }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const handleFormClick = (e) => {
    e.preventDefault();
    console.log(password);
    handleSignup(username, password, email);
  };
  return (
    <form className="flex w-4/6 flex-col gap-4" onSubmit={handleFormClick}>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="email2" value="Your email" />
        </div>
        <TextInput
          icon={AtSymbolIcon}
          id="email2"
          required
          shadow
          type="text"
          onChange={(e) => {
            setEmail(e.target.value);
            setFailureSignup(false);
          }}
        />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="username" value="Your username" />
        </div>
        <TextInput
          icon={UserCircleIcon}
          id="username"
          required
          shadow
          type="text"
          onChange={(e) => {
            setUsername(e.target.value);
            setFailureSignup(false);
          }}
        />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="password2" value="Your password" />
        </div>
        <TextInput
          icon={LockClosedIcon}
          id="password2"
          required
          shadow
          type="password"
          onChange={(e) => {
            setPassword(e.target.value);
            setFailureSignup(false);
          }}
        />
      </div>
      <div className="flex flex-col items-center gap-2 dark:text-white">
        {failureSignup && <p className="text-red-700">Please enter a valid data !</p>}
        <div>
          Already have an account?
          <Link to="/login">
            <span className="text-blue-500 underline">Login</span>
          </Link>
        </div>
      </div>
      <Button type="submit" className="bg-gradient-to-r from-purple-500 to-purple-700">
        Sign up
      </Button>
    </form>
  );
};
