import { Button, DarkThemeToggle, Navbar } from 'flowbite-react';
import { Link } from 'react-router-dom';
export const TopNavbar = () => {
  return (
    <Navbar className='py-1 shadow-sm' fluid>
      <Navbar.Brand>
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
          Lavander
        </span>
      </Navbar.Brand>
      <Navbar.Collapse>
        <Navbar.Link active href="#">
          <p>Home</p>
        </Navbar.Link>
        <Navbar.Link href="#">About us</Navbar.Link>
        <Navbar.Link href="#">Contact</Navbar.Link>
      </Navbar.Collapse>
      <div className="flex md:order-2 gap-2">
        <DarkThemeToggle />
        <Link to="/login"><Button size="sm" color='purple' pill outline>Login</Button></Link>
        <Link to="/signup"><Button size="sm" color='purple'  pill>Sign up</Button></Link>

        <Navbar.Toggle />
      </div>
    </Navbar>
  );
};
