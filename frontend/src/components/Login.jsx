import { Button, Label, TextInput } from "flowbite-react";
import { UserCircleIcon, LockClosedIcon } from "@heroicons/react/24/outline";
import { Link } from "react-router-dom";
export const Login = () => {
    return (
      <form className="flex w-4/6 flex-col gap-4">
        <div>
          <div className="mb-2 block">
            <Label htmlFor="email2" value="Your username" />
          </div>
          <TextInput
            icon={UserCircleIcon}
            id="username"
            required
            shadow
            type="text"
          />
        </div>
        <div>
          <div className="mb-2 block">
            <Label htmlFor="password2" value="Your password" />
          </div>
          <TextInput icon={LockClosedIcon} id="password2" required shadow type="password" />
        </div>
        <div className="flex items-center gap-2 dark:text-white">
            Don’t have an account yet? <Link to="/signup"><span className="text-blue-500 underline">Sign up</span></Link>
        </div>
        <Button type="submit" className="bg-gradient-to-r from-purple-500 to-purple-700">Login</Button>
      </form>
    );
};
