import Head from "next/head";
import Layout from "../components/layout";
import Project from "../components/project";

export default function Privacy() {
  return (
    <Layout>
      <div>
        <Head>
          <title>Privacy Policy</title>
        </Head>

        <main>
          <h1>Privacy Policy</h1>
          <p>Last updated: 2023</p>

          <section>
            <h2>Google Analytics</h2>
            <p>
              We use Google Analytics to understand the behavior of visitors on
              our site. This tool collects data such as pages visited, duration
              of visit, devices used, and geographic location.
            </p>
            <p>
              However, we respect your privacy and anonymize data like IP
              addresses to ensure they can't be linked back to individual users.
              Furthermore, we adhere to the data retention policies and
              practices mandated by Google.
            </p>
          </section>

          <section>
            <h2>GDPR & Your Data Rights</h2>
            <p>
              Under the General Data Protection Regulation (GDPR), you have
              several rights regarding your personal data:
            </p>
            <ul>
              <li>
                Right to Access: Know about the personal data being processed.
              </li>
              <li>Right to Erasure: Request deletion of your data.</li>
              <li>
                Data Portability: Ask for your data to be transferred to another
                service provider.
              </li>
              <li>And more...</li>
            </ul>
            <p>
              If you have concerns or would like to exercise any of these
              rights, please contact us at user@example.com.
            </p>
          </section>
        </main>
      </div>
    </Layout>
  );
}
