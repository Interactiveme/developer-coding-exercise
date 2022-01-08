import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from "react-router-dom";



const Article = () => {
    const server = process.env.REACT_APP_SERVER_URL;
    const { slug } = useParams();
    const [article, setArticle] = useState({});

    useEffect(() => {
        axios.get(`${server}posts/${slug}`)
            .then(res => {
                const postData = res.data;
                setArticle(postData.post);
            })
    }, [server, slug])

    const ArticleContent = () => {

        const tags = renderTags()

        return (
            <div className='blog-post'>
                <span dangerouslySetInnerHTML={{ __html: article.content }} />
                <p><b>Tags: {tags}</b></p>
                <a href="/" className="stretched-link">Back</a>
            </div>)
    }

    const EmptyContent = () => (
        <div className='blog-post'>
            <h2 className="blog-post-title">Whoops</h2>
            <p>
                We couldn't find the article you were looking for. Please try reading one of our other great
                articles that we are sure you will enjoy.
            </p>
            <a href="/" className="stretched-link">Back</a>
        </div>
    )

    const renderTags = () => {
        let tags = [];
        if (article && article.tags)
            tags = article.tags

        return tags.length > 0 ? tags.join(', ') : ''
    }

    return article.content ? <ArticleContent article={article} /> : <EmptyContent />
}

export default Article