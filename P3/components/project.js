import React from "react";
import styles from "./project.module.css";
import Image from "next/image";
import calculatorImg from "../public/calculator.png";
import dashboardImg from "../public/dashboard.png";
import medicalDeviceImg from "../public/medicalDevice.png";
const Project = () => {
  return (
    <div className={`grid ${styles.heroSection}`}>
      <section className={styles.sectionProject}>
        <div className={styles.project_heading}>
          <span className={styles.span}>My Recent Projects</span>
          <h3>My Portfolio</h3>
        </div>

        <div className={styles.project_container}>
          <div className={styles.project_box}>
            <div className={styles.project_img}>
              <Image
                className={styles.project_img_img}
                src={calculatorImg}
                alt="Calculator image"
              />
            </div>

            <div className={styles.project_text}>
              <span>27 January 2023 | Project 1</span>
              <a
                href="https://github.com/ElianMrl/Elian_Portfolio.git"
                className={styles.project_tittle}
              >
                Data Science House Price Estimator
              </a>
              <p>
                Created a GUI that estimates House prices to help real estate
                investors negotiate house prices.
              </p>
              <a href="https://github.com/ElianMrl/Elian_Portfolio.git">
                Read More
              </a>
            </div>
          </div>
          <div className={styles.project_box}>
            <div className={styles.project_img}>
              <Image
                className={styles.project_img_img}
                src={dashboardImg}
                alt="Laptop Dashboard image"
              />
            </div>

            <div className={styles.project_text}>
              <span>21 December 2021 | Project 2</span>
              <a
                href="https://github.com/ElianMrl/Elian_Portfolio.git"
                className={styles.project_tittle}
              >
                Breasr Cancer Prediction
              </a>
              <p>
                Anallyzed and Compared Principal Component Analysis and Linear
                Discriminat Analysis. Findings: For Breast Cancer Prediction,
                the most accurate model is Linear Discriminant Analysis
              </p>
              <a href="https://github.com/ElianMrl/Elian_Portfolio.git">
                Read More
              </a>
            </div>
          </div>
          <div className={styles.project_box}>
            <div className={styles.project_img}>
              <Image
                className={styles.project_img_img}
                src={medicalDeviceImg}
                alt="Medical Device image"
              />
            </div>

            <div className={styles.project_text}>
              <span>02 June 2022 | Project 3</span>
              <a
                href="https://github.com/ElianMrl/Elian_Portfolio.git"
                className={styles.project_tittle}
              >
                NYC Car Accidents Web - Exploratory Data Analysis
              </a>
              <p>
                Cleaned, Organized, and Filtered over 1.9 million rows of data
                from NYC OpenData "Motor Vehicle Collisions - Crashes." and
                "2010 Neighborhood Tabulation Areas (NTAs)"
              </p>
              <a href="https://github.com/ElianMrl/Elian_Portfolio.git">
                Read More
              </a>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Project;
