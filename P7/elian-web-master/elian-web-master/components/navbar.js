import styles from "./navbar.module.css";
import Image from "next/image";
import logoImg from "../public/logoE.png";
import Link from "next/link";

const Navbar = () => {
  return (
    <div className={styles.navbarContainer}>
      <Link href="/">
        <Image
          src={logoImg}
          width={50}
          height={40}
          alt="Elian morales Pina Home Page"
        />
      </Link>
      <nav>
        <ul className={styles.navLinks}>
          <li className={styles.navLiabutton}>
            <a className={styles.navLiabutton} href="/services">
              Services
            </a>
          </li>
          <li className={styles.navLiabutton}>
            <a className={styles.navLiabutton} href="/project">
              Projects
            </a>
          </li>
          <li className={styles.navLiabutton}>
            <a className={styles.navLiabutton} href="/about">
              About
            </a>
          </li>
        </ul>
      </nav>

      <div className={styles.btn_box}>
        <a href="/resume">Resume</a>
      </div>
    </div>
  );
};

export default Navbar;
