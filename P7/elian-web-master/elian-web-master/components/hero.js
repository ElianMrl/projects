import React from "react";
import styles from "./hero.module.css";
import { useRouter } from "next/router";

const Hero = () => {
  return (
    <div className={styles.heroSection}>
      <section className={`grid ${styles.home}`}>
        <div className={`col-12 md:col-6 lg:col-3 ${styles.home_content}`}>
          <h1>Hi, I'm Elian Morales Pina</h1>
          <h3>Data Scientist and Web Devlopment Student</h3>
          <p>
            Welcome! I'm Elian, a driven data scientist with hands-on experience
            in developing health-related medical devices. My expertise
            encompasses the realms of machine learning, big data, statistics,
            and mathematics. While my journey began in the nexus of healthcare
            and data, I possess an unwavering enthusiasm to harness the power of
            data in diverse fields. Discover my projects, understand my passion,
            and let's collaborate to push the boundaries of what data can
            achieve.
          </p>
          <div className={styles.btn_box}>
            <a href="#">Hire Me</a>
            <a href="#">Let's Talk</a>
          </div>
        </div>
        <div
          className={`col-12 md:col-6 lg:col-3 ${styles.image_content}`}
        ></div>
      </section>
    </div>
  );
};

export default Hero;
