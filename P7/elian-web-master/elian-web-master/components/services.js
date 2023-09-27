import React from "react";
import styles from "./services.module.css";
import Image from "next/image";
import calculatorImg from "../public/calculator.png";
import dashboardImg from "../public/dashboard.png";
import medicalDeviceImg from "../public/medicalDevice.png";
const Services = () => {
  return (
    <div className={styles.body}>
      <div className={styles.section}>
        <div className={styles.title}>
          <h1>My Services</h1>
        </div>

        <div className={styles.services}>
          <div className={styles.card}>
            <div className={styles.icon}>
              <i class="fa-brands fa-python"></i>
            </div>
            <h2>Data Science</h2>
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s
            </p>
            <a href="/resume" className={styles.button}>
              Read More
            </a>
          </div>
          <div className={styles.card}>
            <div className={styles.icon}>
              <i class="fas fa-calculator"></i>
            </div>
            <h2>Mathematics & Statistic</h2>
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s
            </p>
            <a href="/resume" className={styles.button}>
              Read More
            </a>
          </div>
          <div className={styles.card}>
            <div className={styles.icon}>
              <i class="fas fa-window-restore"></i>
            </div>
            <h2>Web Development</h2>
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s
            </p>
            <a href="/resume" className={styles.button}>
              Read More
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Services;
