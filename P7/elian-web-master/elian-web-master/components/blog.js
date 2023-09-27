import React from "react";
import styles from "./blog.module.css";
import Image from "next/image";
import calculatorImg from "../public/calculator.png";
import dashboardImg from "../public/dashboard.png";
import medicalDeviceImg from "../public/medicalDevice.png";

const BlogHero = () => {
  return (
    <div className={`grid ${styles.heroSection}`}>
      <section className={styles.sectionBlog}>
        <div className={styles.blog_heading}>
          <span className={styles.span}>My Recent Posts</span>
          <h3>My Blog</h3>
        </div>

        <div className={styles.blog_container}>
          <div className={styles.blog_box}>
            <div className={styles.blog_img}>
              <Image
                className={styles.blog_img_img}
                src={calculatorImg}
                alt="Calculator image"
              />
            </div>

            <div className={styles.blog_text}>
              <span>27 January 2023 | Mathematics</span>
              <a href="/posts/blog1" className={styles.blog_tittle}>
                A Journey of Numbers: Graduating with Honors in Mathematics at
                Hunter College
              </a>
              <p>
                I graduated with honors from Hunter College in NYC, earning a
                bachelor's degree in Mathematics.
              </p>
              <a href="/posts/blog1">Read More</a>
            </div>
          </div>
          <div className={styles.blog_box}>
            <div className={styles.blog_img}>
              <Image
                className={styles.blog_img_img}
                src={dashboardImg}
                alt="Laptop Dashboard image"
              />
            </div>

            <div className={styles.blog_text}>
              <span>21 December 2021 | Data Science</span>
              <a href="/posts/blog2" className={styles.blog_tittle}>
                My Journey as a Data Scientist
              </a>
              <p>
                Initially, I embarked on my journey as a self-taught data
                scientist. Later, I chose to further my expertise by pursuing a
                master's degree in Data Science.
              </p>
              <a href="/posts/blog2">Read More</a>
            </div>
          </div>
          <div className={styles.blog_box}>
            <div className={styles.blog_img}>
              <Image
                className={styles.blog_img_img}
                src={medicalDeviceImg}
                alt="Medical Device image"
              />
            </div>

            <div className={styles.blog_text}>
              <span>02 June 2022 | Medical Devices</span>
              <a href="/posts/blog1" className={styles.blog_tittle}>
                A Data Scientist Building Medical Devices
              </a>
              <p>
                I am currently employed as a data scientist, specializing in the
                creation of tools essential for medical device development. My
                work focuses on harnessing data to innovate and advance
                healthcare solutions.
              </p>
              <a href="/posts/blog1">Read More</a>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default BlogHero;
