import Layout from "../components/layout";
import styles from "../components/blog.module.css";
import BlogHero from "../components/blog";
import Link from "next/link";
import Date from "../components/date";
import { Card } from "primereact/card";

import { getSortedPostsData } from "../lib/posts";

export async function getStaticProps() {
  const allPostsData = getSortedPostsData();
  return {
    props: {
      allPostsData,
    },
  };
}

export default function Blog({ allPostsData }) {
  return (
    <>
      <Layout>
        <BlogHero />
      </Layout>
    </>
  );
}
