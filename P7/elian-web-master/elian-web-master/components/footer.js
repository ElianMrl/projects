import React from "react";
import styles from "./footer.module.css";

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <div className={`grid grid-nogutter ${styles.footerContainer} relative`}>
        <div className={styles.socialIcons}>
          <a href="">
            <i className="fa-brands fa-facebook"></i>
          </a>
          <a href="">
            <i className="fa-brands fa-instagram"></i>
          </a>
          <a href="">
            <i className="fa-brands fa-linkedin"></i>
          </a>
          <a href="">
            <i className="fa-brands fa-youtube"></i>
          </a>
        </div>
        <div className={styles.footerNav}>
          <ul>
            <li>
              <a href="/">Home</a>
            </li>
            <li>
              <a href="/services">Services</a>
            </li>
            <li>
              <a href="/about">About</a>
            </li>
            <li>
              <a href="resume">Contact Me</a>
            </li>
            <li>
              <a href="/privacy">Privacy</a>
            </li>
          </ul>
        </div>
      </div>
      <div className={styles.footerBottom}>
        <p>
          Copyright &copy;2023; Designed by{" "}
          <span className={styles.designer}>Elian</span>
        </p>
      </div>
    </footer>
  );
};

export default Footer;

/*
const Footer = () => {
  return (
    <div className={`grid grid-nogutter ${styles.footerContainer} relative`}>
      <footer className={styles.footer}>
        <div className={styles.container}>
          <div className={styles.row}>
            <div className={styles.footer_col}>
              <h4>Elian Morales Pina</h4>
              <ul>
                <li>
                  <a href="/about">about me</a>
                </li>
                <li>
                  <a href="/services">my services</a>
                </li>
                <li>
                  <a href="/project">Projects</a>
                </li>
              </ul>
            </div>
            <div className={styles.footer_col}>
              <h4>get help</h4>
              <ul>
                <li>
                  <a href="#">FAQ</a>
                </li>
                <li>
                  <a href="#">shipping</a>
                </li>
                <li>
                  <a href="#">returns</a>
                </li>
                <li>
                  <a href="#">order status</a>
                </li>
              </ul>
            </div>
            <div className={styles.footer_col}>
              <h4>online shop</h4>
              <ul>
                <li>
                  <a href="#">watch</a>
                </li>
                <li>
                  <a href="#">bag</a>
                </li>
                <li>
                  <a href="#">shoes</a>
                </li>
                <li>
                  <a href="#">dress</a>
                </li>
              </ul>
            </div>
            <div className={styles.footer_col}>
              <h4>follow me</h4>
              <div className={styles.social_links}>
                <a href="https://www.facebook.com/">
                  <FacebookOutlinedIcon
                    className="m-3 lg:m-5"
                    style={{ color: "#3b5998", fontSize: "30px" }}
                  />
                </a>
                <a href="https://www.twitter.com/">
                  <TwitterIcon
                    className="m-3 lg:m-5"
                    style={{ color: "#00acee", fontSize: "30px" }}
                  />
                </a>
                <a href="https://www.instagram.com/">
                  <InstagramIcon
                    className="m-3 lg:m-5"
                    style={{ color: "#D13C8C", fontSize: "30px" }}
                  />
                </a>
                <a href="https://www.instagram.com/">
                  <LinkedInIcon
                    className="m-3 lg:m-5"
                    style={{ color: "#0a66c2", fontSize: "30px" }}
                  />
                </a>
              </div>
            </div>
          </div>
          <p className="">© 2023 Elian Morales Pina. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default Footer;
*/
