import './Home.css';
import ArticleStub from '../posts/ArticleSummary';


const Home = () => {

  return (
    <main className="container">
      <div className="p-4 p-md-5 mb-4 text-white rounded bg-dark">
        <div className="col-md-6 px-0">
          <h1 className="display-4 fst-italic">Joseph Smith's programming exercise</h1>
          <p className="lead my-3">I decided to use React for the frontend framework and Django for the backend. I'm currently unfimiliar with both, so I thought it could be a good oppertunity to learn something new.</p>
        </div>
      </div>
      <div className="row g-5">
        <div className="col-md-8">
          <ArticleStub />
        </div>
        <div className="col-md-4">
          <div className="position-sticky">
            <div className="p-4 mb-3 bg-light rounded">
              <h4 className="fst-italic">About</h4>
              <p className="mb-0">This is designed as a relatively simple exercise to get some code we can talk about in our technical interview. Not all developers have code that they can share with us due to IP restrictions, and this provides a common scenario across all candidates that provides some level of objective measure.</p>
            </div>
          </div>
        </div>
      </div>
    </main>

  );
}

export default Home;
