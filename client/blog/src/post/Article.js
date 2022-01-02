import React, { Component } from 'react';
import axios from 'axios';

export default class Article extends Component {

    state = {
        article: {}
    }

    componentDidMount() {
        debugger
        axios.get(`http://127.0.0.1:8000/posts/kiasuism-vs-no8-wire`)
            .then(res => {
                const postData = res.data;
                debugger;
                this.setState({ article: postData.data });
            })
    }

    renderTags (){
        const tags = this.state.article.tags;
        
    }

    render() {
        return (
            <main className="container">
                <article className="blog-post">
                    <h2 className="blog-post-title">{this.state.article.title}</h2>
                    <span>Tags: {this.renderTags()}</span>
                    <p>{this.state.article.content}</p>
                    <a href="/" className="stretched-link">Back</a>
                </article>
            </main>
        )
    }
}