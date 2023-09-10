import { Button, DarkThemeToggle, Navbar } from 'flowbite-react';
export const TopNavbar = () => {
  return (
    <Navbar className='py-1 shadow-sm' fluid>
      <Navbar.Brand href="https://flowbite-react.com">
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
        <Button size="sm" color='purple' pill outline>Login</Button>
        <Button size="sm" color='purple'  pill>Sign up</Button>

        <Navbar.Toggle />
      </div>
    </Navbar>
  );
};
