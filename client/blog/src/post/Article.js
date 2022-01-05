import React, { Component , useState, useEffect} from 'react';
import axios from 'axios';
import { useParams } from "react-router-dom";

const Article = () => {
    const server = process.env.REACT_APP_SERVER_URL;
    const { slug } = useParams();
    const [article, setArticle] = useState({});

    useEffect(()=>{
        axios.get(`${server}posts/${slug}`)
            .then(res => {
                const postData = res.data;
                setArticle(postData.post);
            })
      },[])

    const renderTags = () => {
        const tags = article.tags || [];
        return tags.join(', ')
    };

    if(article.content){
        return (
            <main className="container">
                <article className="blog-post">
                    <h2 className="blog-post-title">{article.title}</h2>
                    <span dangerouslySetInnerHTML = {{__html:article.content}}/>
                    <p><b>Tags: {renderTags()}</b></p>
                    <a href="/" className="stretched-link">Back</a>
                </article>
            </main>
        )    
    } else {
        return (
            <main className="container">
                <article className="blog-post">
                    <h2 className="blog-post-title">Whoops</h2>
                    <p>We couldn't find the article you were looking for. Please try reading one of our other great articles that we are sure you will enjoy.</p>
                    <a href="/" className="stretched-link">Back</a>
                </article>
            </main>
        )
    }   
}

export default Article