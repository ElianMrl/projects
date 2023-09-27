import React from "react";
import styles from "./resume.module.css";
import Image from "next/image";
import meImg from "../public/me_image.png";
const Resume = () => {
  return (
    <div className={styles.body}>
      <div className={styles.container}>
        <aside className={styles.sidebar} role="complementary">
          <div className={styles.sidebar_top}>
            <div className={styles.portrait}>
              <Image className={styles.img} src={meImg} alt="Random guy Img" />
            </div>
            <h2>Elian Morales Pina</h2>
            <h3>Data Scientist</h3>
            <div className={styles.links}>
              <a
                href="https://www.linkedin.com/in/elian-morales-pina-9733a3223"
                aria-label="Elian Morales Pina's LinkedIn profile"
                target="_blank"
              >
                <i class="fab fa-linkedin"></i>
              </a>
              <a
                href="https://www.instagram.com/elianmrl/"
                aria-label="Elian Morales Pina's Instagram profile"
                target="_blank"
              >
                <i class="fa-brands fa-instagram"></i>
              </a>
              <a
                href="https://github.com/ElianMrl/Elian_Portfolio"
                aria-label="Elian Morales Pina's GitHub Portfolio"
                target="_blank"
              >
                <i class="fab fa-github"></i>
              </a>
              <a
                href="mailto:elianpmrl@gmail.com"
                aria-label="Email Elian Morales Pina"
              >
                <i class="fab fas fa-envelope"></i>
              </a>
              <a href="tel:+6467260432" aria-label="Call Elian Morales Pina">
                <i class="fab fas fa-phone"></i>
              </a>
            </div>
            <section className={styles.sidebar_bottom}>
              <h4>Objective</h4>
              <p>
                A highly motivated and results-driven data scientist with a
                strong background in mathematics, extensive experience in
                developing medical devices, and a solid foundation in web
                development. Committed to leveraging analytical expertise and
                technological skills to drive data-informed decision-making and
                deliver innovative solutions.
              </p>
            </section>
          </div>
        </aside>

        <main className={styles.main_content} role="main">
          <header role="banner">
            <h1>Embarking on Every Data Adventure</h1>
          </header>

          <section className={styles.skills_section}>
            <h2>Skills</h2>
            <ul className={styles.skill_list}>
              <li>
                <i class="fab fa-python fa-skill-icon"></i> Python
              </li>
              <li>
                <i class="fab fa-r-project fa-skill-icon"></i> R
              </li>
              <li>
                <i class="fa-solid fa-c fa-skill-icon"></i> C++
              </li>
              <li>
                <i class="fas fa-chart-bar fa-skill-icon"></i> Data Analysis
              </li>
              <li>
                <i class="fas fa-robot fa-skill-icon"></i> Machine Learning
              </li>
              <li>
                <i class="fas fa-solid fa-circle-info fa-skill-icon"></i> Data
                Mining
              </li>
              <li>
                <i class="fas fa-solid fa-calculator fa-skill-icon"></i> Wolfram
                Mathematica
              </li>
              <li>
                <i class="fas fa-database fa-skill-icon"></i> SQL
              </li>
              <li>
                <i class="fas fa-solid fa-server fa-skill-icon"></i> Database
                Management and Design
              </li>
              <li>
                <i class="fab fa-github fa-skill-icon"></i> GitHub
              </li>
              <li>
                <i class="fab fa-solid fa-microscope fa-skill-icon"></i>
                PlayWright
              </li>
              <li>
                <i class="fab fa-aws fa-skill-icon"></i> Amazon Web Services
              </li>
              <li>
                <i class="fab fa-html5 fa-skill-icon"></i> HTML5
              </li>
              <li>
                <i class="fab fa-css3-alt fa-skill-icon"></i> CSS3
              </li>
            </ul>
          </section>

          <section className={styles.experience_section}>
            <h2>Experience</h2>
            <h3>
              Data Scientist | BeCare link LLC - <span>Manhattan, NY</span>
            </h3>

            <h4 className={styles.right_align}>2022 - present</h4>
            <ul>
              <li>
                Engineered software and hardware for medical devices, enhancing
                functionality and performance.
              </li>
              <li>
                Applied programming skills to extract medical data insights for
                informed decision-making.
              </li>
              <li>
                Implemented statistical techniques and neural network models for
                precise medical data analysis.
              </li>
              <li>
                Leveraged medical statistics and machine learning knowledge to
                innovate healthcare solutions.
              </li>
            </ul>
          </section>

          <section className={styles.education_section}>
            <h2>Education</h2>
            <h3>
              M.S. in Data Science - Comp Track | New Jersey Institute of
              Technology
            </h3>
            <h4>2023 - 2024</h4>
          </section>

          <section className={styles.projects_section}>
            <h2>Projects</h2>
            <h3>NYC Car Accidents - Website</h3>
            <ul>
              <li>
                Performed comprehensive analysis of NYC car accidents to
                identify high-risk zones and safety issues.
              </li>
              <li>
                Designed a website for visualizing this data with heat maps and
                alerting users of potential hazards.
              </li>
            </ul>

            <h3>Data Science House Price Estimator</h3>
            <ul>
              <li>
                Designed and implemented a user-friendly graphical user
                interface (GUI) for estimating house prices.
              </li>
              <li>
                Utilized machine learning techniques to predict house prices
                based on selected property characteristics.
              </li>
            </ul>

            <h3>Breast Cancer Prediction</h3>
            <ul>
              <li>
                Conducted a comprehensive analysis comparing two popular
                dimensionality reduction techniques: Principal Component
                Analysis (PCA) and Linear Discriminant Analysis (LDA) for breast
                cancer prediction.
              </li>
              <li>
                Evaluated the performance of both techniques in terms of
                accuracy and reliability.
              </li>
            </ul>
          </section>

          <section className={styles.certifications_section}>
            <h2>Certifications</h2>
            <h3>None</h3>
          </section>
        </main>
      </div>
    </div>
  );
};

export default Resume;
