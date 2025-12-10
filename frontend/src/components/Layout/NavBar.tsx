import React from 'react';

const NavBar: React.FC = () => {
  return (
    <nav className='bg-neutral-primary fixed w-full z-20 top-0 start-0 border-b border-default'>
      <div className='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'>
        <span className='self-center text-xl text-heading font-semibold whitespace-nowrap'>Sparee</span>
        <div className='hidden w-full md:block md:w-auto' id='navbar-default'>
          <ul className='font-medium flex flex-col p-4 md:p-0 mt-4 border border-default rounded-base bg-neutral-secondary-soft md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-neutral-primary'>
            <li>
              <a
                href='#'
                className='block py-2 px-3 text-heading rounded hover:bg-neutral-tertiary md:hover:bg-transparent md:border-0 md:hover:text-fg-brand md:p-0 md:dark:hover:bg-transparent'
              >
                Jobs
              </a>
            </li>
            <li>
              <a
                href='#'
                className='block py-2 px-3 text-heading rounded hover:bg-neutral-tertiary md:hover:bg-transparent md:border-0 md:hover:text-fg-brand md:p-0 md:dark:hover:bg-transparent'
              >
                Messages
              </a>
            </li>
            <li>
              <a
                href='#'
                className='block py-2 px-3 text-heading rounded hover:bg-neutral-tertiary md:hover:bg-transparent md:border-0 md:hover:text-fg-brand md:p-0 md:dark:hover:bg-transparent'
              >
                Profile
              </a>
            </li>
            <li>
              <a
                href='#'
                className='block py-2 px-3 text-heading rounded hover:bg-neutral-tertiary md:hover:bg-transparent md:border-0 md:hover:text-fg-brand md:p-0 md:dark:hover:bg-transparent'
              >
                Setting
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
