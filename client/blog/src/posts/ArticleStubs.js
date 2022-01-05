import React, { Component , useState, useEffect} from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const ArticleStubs = () => {
    const server = process.env.REACT_APP_SERVER_URL;
    const [articles, setArticles] = useState([]);

    useEffect(()=>{
        axios.get(server)
            .then(res => {
                const postData = res.data;
                setArticles(postData.posts);
            })
      },[])

    
    return articles.map((_item, _index) => (
        <article className="blog-post" key={_item.slug}>
            <h2 className="blog-post-title">{_item.title}</h2>
            <p><i>{_item.author}</i></p>
            <span className="blog-post-stub-content" dangerouslySetInnerHTML = {{__html:_item.content}}/>
            <Link to={'post/'+_item.slug}>Continue reading</Link>
        </article>
    ))
}

export default ArticleStubs